from cpexp.ir.label import *
from cpexp.ir.memory import *
from cpexp.generic.generator import TargetInstruction


class X86(TargetInstruction):

    def gen(self, operands: list[str]) -> str:
        c = len(operands)
        if c != self.OP_CNT:  # TODO: this line is written for development, remove this to improve performance
            raise Exception(f'{c} operands ({operands}) are not supported for instruction {self.NAME}')
        if c == 0:
            cmd = self.NAME
        else:
            cmd = f'{self.NAME.ljust(4)}\t{", ".join(operands)}'
        return f'\t{cmd}\n'


class MOV(X86):
    NAME = 'mov'
    OP_CNT = 2


class MOVSX(X86):
    NAME = 'movsx'
    OP_CNT = 2


class ADD(X86):
    NAME = 'add'
    OP_CNT = 2


class SUB(X86):
    NAME = 'sub'
    OP_CNT = 2


class IMUL(X86):
    NAME = 'imul'
    OP_CNT = 1


class IDIV(X86):
    NAME = 'idiv'
    OP_CNT = 1


class XOR(X86):
    NAME = 'xor'
    OP_CNT = 2


class PUSH(X86):
    NAME = 'push'
    OP_CNT = 1


class POP(X86):
    NAME = 'pop'
    OP_CNT = 1


class CALL(X86):
    NAME = 'call'
    OP_CNT = 1


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


class _TEXT(X86):
    def __init__(self, text: str):
        self.text = text
        super().__init__()

    def gen(self, operands: list[str]) -> str:
        return self.text
