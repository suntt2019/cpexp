from cpexp.ir.memory import Type


class C4eType(Type):
    types = {
        'string': (0, 0),
        'bool': (1, 1),
        'char': (2, 1),
        'short': (3, 2),
        'int': (4, 4),
        'long': (5, 8),
        'float': (11, 8),
    }
