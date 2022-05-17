from __future__ import annotations

from cpexp.ir.instructions import DataInst, ConvertInst


class DataType:
    types = {
        '_': (0, 0),
    }

    def __init__(self, name: str):
        self.name = name
        self._id, self.bits = self.types[name]

    def __str__(self):
        return self.name

    def __lt__(self, other: DataType):
        return self._id < other._id

    def __eq__(self, other: DataType):
        return self._id == other._id


class Place:
    def __init__(self, name: str, _type: DataType, initial: any = None):
        self.name = name
        self.type = _type
        self.initial = initial

    def __repr__(self):
        return self.name

    def alloc(self):
        return DataInst(self.name, self.type.bits, self.initial)


class Constant(Place):
    def __init__(self, _type: DataType, value):
        super().__init__(f'_{value}', _type)

    def __str__(self):
        return self.name[1:]


class PlaceManager:
    def __init__(self):
        self.temp = []
        self.global_ = {}

    def new_temp(self, _type: DataType):
        ret = Place(f't{len(self.temp)}', _type)
        self.temp.append(ret)
        return ret

    def add_global(self, name: str, _type: DataType):
        if name in self.global_:
            raise Exception(f'Global variable "{name}" already exists.')
        ret = Place(name, _type)
        self.global_[name] = ret
        return ret

    def __getitem__(self, name: str):
        # We only support global variable for now
        if name not in self.global_:
            raise Exception(f'Undeclared variable {name}.')
        return self.global_[name]

    def alloc(self):
        ret = list(map(lambda x: x.alloc(), self.temp + list(self.global_.values())))
        return ret
