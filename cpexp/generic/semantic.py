from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeWalker

import cpexp.antlr.CPExpListener
from cpexp.generic.label import *


class Semantic(cpexp.antlr.CPExpListener.CPExpListener):

    def __init__(self, token_value: list):
        self.token_value = token_value
        self.variable_attributes = {}
        self.labels = []

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

    def analyze(self, ast):
        walker = ParseTreeWalker()
        walker.walk(self, ast)
        return self.variable_attributes[ast].code


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
        func(
            self,
            *filter(
                lambda x: x != '_',
                map(
                    lambda x: self.get_data(x),
                    [ctx] + list(ctx.getChildren())
                )
            )
        )

    return wrapper
