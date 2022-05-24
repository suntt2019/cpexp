from cpexp.generic.generator import *
from cpexp.ir.base import Instruction


class TACGenerator(Generator):
    def generate(self, tac: list[Instruction]) -> str:
        return ''.join(map(self.gen, tac))
    
    @meth_dispatch
    def gen(self, inst):
        raise Exception(f'Unable to generate from type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: DataInst):
        return ''

    @gen.register
    def _(self, inst: ConvertInst):
        return f'\t{inst.dst} := {inst.src}\n'

    @gen.register
    def _(self, inst: AssignInst):
        return f'\t{inst.left} := {inst.right}\n'

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
