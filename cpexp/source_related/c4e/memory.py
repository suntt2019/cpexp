from cpexp.ir.memory import Type


class C4eType(Type):
    types = {
        'string': (0, 0),
        'int': (1, 4),
        'long': (2, 8),
        'float': (11, 8),
    }
