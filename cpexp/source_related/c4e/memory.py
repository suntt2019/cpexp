from cpexp.generic.memory import DataType


class C4eType(DataType):
    types = {
        'long': (1, 64),
        'float': (2, 64)
    }
