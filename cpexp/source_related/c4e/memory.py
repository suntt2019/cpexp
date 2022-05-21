from cpexp.generic.memory import DataType


class C4eType(DataType):
    types = {
        'int': (1, 64),
        'float': (2, 64)
    }
