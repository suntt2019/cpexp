from cpexp.generic.memory import DataType


class C4eType(DataType):
    types = {
        'int': (1, 32),
        'float': (2, 64)  # TODO: change to 32 after development
    }
