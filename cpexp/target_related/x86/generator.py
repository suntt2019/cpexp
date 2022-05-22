import os.path

from cpexp.base import working_dir
from cpexp.ir.generator import *
from cpexp.target_related.x86.instructions import *

template = None

# Register variables:
#   * simplify coding
#   * avoid typo
rax = 'rax'
rbx = 'rbx'
rcx = 'rcx'
rdx = 'rdx'
rsi = 'rsi'
rdi = 'rdi'
rsp = 'rsp'
rbp = 'rbp'


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


def bits_to_type(bits: int):
    if bits > 64:
        raise Exception(f'Unsupported word length {bits}')
    elif bits <= 0:
        raise Exception(f'Invalid non-positive bits {bits}')
    elif bits <= 8:
        data_type = 'b'
    elif bits <= 16:
        data_type = 'w'
    elif bits <= 32:
        data_type = 'd'
    else:  # bits <= 64
        data_type = 'q'
    return data_type


# Generate intel syntax for nasm
class X86Generator(Generator):
    def generate(self, tac: list[Instruction]) -> str:
        prefix, suffix = get_template()
        generated = ''.join(map(lambda x: ''.join(map(str, self.gen(x))), tac))
        return prefix + generated + suffix

    @meth_dispatch
    def gen(self, inst) -> list:
        raise Exception(f'Unable to generate from type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: SectionStartInst):
        return [
            f'\n\tsection .{inst.name}\n'
        ]

    @gen.register
    def _(self, inst: DataInst):
        return [
            f'\t{inst.place.name}: d{bits_to_type(inst.place.type.bits)} {inst.place.initial}\n'
        ]

    @gen.register
    def _(self, inst: BSSInst):
        return [
            f'\t{inst.place.name}: res{bits_to_type(inst.place.type.bits)} 1\n'
        ]

    @gen.register
    def _(self, inst: FunctionStartInst):
        alloc = []
        if inst.function.local_size > 0:
            alloc = [SUB(rsp, inst.function.local_size)]
        return [
            f'\n{inst.function.name}:\n',
            PUSH(rbp),
            MOV(rbp, rsp)
        ] + alloc

    @gen.register
    def _(self, inst: FunctionEndInst):
        return []

    @gen.register
    def _(self, inst: ConvertInst):
        return [
            f'\t; {inst.dst} := {inst.src_type}_to_{inst.dst_type}({inst.src})\n'
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
                   MOV('rsp', 'rbp'),
                   POP('rbp'),
               ] + assign + [
                   RET()
               ]

    @gen.register
    def _(self, inst: CallInst):
        push_args = []
        for arg in inst.arguments:
            push_args.append(PUSH(arg))
        assign = []
        if not isinstance(inst.place, VoidPlace):
            assign = [MOV(inst.place, rax)]
        return push_args + [CALL(inst.function.name)] + assign + [ADD('rsp', inst.function.param_size)]

    @gen.register
    def _(self, inst: AllocInst):
        return []

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
        return [f'{inst.label}:']

    @gen.register
    def _(self, inst: AsmInst):
        return [f'{inst.code}\n']
