import math
import os.path

from cpexp.base import working_dir
from cpexp.ir.generator import *

template = None


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


# Generate intel syntax for nasm
class X86Generator(Generator):
    def generate(self, tac: list[Instruction]) -> str:
        prefix, suffix = get_template()
        generated = ''.join(map(self.gen, tac))
        # print(generated)
        return prefix + generated + suffix

    @meth_dispatch
    def gen(self, inst):
        raise Exception(f'Unable to generate from type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: SectionStartInst):
        return f'\n\tsection .{inst.name}\n'

    @gen.register
    def _(self, inst: DataInst):
        bits = inst.place.type.bits
        data_type = ''
        if bits > 64:
            raise Exception(f'Unsupported word length {bits}')
        elif bits <= 0:
            raise Exception(f'Invalid non-positive bits {bits}')
        elif bits <= 8:
            data_type = 'db'
        elif bits <= 16:
            data_type = 'dw'
        elif bits <= 32:
            data_type = 'dd'
        elif bits <= 64:
            data_type = 'dq'
        initial = inst.place.initial
        if initial is None:
            initial = 0
            # TODO: use BSS segment instead of this
        return f'\t{inst.place.name}: {data_type} {initial}\n'

    @gen.register
    def _(self, inst: FunctionStartInst):
        return f'\n_{inst.function}:\n' \
               f'\tpush\trbp\n' \
               f'\tmov \trbp, rsp\n' \
               f'\t; Alloc local variable\n' \
               f'\t; Store callee-saved registers\n'

    @gen.register
    def _(self, inst: FunctionEndInst):
        return f''

    @gen.register
    def _(self, inst: ConvertInst):
        return f'\t{inst.dst} := {inst.src_type}_to_{inst.dst_type}({inst.src})\n'

    @gen.register
    def _(self, inst: AssignInst):
        # TODO: use different register for different size
        # TODO: Alloc registers
        return f'\tmov \trax, {inst.right}\n' \
               f'\tmov \t{inst.left}, rax\n'

    @gen.register
    def _(self, inst: ReturnInst):
        return f'\t; Recover callee-saved registers\n' \
               f'\tmov \trsp, rbp\n' \
               f'\tpop \trbp\n' \
               f'\tmov \trax, {inst.value}\n' \
               f'\tret\n'

    @gen.register
    def _(self, inst: CallInst):
        push_args = ''
        for arg in inst.arguments:
            push_args += f'\tpush\tqword {str(arg)}\n'
        return push_args + \
               f'\t; Store caller-saved registers\n' \
               f'\tcall\t_{inst.function.name}\n' \
               f'\tmov \t{inst.place}, rax\n' \
               f'\t; Recover caller-saved registers\n' \
               f'\tadd \trsp, {inst.function.param_size}\n'

    @gen.register
    def _(self, inst: AllocInst):
        return f'\t[Alloc on stack {inst.local.name}({inst.local.type.bits}) = {inst.local.initial} at {inst.local.address}]\n'

    @gen.register
    def _(self, inst: TwoOperandAssignInst):
        return f'\t{inst.target} := {inst.operand1} {inst.OP} {inst.operand2}\n'

    @gen.register
    def _(self, inst: IfGotoInst):
        return f'\tif {inst.operand1} {inst.op} {inst.operand2} goto {inst.label}\n'

    @gen.register
    def _(self, inst: GotoInst):
        return f'\tgoto {inst.label}\n'

    @gen.register
    def _(self, inst: LabelInst):
        return f'{inst.label}:'

    @gen.register
    def _(self, inst: AsmInst):
        return f'{inst.code}\n'
