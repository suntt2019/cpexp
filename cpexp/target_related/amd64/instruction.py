from cpexp.generic.error import MessageException
from cpexp.ir.label import *
from cpexp.ir.memory import *
from cpexp.generic.generator import TargetInstruction


class AMD64(TargetInstruction):

    def gen(self, operands: list[str]) -> str:
        c = len(operands)
        if c != self.OP_CNT:  # TODO: this line is written for development, remove this to improve performance
            raise MessageException(f'{c} operands ({operands}) are not supported for instruction {self.NAME}')
        if c == 0:
            cmd = self.NAME
        else:
            cmd = f'{self.NAME.ljust(4)}\t{", ".join(operands)}'
        return f'\t{cmd}\n'


class MOV(AMD64):
    NAME = 'mov'
    OP_CNT = 2


class MOVSX(AMD64):
    NAME = 'movsx'
    OP_CNT = 2


class ADD(AMD64):
    NAME = 'add'
    OP_CNT = 2


class SUB(AMD64):
    NAME = 'sub'
    OP_CNT = 2


class IMUL(AMD64):
    NAME = 'imul'
    OP_CNT = 1


class IDIV(AMD64):
    NAME = 'idiv'
    OP_CNT = 1


class XOR(AMD64):
    NAME = 'xor'
    OP_CNT = 2


class PUSH(AMD64):
    NAME = 'push'
    OP_CNT = 1


class POP(AMD64):
    NAME = 'pop'
    OP_CNT = 1


class CALL(AMD64):
    NAME = 'call'
    OP_CNT = 1


class RET(AMD64):
    NAME = 'ret'
    OP_CNT = 0


class JMP(AMD64):
    NAME = 'jmp'
    OP_CNT = 1


class CMP(AMD64):
    NAME = 'cmp'
    OP_CNT = 2


class JG(AMD64):
    NAME = 'jg'
    OP_CNT = 1


class JL(AMD64):
    NAME = 'jl'
    OP_CNT = 1


class JE(AMD64):
    NAME = 'je'
    OP_CNT = 1


class LAHF(AMD64):
    NAME = 'lahf'
    OP_CNT = 0


class SHR(AMD64):
    NAME = 'shr'
    OP_CNT = 2


class AND(AMD64):
    NAME = 'and'
    OP_CNT = 2


class NOT(AMD64):
    NAME = 'not'
    OP_CNT = 1


class _TEXT(AMD64):
    def __init__(self, text: str):
        self.text = text
        super().__init__()

    def gen(self, operands: list[str]) -> str:
        return self.text
