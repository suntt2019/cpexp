from cpexp.ir.memory import Type


class C4eType(Type):
    types = {
        'string': (0, 0),
        'long': (1, 8),
        'float': (2, 8),
    }
