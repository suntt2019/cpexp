from antlr4 import *

# Use "import X.Y" instead of "from X import Y" to make reloading available
import cpexp.antlr.CPExpParser
import cpexp.antlr.CPExpLexer
from cpexp.source_related.exp.lex import *
from cpexp.generic.semantic import *
from cpexp.source_related.exp.semantic import ExpSemantic


class Compile:
    def __init__(self, input_stream: InputStream):
        self.input_s = input_stream
        self.lexer = CPELexer(self.input_s)
        self.token_s = CommonTokenStream(self.lexer)
        self.parser = cpexp.antlr.CPExpParser.CPExpParser(self.token_s)
        self.ast = None
        self.semantic_analyzer = ExpSemantic(self.lexer.token_values)
        self.tac = None

    def lex_only(self):
        self.token_s.fetch(sys.maxsize)

    def parse(self):
        self.ast = self.parser.p()

    def semantic(self):
        self.semantic_analyzer.analyze(self.ast)
        self.tac = self.semantic_analyzer.variable_attributes[self.ast].code

    def optimize(self, optimizer):
        self.tac = optimizer(self.tac)

    def get_tokens(self):
        return list(map(self.lexer.format_token, get_tokens(self.token_s)))

    # tac(3ac): three address code
    def get_tac(self):
        return self.tac
