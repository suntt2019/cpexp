import json
import xml

import yaml
from antlr4 import ParserRuleContext, TokenStream
from antlr4.tree.Tree import ParseTree, TerminalNodeImpl
from loguru import logger

from cpexp.antlr.CPExpParser import CPExpParser
from cpexp.generic.error import CPEErrorListener, MultipleException, MessageException


class ASTViewer:
    def __init__(self, root: ParseTree):
        self.root = root

    def view(self):
        k, v = self.dict(self.root)
        ret = {k: v}
        logger.debug(json.dumps({k: v}, indent=2))

    def dict(self, node):
        if type(node) == TerminalNodeImpl:
            return self.terminal(node)
        elif issubclass(type(node), ParserRuleContext):
            return self.variable(node)
        else:
            raise MessageException(f'Unknown node type {type(node)}')

    def variable(self, var: ParserRuleContext):
        name = var.__class__.__name__[:-len('Context')]
        ret = {}
        for i, c in enumerate(list(var.getChildren())):
            k, v = self.dict(c)
            ret[str(i) + k] = v
        return name, ret

    def terminal(self, term: TerminalNodeImpl):
        token = term.getSymbol()
        return CPExpParser.symbolicNames[token.type], term.getText()


class CPEParser(CPExpParser):
    START = 's'

    def __init__(self, input_s):
        super().__init__(input_s)
        self.source = None
        self.error_listener = CPEErrorListener()
        self.removeErrorListeners()
        self.addErrorListener(self.error_listener)

    def parse(self):
        ret = getattr(self, self.START)()
        errors = self.error_listener.errors
        if len(errors) == 0:
            return ret
        elif len(errors) == 1:
            raise errors[0]
        else:
            raise MultipleException(errors)


def custom_start_parser(start: str):
    class P(CPEParser):
        START = start

    return P
