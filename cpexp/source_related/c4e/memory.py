from cpexp.ir.memory import Type


class C4eType(Type):
    types = {
        'long': (1, 64),
        'float': (2, 64)
    }
