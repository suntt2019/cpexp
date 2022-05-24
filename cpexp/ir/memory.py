from __future__ import annotations

from cpexp.ir.base import InstructionContent


class Type(InstructionContent):
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

    def __lt__(self, other: Type):
        return self._id < other._id

    def __eq__(self, other: Type):
        return self._id == other._id


class Place(InstructionContent):
    def __init__(self, name: str, _type: Type | None, initial: any = None):
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
    def __init__(self, _type: Type, value):
        super().__init__(f'_{value}', _type)

    def __str__(self):
        return self.name[1:]


class Local(Place):
    def __init__(self, name: str, _type: Type, address, initial=None):
        self.address = address
        super().__init__(name, _type, initial)

    def __str__(self):
        return f'[rbp+{self.address}]'


