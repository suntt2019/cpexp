class Instruction:
    pass


class DataInst(Instruction):
    def __init__(self, name: str, bits: int, initial: any):
        self.name = name
        self.bit = bits
        self.initial = initial


class FunctionStartInst(Instruction):
    def __init__(self, function):
        self.function = function


class FunctionEndInst(Instruction):
    def __init__(self, function):
        self.function = function


class ConvertInst(Instruction):
    # May refactor to subclasses for different types, eg: between integers, itr, rti...
    def __init__(self, src_type, dst_type, src, dst):
        self.src_type = src_type
        self.dst_type = dst_type
        self.src = src
        self.dst = dst


class AssignInst(Instruction):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ReturnInst(Instruction):
    def __init__(self, value):
        self.value = value


class CallInst(Instruction):
    def __init__(self, place, function):
        self.place = place
        self.function = function


class TwoOperandAssignInst(Instruction):
    OP = 'UNKNOWN'

    def __init__(self, target, operand1, operand2):
        self.target = target
        self.operand1 = operand1
        self.operand2 = operand2


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


class GotoInst(WithLabelInst):
    def __init__(self, label):
        super().__init__(label)


class LabelInst(WithLabelInst):
    def __init__(self, label):
        super().__init__(label)
