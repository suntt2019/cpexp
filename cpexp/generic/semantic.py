from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeWalker

import cpexp.antlr.CPExpListener
from cpexp.generic.context import Context
from cpexp.generic.function import Function
from cpexp.generic.label import *
from cpexp.generic.memory import PlaceManager, DataType, Place


class Semantic(cpexp.antlr.CPExpListener.CPExpListener):

    def __init__(self, token_value: list):
        self.token_value = token_value
        self.variable_attributes = {}
        self.labels = []
        self.places = PlaceManager()
        self.functions = {}
        self.context = Context()

    def get_data(self, x):
        if type(x) == TerminalNodeImpl:
            return self.token_value[x.symbol.tokenIndex]
        else:
            self.variable_attributes.setdefault(x, VA())
            return self.variable_attributes.get(x)

    def new_label(self):
        ret = Label(len(self.labels))
        self.labels.append(ret)
        return ret

    def new_temp(self, _type: DataType):
        return self.places.new_temp(_type)

    def new_global(self, name: str, _type: DataType):
        return self.places.add_global(name, _type)

    # TODO: refactor 'new_xxx' into a symbol table (symbol manager)
    def new_function(self, name: str, return_type: DataType):
        if name in self.functions:
            raise Exception(f'Function "{name}" already exists.')
        ret = Function(name, return_type)
        self.functions[name] = ret
        return ret

    def get_function(self, name: str):
        if name not in self.functions:
            raise Exception(f'Undeclared function "{name}".')
        return self.functions[name]

    def convert_type(self, dst_type: DataType, src: Place) -> tuple[Place, list[ConvertInst]]:
        # TODO: check if place is Constant, calculate during compile; maybe do this in an optimizer
        src_type = src.type
        if src_type == dst_type:
            return src, []
        dst = self.new_temp(dst_type)
        code = ConvertInst(src_type, dst_type, src, dst)
        return dst, [code]

    def convert_types(self, *places: Place, type_require: DataType = None):
        dst_type = max(list(map(lambda x: x.type, places)))
        if type_require is not None:
            dst_type = max(dst_type, type_require)
        ret = [dst_type, []]
        for p in places:
            dst, code = self.convert_type(dst_type, p)
            ret[1] += code
            ret.append(dst)
        return ret

    def analyze(self, ast):
        walker = ParseTreeWalker()
        walker.walk(self, ast)
        return self.places.alloc() + self.variable_attributes[ast].code


class VA:
    """VA: Variable Attributes"""

    def __init__(self):
        self.code = None
        self.place = None
        self.begin = None
        self.next = None
        self.true = None
        self.false = None
        self.gen_s_next = False

    def __str__(self):
        return f'(code={self.code}, place={self.place})'


def parameterize_children(func):
    def wrapper(self, ctx):
        args = list(filter(
            lambda x: x != '_',
            map(
                lambda x: self.get_data(x),
                [ctx] + list(ctx.getChildren())
            )
        ))
        func(
            self,
            *args
        )

    return wrapper
