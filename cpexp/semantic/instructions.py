class Instruction:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string


class AddInst(Instruction):
    def __init__(self, target, addend1, addend2):
        super().__init__(f'{target}:={addend1}+{addend2}')


class SubInst(Instruction):
    def __init__(self, target, minuend, subtraction):
        super().__init__(f'{target}:={minuend}-{subtraction}')


class MultipleInst(Instruction):
    def __init__(self, target, multiplier1, multiplier2):
        super().__init__(f'{target}:={multiplier1}*{multiplier2}')


class DivisionInst(Instruction):
    def __init__(self, target, dividend, divisor):
        super().__init__(f'{target}:={dividend}/{divisor}')


class IfGotoInst(Instruction):
    def __init__(self, operand1, op, operand2, label):
        super().__init__(f'if {operand1} {op} {operand2} goto {label}')


class GotoInst(Instruction):
    def __init__(self, label):
        super().__init__(f'goto {label}')


class LabelInst(Instruction):
    def __init__(self, label):
        super().__init__(f'{label}:')


class AssignInst(Instruction):
    def __init__(self, left, right):
        super().__init__(f'{left} := {right}')
