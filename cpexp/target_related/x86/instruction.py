from cpexp.generic.memory import Place, Constant
from cpexp.ir.generator import TargetInst


def specify_size(operand: Place | str):
    if isinstance(operand, Place) and not isinstance(operand, Constant):
        # TODO: choose size specifier by operand.type.bits
        return f'qword {operand}'
    return operand


class X86(TargetInst):
    NAME = 'UNKNOWN'
    OP_CNT = -1

    def __init__(self, *operands: str):
        self.operands = list(operands)

    def __str__(self):
        c = len(self.operands)
        if c != self.OP_CNT:  # TODO: for development, remove this to improve performance
            raise Exception(f'{c} operands ({self.operands}) are not supported for instruction {self.NAME}')
        if c == 0:
            cmd = self.NAME
        else:
            cmd = f'{self.NAME.ljust(4)}\t{", ".join(map(str, self.operands))}'
        return f'\t{cmd}\n'


class SpecifyFirstOperand(X86):
    def __str__(self):
        self.operands[0] = specify_size(self.operands[0])
        return super().__str__()


class MOV(X86):
    NAME = 'mov'
    OP_CNT = 2


class ADD(X86):
    NAME = 'add'
    OP_CNT = 2


class SUB(X86):
    NAME = 'sub'
    OP_CNT = 2


class IMUL(SpecifyFirstOperand):
    NAME = 'imul'
    OP_CNT = 1


class IDIV(SpecifyFirstOperand):
    NAME = 'idiv'
    OP_CNT = 1


class XOR(X86):
    NAME = 'xor'
    OP_CNT = 2


class PUSH(SpecifyFirstOperand):
    NAME = 'push'
    OP_CNT = 1


class POP(X86):
    NAME = 'pop'
    OP_CNT = 1


class CALL(X86):
    NAME = 'call'
    OP_CNT = 1

    def __str__(self):
        self.operands[0] = f'_{str(self.operands[0])}'
        return super().__str__()


class RET(X86):
    NAME = 'ret'
    OP_CNT = 0


class JMP(X86):
    NAME = 'jmp'
    OP_CNT = 1


class CMP(X86):
    NAME = 'cmp'
    OP_CNT = 2


class JG(X86):
    NAME = 'jg'
    OP_CNT = 1


class JL(X86):
    NAME = 'jl'
    OP_CNT = 1


class JE(X86):
    NAME = 'jE'
    OP_CNT = 1
