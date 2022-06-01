from __future__ import annotations

import math

from cpexp.generic.error import MessageException
from cpexp.ir.function import Function
from cpexp.ir.memory import Type, Local


class Context:
    def __init__(self, outer: Context = None, func: Function = None):
        self.outer = outer
        self._function = func
        self.locals = {}
        if func is not None:
            for local in func.param_list:
                self.add_local(local)

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

    def add_local(self, local: Local):
        if local.name in self.locals:
            raise MessageException(f'Local variable {local.name} already exists.')
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
