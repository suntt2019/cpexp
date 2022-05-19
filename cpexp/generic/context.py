from __future__ import annotations
from cpexp.generic.function import Function
from cpexp.generic.memory import DataType, Local


class Context:
    def __init__(self, outer: Context = None, func: Function = None):
        self.outer = outer
        self._function = func
        self.locals = {}
        if func is not None:
            address = 0
            for _type, _id in func.param_list:
                address += _type.bits
                self.add_local_variable(_id, _type, address)

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

    def add_local(self, name: str, _type: DataType):
        address = -self.function.use_memory(_type.bits)
        return self.add_local_variable(name, _type, address)

    def add_local_variable(self, name: str, _type: DataType, address: int):
        if name in self.locals:
            raise Exception(f'Local variable {name} already exists.')
        local = Local(name, _type, address)
        self.locals[name] = local
        return local

    def __getitem__(self, name: str):
        if name not in self.locals:
            if self.outer is None:
                return None
            else:
                return self.outer[name]
        else:
            return self.locals[name]
