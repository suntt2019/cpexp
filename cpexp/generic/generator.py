from __future__ import annotations
from functools import singledispatch, update_wrapper

from cpexp.ir.instruction import *


# Awesome decorator from stackoverflow.
# URL: https://stackoverflow.com/questions/24601722/how-can-i-use-functools-singledispatch-with-instance-methods
def meth_dispatch(func):
    dispatcher = singledispatch(func)

    def wrapper(*args, **kw):
        return dispatcher.dispatch(args[1].__class__)(*args, **kw)

    wrapper.register = dispatcher.register
    update_wrapper(wrapper, func)
    return wrapper


class Register:
    NAME = 'UNKNOWN_REGISTER'

    def __init__(self, size: int | None = None):
        if not hasattr(self, 'name'):
            self.name = self.NAME

    def gen(self) -> str:
        return self.name


class TargetInstruction:
    NAME = 'UNKNOWN_TARGET_INSTRUCTION'
    OP_CNT = -1

    def __init__(self, *operands: InstructionContent | Register):
        self.operands = operands

    def gen(self, operands: list[str]) -> str:
        raise Exception(f'Type {self.__class__} target instruction {self} without gen() function')


class Generator:
    def generate(self, ir: list[Instruction]) -> any:
        return self.tr_to_str(sum(map(self.gen, ir)))

    @meth_dispatch
    def gen(self, x: Instruction | InstructionContent):
        raise Exception(f'Unable to generate from non-instruction type {x.__class__.__name__}')

    @gen.register
    def _(self, inst: Instruction) -> list[TargetInstruction]:
        raise Exception(f'Unable to generate from type {inst.__class__.__name__} instruction {inst}')

    @gen.register
    def _(self, content: InstructionContent) -> list[str]:
        raise Exception(f'Unable to generate from type {content.__class__.__name__} instruction content {content}')

    def tr_to_str(self, tr: list[TargetInstruction]):
        ret = ''
        for r in tr:
            operands = []
            for o in r.operands:
                if isinstance(o, Register):
                    operands.append(o.gen())
                elif isinstance(o, InstructionContent):
                    operands.append(self.gen(o))
                else:
                    raise Exception(f'Unexpected operand {o} which is neither a register nor a instruction content')
            ret += r.gen(operands)
        return ret
