class Instruction:
    def __str__(self):
        pass

    def __repr__(self):
        return str(self)


class AssignInst(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} := {self.right}'


class TwoOperandAssignInst(Instruction):
    OP = 'UNKNOWN'

    def __init__(self, target, operand1, operand2):
        self.target = target
        self.operand1 = operand1
        self.operand2 = operand2

    def __str__(self):
        return f'{self.target}:={self.operand1}{self.OP}{self.operand2}'


class AddInst(TwoOperandAssignInst):
    OP = '+'


class SubInst(TwoOperandAssignInst):
    OP = '-'


class MultipleInst(TwoOperandAssignInst):
    OP = '*'


class DivisionInst(TwoOperandAssignInst):
    OP = '/'


class WithLabelInst(Instruction):
    def __init__(self, label):
        self.label = label
        self.label.use(self)

    def set_label(self, label):
        self.label = label


class IfGotoInst(WithLabelInst):
    def __init__(self, operand1, op, operand2, label):
        self.operand1 = operand1
        self.operand2 = operand2
        self.op = op
        super().__init__(label)

    def __str__(self):
        return f'if {self.operand1} {self.op} {self.operand2} goto {self.label}'


class GotoInst(WithLabelInst):
    def __init__(self, label):
        super().__init__(label)

    def __str__(self):
        return f'goto {self.label}'


class LabelInst(WithLabelInst):
    def __init__(self, label):
        super().__init__(label)

    def __str__(self):
        return f'{self.label}:'
