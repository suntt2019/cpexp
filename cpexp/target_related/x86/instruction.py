from cpexp.generic.label import *
from cpexp.generic.memory import *
from cpexp.ir.generator import TargetInst
from cpexp.target_related.x86.base import bits_to_data_size
from cpexp.target_related.x86.register import Register


def gen_operand(operand: Place | Register | str, redundancy=False):
    if type(operand) in [int, str]:
        print(operand)
        return str(operand)
    elif isinstance(operand, Label):
        return f'L{operand.id}'
    elif isinstance(operand, Register):
        return operand.name
    elif isinstance(operand, Constant):
        return f'{operand.name[1:]}'
    elif isinstance(operand, Place):
        if redundancy:
            specifier = 'q'
        else:
            specifier = f'{bits_to_data_size(operand.type.bits)}'
        if isinstance(operand, Local):
            return f'{specifier}word [rbp{operand.address:+d}]'
        return f'{specifier}word [{operand.name}]'
    raise Exception(f'Unsupported type {operand.__class__} operand {operand}')


class X86(TargetInst):
    NAME = 'UNKNOWN'
    OP_CNT = -1
    REDUNDANCY = False

    def __init__(self, *operands):
        self.operands = list(operands)

    def __str__(self):
        c = len(self.operands)
        if c != self.OP_CNT:  # TODO: this line is written for development, remove this to improve performance
            raise Exception(f'{c} operands ({self.operands}) are not supported for instruction {self.NAME}')
        if c == 0:
            cmd = self.NAME
        else:
            ret = []
            for op in self.operands:
                ret.append(gen_operand(op, redundancy=self.REDUNDANCY))
            cmd = f'{self.NAME.ljust(4)}\t{", ".join(ret)}'
        return f'\t{cmd}\n'


class MOV(X86):
    NAME = 'mov'
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
    REDUNDANCY = True


class POP(X86):
    NAME = 'pop'
    OP_CNT = 1
    REDUNDANCY = True


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
    NAME = 'je'
    OP_CNT = 1


class CDQ(X86):
    NAME = 'cdq'
    OP_CNT = 0
