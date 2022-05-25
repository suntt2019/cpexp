import os.path
from itertools import zip_longest

from cpexp.base import working_dir
from cpexp.generic.generator import *
from cpexp.source_related.c4e.memory import C4eType
from cpexp.target_related.x86.instruction import *
from cpexp.target_related.x86.instruction import _TEXT
from cpexp.target_related.x86.register import *

template = None

# TODO: use different register for different size
# TODO: Alloc registers


def get_template():
    global template
    if template is not None:
        return template
    with open(os.path.join(working_dir, 'target_related', 'x86', 'template.s')) as f:
        content = f.read()
    prefix, _, leftover = content.partition('; PREFIX_END')
    _, _, suffix = leftover.partition('; SUFFIX_BEGIN')
    template = (prefix, suffix)
    return template


def bits_to_type(byte: int):
    if byte > 8:
        raise Exception(f'Unsupported word length {byte}')
    elif byte <= 0:
        raise Exception(f'Invalid non-positive bits {byte}')
    elif byte <= 1:
        data_type = 'b'
    elif byte <= 2:
        data_type = 'w'
    elif byte <= 4:
        data_type = 'd'
    else:  # bits <= 8
        data_type = 'q'
    return data_type


# Generate intel syntax for nasm
class X86Generator(Generator):
    def generate(self, ir: list[Instruction]) -> str:
        prefix, suffix = get_template()
        generated = sum(map(self.gen, ir), [])
        return prefix + self.tr_to_str(generated) + suffix

    @meth_dispatch
    def gen(self, x) -> list:
        raise Exception(f'Unable to generate from type {x.__class__.__name__} object {x}')

    @gen.register
    def _(self, inst: SymbolInst):
        return [
            _TEXT(f'\n{inst.type_name} {inst.name}\n')
        ]

    @gen.register
    def _(self, inst: SectionStartInst):
        return [
            _TEXT(f'\n\tsection .{inst.name}\n')
        ]

    @gen.register
    def _(self, inst: DataInst):
        if inst.place.type.name == 'string':
            initial = f'"{inst.place.initial.value}", 0'.replace('\\n', '", 10, "').replace(', ""', '')
            return [
                _TEXT(f'\t{inst.place.name}: db {initial}\n')
            ]
        return [
            _TEXT(f'\t{inst.place.name}: d{bits_to_type(inst.place.type.byte)} {inst.place.initial.value}\n')
        ]

    @gen.register
    def _(self, inst: BSSInst):
        return [
            _TEXT(f'\t{inst.place.name}: res{bits_to_type(inst.place.type.byte)} 1\n')
        ]

    @gen.register
    def _(self, inst: FunctionStartInst):
        alloc = []
        allocated_byte = inst.function.local_size
        stack_address = 8
        for param, reg in zip_longest(inst.function.param_list, [rdi, rsi, rdx, rcx, r8, r9]):
            if param is None:
                break
            allocated_byte += param.type.byte
            param.address = -allocated_byte
            if reg is not None:
                alloc += [MOV(param, reg)]
            else:
                stack_address += 8
                alloc += [MOV(param, Local('TMP_LOCAL', C4eType('long'), stack_address))]
        if allocated_byte > 0:
            # TODO: Add X86Type which is almost same with C4eType, then add conversion between them
            alloc = [SUB(rsp, Constant(C4eType('long'), allocated_byte))] + alloc
        return [
            _TEXT(f'\n{inst.function.name}:\n'),
            PUSH(rbp),
            MOV(rbp, rsp)
        ] + alloc

    @gen.register
    def _(self, inst: FunctionEndInst):
        return []

    @gen.register
    def _(self, inst: ConvertInst):
        return [
            _TEXT(f'\t; {inst.dst.name} := {inst.src.type.name}_to_{inst.dst.type.name}({inst.src.name})\n')
            # TODO: add float computing
        ]

    @gen.register
    def _(self, inst: AssignInst):
        return [
            MOV(rax, inst.right),
            MOV(inst.left, rax)
        ]

    @gen.register
    def _(self, inst: ReturnInst):
        if inst.value is None:
            assign = []
        else:
            assign = [MOV(rax, inst.value)]
        return [
                   MOV(rsp, rbp),
                   POP(rbp),
               ] + assign + [
                   RET()
               ]

    @gen.register
    def _(self, inst: CallInst):
        store_args = []
        for arg, reg in zip_longest(inst.arguments, [rdi, rsi, rdx, rcx, r8, r9]):
            if arg is None:
                break
            if reg is not None:
                store_args.append(MOV(reg, arg))
            else:
                store_args.append(PUSH(arg))
        assign = []
        if not isinstance(inst.place, VoidPlace):
            assign = [MOV(inst.place, rax)]
        recover_rsp = []
        pushed_count = max(0, len(inst.arguments) - 6)
        if pushed_count > 0:
            recover_rsp = [ADD(rsp, Constant(C4eType('long'), pushed_count))]
        return store_args + [CALL(inst.function)] + assign + recover_rsp

    @gen.register
    def _(self, inst: TwoOperandAssignInst):
        instructions = {
            '+': {
                'long': [ADD(rax, inst.operand2)]
            },
            '-': {
                'long': [SUB(rax, inst.operand2)]
            },
            '*': {
                'long': [MOV(rbx, inst.operand2), IMUL(rbx)]
            },
            '/': {
                'long': [XOR(rdx, rdx), MOV(rbx, inst.operand2), IDIV(rbx)]
            }
        }
        op = inst.OP
        type_name = inst.target.type.name
        if op not in instructions:
            raise Exception(f'Unsupported operator {op}')
        if type_name not in instructions[op]:
            raise Exception(f'Unsupported type {type_name} for operator {op}')
        return [MOV(rax, inst.operand1)] + instructions[op][type_name] + [MOV(inst.target, rax)]

    @gen.register
    def _(self, inst: IfGotoInst):
        instructions = {
            '>': {
                'long': [JG(inst.label)]
            },
            '<': {
                'long': [JL(inst.label)]
            },
            '==': {
                'long': [JE(inst.label)]
            },
        }
        op = inst.op
        type_name = inst.operand1.type.name
        if op not in instructions:
            raise Exception(f'Unsupported operator {op}')
        if type_name not in instructions[op]:
            raise Exception(f'Unsupported type {type_name} for operator {op}')
        return [
                   MOV(rax, inst.operand1),
                   CMP(rax, inst.operand2),
               ] + instructions[op][type_name]

    @gen.register
    def _(self, inst: GotoInst):
        return [JMP(inst.label)]

    @gen.register
    def _(self, inst: LabelInst):
        return [_TEXT(f'{inst.label.name}:')]

    @gen.register
    def _(self, inst: AsmInst):
        return [_TEXT(f'{inst.code}\n')]

    @gen.register
    def _(self, content: Label):
        return content.name

    @gen.register
    def _(self, content: Constant):
        return content.name

    @gen.register
    def _(self, content: Local):
        return f'qword [rbp{content.address:+d}]'

    @gen.register
    def _(self, content: Place):
        if content.type.name == 'string':
            return content.name
        return f'qword [{content.name}]'

    @gen.register
    def _(self, content: Function):
        return content.name
