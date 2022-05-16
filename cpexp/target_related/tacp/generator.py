from cpexp.ir.generator import *


class TACPGenerator(Generator):
    def generate(self, tac: list[Instruction]) -> str:
        return ''.join(map(self.gen, tac))

    @Generator.gen.register
    def _(self, inst: DataInst):
        return f'[{inst.name}({inst.bit}) = {inst.initial}]\n'

    @Generator.gen.register
    def _(self, inst: ConvertInst):
        return f'\t{inst.dst} := {inst.src_type}_to_{inst.dst_type}({inst.src})\n'

    @Generator.gen.register
    def _(self, inst: AssignInst):
        return f'\t{inst.left} := {inst.right}\n'

    @Generator.gen.register
    def _(self, inst: TwoOperandAssignInst):
        return f'\t{inst.target} := {inst.operand1} {inst.OP} {inst.operand2}\n'

    @Generator.gen.register
    def _(self, inst: IfGotoInst):
        return f'\tif {inst.operand1} {inst.op} {inst.operand2} goto {inst.label}\n'

    @Generator.gen.register
    def _(self, inst: GotoInst):
        return f'\tgoto {inst.label}\n'

    @Generator.gen.register
    def _(self, inst: LabelInst):
        return f'{inst.label}:'
