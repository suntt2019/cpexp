from __future__ import annotations

from cpexp.ir.instructions import *


class DataType:
    types = {
        '_': (0, 0),
    }

    def __init__(self, name: str):
        self.name = name
        self._id, self.bits = self.types[name]
        # TODO: For more complex type system, use POSet instead of id

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __lt__(self, other: DataType):
        return self._id < other._id

    def __eq__(self, other: DataType):
        return self._id == other._id


class Place:
    def __init__(self, name: str, _type: DataType | None, initial: any = None):
        self.name = name
        self._type = _type
        self.initial = initial

    @property
    def type(self):
        return self._type

    def __repr__(self):
        return f'[{self.name}]'


class VoidPlace(Place):
    def __init__(self):
        super().__init__('VOID_PLACE', None)

    @property
    def type(self):
        # TODO: This assumes any access to the places need to get its type first
        raise Exception("Void value not ignored as it should be")


class Constant(Place):
    def __init__(self, _type: DataType, value):
        super().__init__(f'_{value}', _type)

    def __str__(self):
        return self.name[1:]


class Local(Place):
    def __init__(self, name: str, _type: DataType, address, initial=None):
        self.address = address
        super().__init__(name, _type, initial)

    def __str__(self):
        return f'[rbp+{self.address}]'


class PlaceManager:
    def __init__(self):
        self.temp = []
        self.global_ = {}

    def new_temp(self, _type: DataType):
        ret = Place(f't{len(self.temp)}', _type)
        self.temp.append(ret)
        return ret

    def add_global(self, name: str, _type: DataType, initial=None):
        if name in self.global_:
            raise Exception(f'Global variable "{name}" already exists.')
        ret = Place(name, _type, initial)
        self.global_[name] = ret
        return ret

    def __getitem__(self, name: str):
        # We only support global variable for now
        if name not in self.global_:
            return None
        else:
            return self.global_[name]

    def alloc(self):
        data_section = [SectionStartInst('data')]
        bss_section = [SectionStartInst('bss')]
        for var in self.temp + list(self.global_.values()):
            if var.initial is None:
                bss_section.append(BSSInst(var))
            else:
                # TODO: try to calculate initial expression during compile
                if isinstance(var.initial, Constant):
                    data_section.append(DataInst(var))
                else:
                    bss_section.append(BSSInst(var))
        return data_section + bss_section
