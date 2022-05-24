from cpexp.ir.memory import Type


class C4eType(Type):
    types = {
        'long': (1, 8),
        'float': (2, 8)
    }
