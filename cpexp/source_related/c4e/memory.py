from cpexp.generic.memory import DataType


class C4eType(DataType):
    types = {
        'int': (1, 32),
        'long': (2, 64),
        'float': (11, 64)
    }
