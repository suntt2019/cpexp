import os

from antlr4 import *

# Use "import X.Y" instead of "from X import Y" to make reloading available
import cpexp.generated.CPExpParser
import cpexp.generated.CPExpLexer
from cpexp.lexer import get_tokens


class Compile:
    def __init__(self, input_stream: InputStream):
        self.input_s = input_stream
        self.lexer = cpexp.generated.CPExpLexer.CPExpLexer(self.input_s)
        self.token_s = CommonTokenStream(self.lexer)
        self.parser = cpexp.generated.CPExpParser.CPExpParser(self.token_s)

    def compile(self):
        self.parser.p()

    def tokens(self):
        get_tokens(self.token_s)
