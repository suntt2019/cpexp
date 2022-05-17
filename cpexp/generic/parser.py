import json
import xml

import yaml
from antlr4 import ParserRuleContext, TokenStream
from antlr4.tree.Tree import ParseTree, TerminalNodeImpl

import cpexp.antlr.CPExpParser


class ASTViewer:
    def __init__(self, root: ParseTree):
        self.root = root

    def view(self):
        k, v = self.dict(self.root)
        ret = {k: v}
        print(json.dumps({k: v}, indent=2))

    def dict(self, node):
        if type(node) == TerminalNodeImpl:
            return self.terminal(node)
        elif issubclass(type(node), ParserRuleContext):
            return self.variable(node)
        else:
            raise Exception(f'Unknown node type {type(node)}')

    def variable(self, var: ParserRuleContext):
        name = var.__class__.__name__[:-len('Context')]
        ret = {}
        for i, c in enumerate(list(var.getChildren())):
            k, v = self.dict(c)
            ret[str(i) + k] = v
        return name, ret

    def terminal(self, term: TerminalNodeImpl):
        token = term.getSymbol()
        return cpexp.antlr.CPExpParser.CPExpParser.symbolicNames[token.type], term.getText()


class CPEParser(cpexp.antlr.CPExpParser.CPExpParser):
    START = 's'

    def parse(self):
        return getattr(self, self.START)()


def custom_start_parser(start: str):
    class P(CPEParser):
        START = start

    return P
