from cpexp.generic.generator import *
from cpexp.ir.base import Instruction


class TACPGenerator(Generator):
    def generate(self, ir: list[Instruction]) -> str:
        return ''.join(map(self.gen, ir))

    @meth_dispatch
    def gen(self, inst):
        raise Exception(f'Unable to generate from type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: DataInst):
        return f'[{inst.place.name}({inst.place.type.byte}) = {inst.place.initial}]\n'

    @gen.register
    def _(self, inst: FunctionStartInst):
        return f'\n{inst.function} PROC\n' \
               f'\t[REG <-> Stack operate(EBP, ESP...)]\n' \
               f'\t[Store callee-saved registers]\n'

    @gen.register
    def _(self, inst: FunctionEndInst):
        return f'\n{inst.function.name} ENDP\n'

    @gen.register
    def _(self, inst: ConvertInst):
        return f'\t{inst.dst} := {inst.src_type}_to_{inst.dst_type}({inst.src})\n'

    @gen.register
    def _(self, inst: AssignInst):
        return f'\t{inst.left} := {inst.right}\n'

    @gen.register
    def _(self, inst: ReturnInst):
        return f'\t[Recover callee-saved registers]\n' \
               f'\t[REG <-> Stack operate(EBP, ESP...)(dealloc memory on stack)]\n' \
               f'\treturn {inst.value}\n'

    @gen.register
    def _(self, inst: CallInst):
        return f'\t[Push arguments: {", ".join(list(map(str, inst.arguments)))}]\n' \
               f'\t[Store caller-saved registers]\n' \
               f'\t{inst.place} := {inst.function.name}()\n' \
               f'\t[Recover caller-saved registers]\n' \
               f'\t[Dealloc arguments from stack(add ESP)]\n'

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
