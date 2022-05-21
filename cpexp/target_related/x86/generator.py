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
        return prefix + ''.join(map(self.gen, tac)) + suffix

    @meth_dispatch
    def gen(self, inst):
        raise Exception(f'Unable to generate from type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: DataInst):
        return f'[{inst.place.name}({inst.place.type.bits}) = {inst.place.initial}]\n'

    @gen.register
    def _(self, inst: FunctionStartInst):
        return f'\n_{inst.function}:\n' \
               f'\tpush\trbp\n' \
               f'\tmov\trbp, rsp\n' \
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
        return f'\t{inst.left} := {inst.right}\n'

    @gen.register
    def _(self, inst: ReturnInst):
        return f'\t; Recover callee-saved registers\n' \
               f'\tmov\trsp, rbp\n' \
               f'\tpop\trbp\n' \
               f'\tmov\trax, {inst.value}\n' \
               f'\tret\n'

    @gen.register
    def _(self, inst: CallInst):
        return f'\t[Push arguments: {", ".join(list(map(str, inst.arguments)))}]\n' \
               f'\t[Store caller-saved registers]\n' \
               f'\t{inst.place} := {inst.function.name}()\n' \
               f'\t[Recover caller-saved registers]\n' \
               f'\t[Dealloc arguments from stack(add ESP)]\n'

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
