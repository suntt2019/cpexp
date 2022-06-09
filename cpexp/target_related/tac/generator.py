from cpexp.generic.generator import *
from cpexp.ir.base import Instruction


class TACGenerator(Generator):
    def generate(self, ir: list[Instruction]) -> str:
        return ''.join(map(self.gen, ir))
    
    @meth_dispatch
    def gen(self, inst):
        raise MessageException(f'Unable to generate from type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: DataInst):
        return ''

    @gen.register
    def _(self, inst: BSSInst):
        return ''

    @gen.register
    def _(self, inst: SectionStartInst):
        return ''

    @gen.register
    def _(self, inst: ConvertInst):
        return f'\t{inst.dst.name} := {inst.src.name}\n'

    @gen.register
    def _(self, inst: AssignInst):
        return f'\t{inst.left.name} := {inst.right.name}\n'

    @gen.register
    def _(self, inst: TwoOperandAssignInst):
        return f'\t{inst.target.name} := {inst.operand1.name} {inst.OP} {inst.operand2.name}\n'

    @gen.register
    def _(self, inst: IfGotoInst):
        return f'\tif {inst.operand1.name} {inst.op} {inst.operand2.name} goto {inst.label.name}\n'

    @gen.register
    def _(self, inst: GotoInst):
        return f'\tgoto {inst.label.name}\n'

    @gen.register
    def _(self, inst: LabelInst):
        return f'{inst.label.name}:'
