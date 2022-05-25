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


def byte_to_type(byte: int):
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
            _TEXT(f'\t{inst.place.name}: d{byte_to_type(inst.place.type.byte)} {inst.place.initial.value}\n')
        ]

    @gen.register
    def _(self, inst: BSSInst):
        return [
            _TEXT(f'\t{inst.place.name}: res{byte_to_type(inst.place.type.byte)} 1\n')
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
                alloc += [MOV(param, reg.resize(param))]
            else:
                stack_address += 8
                temp_local = Local('TEMP_LOCAL', C4eType('long'), stack_address)
                if param.type.byte == 8:
                    alloc += [MOV(param, temp_local)]
                else:
                    alloc += [
                        MOV(rax, temp_local),
                        MOV(param, AX(param))
                    ]
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
        src = inst.src.type.name
        dst = inst.dst.type.name
        if src == dst:
            raise Exception(f'Unexpected conversion instruction between same types')
        conv = []
        instructions = {}
        signed = ['int', 'long']
        if src in signed and dst in signed:
            # between signed
            if src == 'long':
                conv = [MOV(rax, inst.src)]
            else:
                conv = [MOVSX(rax, inst.src)]
        else:
            if src not in instructions:
                raise Exception(f'Unsupported source type {src}')
            if dst not in instructions[src]:
                raise Exception(f'Unsupported type {dst} converted from type {src}')
            conv = instructions[src][dst]
        return conv + [MOV(inst.dst, AX(inst.dst))]

    @gen.register
    def _(self, inst: AssignInst):
        return [
            MOV(AX(inst.right), inst.right),
            MOV(inst.left, AX(inst.left))
        ]

    @gen.register
    def _(self, inst: ReturnInst):
        if inst.value is None:
            assign = []
        else:
            assign = [MOV(AX(inst.value), inst.value)]
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
                if arg.type.byte == 8 or arg.type.name == 'string':
                    store_args += [MOV(reg, arg)]
                else:
                    store_args += [MOVSX(reg, arg)]
            else:
                if arg.type.byte == 8 or arg.type.name == 'string':
                    store_args += [PUSH(arg)]
                else:
                    store_args += [MOVSX(rax, arg), PUSH(rax)]
        if inst.function.varargs:
            store_args += [XOR(rax, rax)]
        assign = []
        if not isinstance(inst.place, VoidPlace):
            assign = [MOV(inst.place, AX(inst.place))]
        recover_rsp = []
        pushed_count = max(0, len(inst.arguments) - 6)
        if pushed_count > 0:
            recover_rsp = [ADD(rsp, Constant(C4eType('long'), pushed_count))]
        return store_args + [CALL(inst.function)] + assign + recover_rsp

    @gen.register
    def _(self, inst: TwoOperandAssignInst):
        instructions = {
            '+': {
                'signed': [ADD(AX(inst.operand2), inst.operand2)],
            },
            '-': {
                'signed': [SUB(AX(inst.operand2), inst.operand2)],
            },
            '*': {
                'signed': [MOV(BX(inst.operand2), inst.operand2), IMUL(BX(inst.operand2))],
            },
            '/': {
                'signed': [
                    XOR(DX(inst.operand2), DX(inst.operand2)),
                    MOV(BX(inst.operand2), inst.operand2),
                    IDIV(BX(inst.operand2))
                ],
            }
        }
        op = inst.OP
        type_name = inst.target.type.name
        if type_name in ['int', 'long']:
            type_name = 'signed'
        if op not in instructions:
            raise Exception(f'Unsupported operator {op}')
        if type_name not in instructions[op]:
            raise Exception(f'Unsupported type {type_name} for operator {op}')
        return [MOV(AX(inst.operand1), inst.operand1)] + instructions[op][type_name] + [
            MOV(inst.target, AX(inst.target))]

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
                   MOV(AX(inst.operand1), inst.operand1),
                   CMP(AX(inst.operand2), inst.operand2),
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
        return f'{byte_to_type(content.type.byte)}word [rbp{content.address:+d}]'

    @gen.register
    def _(self, content: Place):
        if content.type.name == 'string':
            return content.name
        return f'{byte_to_type(content.type.byte)}word [{content.name}]'

    @gen.register
    def _(self, content: Function):
        return content.name
