from cpexp.ir.generator import *


class TACGenerator(Generator):
    def generate(self, tac: list[Instruction]) -> str:
        return ''.join(map(self.gen, tac))

    @Generator.gen.register
    def _(self, inst: AssignInst):
        return f'\t{inst.left} := {inst.right}\n'

    @Generator.gen.register
    def _(self, inst: TwoOperandAssignInst):
        return f'\t{inst.target}:={inst.operand1}{inst.OP}{inst.operand2}\n'

    @Generator.gen.register
    def _(self, inst: IfGotoInst):
        return f'\tif {inst.operand1} {inst.op} {inst.operand2} goto {inst.label}\n'

    @Generator.gen.register
    def _(self, inst: GotoInst):
        return f'\tgoto {inst.label}\n'

    @Generator.gen.register
    def _(self, inst: LabelInst):
        return f'{inst.label}:'
