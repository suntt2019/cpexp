import os

from antlr4 import *

# Use "import X.Y" instead of "from X import Y" to make reloading available
import cpexp.generated.CPExpParser
import cpexp.generated.CPExpLexer
from cpexp.lexer import *
from cpexp.parser import *


class Compile:
    def __init__(self, input_stream: InputStream):
        self.input_s = input_stream
        self.lexer = CPELexer(self.input_s)
        self.token_s = CommonTokenStream(self.lexer)
        self.parser = cpexp.generated.CPExpParser.CPExpParser(self.token_s)

    def compile(self):
        tree = self.parser.p()
        listener = PrintListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    def lex_only(self):
        self.token_s.fetch(sys.maxsize)

    def get_tokens(self):
        tokens = get_tokens(self.token_s)
        return list(map(self.lexer.format_token, tokens))
