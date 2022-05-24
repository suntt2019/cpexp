from cpexp.ir.base import Instruction
from cpexp.ir.function import Function
from cpexp.ir.label import Label
from cpexp.ir.memory import *


class SectionStartInst(Instruction):
    def __init__(self, name: str):
        self.name = name  # type: str


class DataInst(Instruction):
    def __init__(self, place: Place):
        self.place = place  # type: Place


class BSSInst(Instruction):
    def __init__(self, place: Place):
        self.place = place  # type: Place


class FunctionStartInst(Instruction):
    def __init__(self, function: Function):
        self.function = function  # type: Function


class FunctionEndInst(Instruction):
    def __init__(self, function: Function):
        self.function = function  # type: Function


class ConvertInst(Instruction):
    # May refactor to subclasses for different types, eg: between integers, itr, rti...
    def __init__(self, src_type, dst_type, src: Place, dst: Place):
        self.src_type = src_type  # TODO: remove these
        self.dst_type = dst_type
        self.src = src  # type: Place
        self.dst = dst  # type: Place


class AssignInst(Instruction):
    def __init__(self, left: Place, right: Place):
        self.left = left  # type: Place
        self.right = right  # type: Place


class ReturnInst(Instruction):
    def __init__(self, value: Place = None):
        self.value = value  # type: Place | None


class CallInst(Instruction):
    def __init__(self, place: Place, func: Function, arguments: list[Place]):
        self.place = place  # type: Place
        self.function = func  # type: Function
        self.arguments = arguments  # type: list[Place]


class TwoOperandAssignInst(Instruction):
    OP = 'UNKNOWN'

    def __init__(self, target: Place, operand1: Place, operand2: Place):
        self.target = target  # type: Place
        self.operand1 = operand1  # type: Place
        self.operand2 = operand2  # type: Place


class AddInst(TwoOperandAssignInst):
    OP = '+'


class SubInst(TwoOperandAssignInst):
    OP = '-'


class MultipleInst(TwoOperandAssignInst):
    OP = '*'


class DivisionInst(TwoOperandAssignInst):
    OP = '/'


class WithLabelInst(Instruction):
    def __init__(self, label: Label):
        self.label = label  # type: Label
        self.label.use(self)

    def set_label(self, label: Label):
        self.label = label


class IfGotoInst(WithLabelInst):
    def __init__(self, operand1: Place, op: str, operand2: Place, label: Label):
        self.operand1 = operand1  # type: Place
        self.operand2 = operand2  # type: Place
        self.op = op  # type: str
        super().__init__(label)


class GotoInst(WithLabelInst):
    def __init__(self, label: Label):
        super().__init__(label)


class LabelInst(WithLabelInst):
    def __init__(self, label: Label):
        super().__init__(label)


class AsmInst(Instruction):
    def __init__(self, code: str):
        self.code = code  # type: str
