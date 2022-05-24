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


class Generator:
    def generate(self, tac: list[Instruction]) -> any:
        return list(map(self.gen, tac))

    @meth_dispatch
    def gen(self, inst):
        raise Exception(f'Unable to generate from non-instruction type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: Instruction):
        raise Exception(f'Unable to generate from type {inst.__class__.__name__} instructions')


class TargetInst:  # Target Instruction
    pass
