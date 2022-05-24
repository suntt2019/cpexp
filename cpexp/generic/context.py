from __future__ import annotations

import math

from cpexp.generic.function import Function
from cpexp.generic.memory import DataType, Local


class Context:
    def __init__(self, outer: Context = None, func: Function = None):
        self.outer = outer
        self._function = func
        self.locals = {}
        if func is not None:
            for param in func.param_list:
                self.add_local_variable(param)

    def enter(self, func=None):
        inner = Context(self, func)
        return inner

    def exit(self):
        return self.outer

    @property
    def function(self):
        if self._function is None:
            if self.outer is None:
                return None
            else:
                return self.outer.function
        else:
            return self._function

    def add_local(self, name: str, _type: DataType, initial=None):
        address = -self.function.use_memory(math.ceil(_type.bits / 8))
        local = Local(name, _type, address, initial)
        return self.add_local_variable(local)

    def add_local_variable(self, local: Local):
        if local.name in self.locals:
            raise Exception(f'Local variable {local.name} already exists.')
        self.locals[local.name] = local
        return local

    def __getitem__(self, name: str):
        if name not in self.locals:
            if self.outer is None:
                return None
            else:
                return self.outer[name]
        else:
            return self.locals[name]
