import sys

from antlr4 import *

# Use "import X.Y" instead of "from X import Y" to make reloading available
import cpexp.antlr.CPExpParser
from cpexp.antlr.build import update
from cpexp.generic.lexer import get_tokens, CPELexer
from cpexp.ir.generator import Generator
from cpexp.generic.semantic import *
from cpexp.source_related.source import SourceLanguage


class Compiler:
    def __init__(self,
                 lexer=CPELexer,
                 parser=cpexp.antlr.CPExpParser.CPExpParser,
                 semantic=Semantic,
                 generator=Generator):
        self.lexer = lexer
        self.parser = parser
        self.semantic = semantic
        self.generator = generator

    def run(self, input_stream: InputStream):
        return Compile(input_stream, self.lexer, self.parser, self.semantic, self.generator)


class Compile:
    def __init__(self, input_stream: InputStream,
                 lexer=CPELexer,
                 parser=cpexp.antlr.CPExpParser.CPExpParser,
                 semantic=Semantic,
                 generator=Generator):
        self.input_s = input_stream
        self.lexer = lexer(self.input_s)
        self.token_s = CommonTokenStream(self.lexer)
        self.parser = parser(self.token_s)
        self.ast = None
        self.semantic_analyzer = semantic(self.lexer.get_token_values())
        self.tac = None
        self.generator = generator()
        self.result = None

    def compile(self, *optimizers):
        self.parse()
        self.semantic()
        self.optimize(*optimizers)
        self.generate()
        return self.result

    def lex_tokens(self):
        self.lex_only()
        return self.get_tokens()

    def lex_only(self):
        self.token_s.fetch(sys.maxsize)

    def parse(self):
        # TODO: refactor parser
        self.ast = self.parser.b()

    def semantic(self):
        self.semantic_analyzer.analyze(self.ast)
        self.tac = self.semantic_analyzer.variable_attributes[self.ast].code

    def optimize(self, *optimizers):
        for func in optimizers:
            self.tac = func(self.tac)

    def generate(self):
        self.result = self.generator.generate(self.tac)

    def get_tokens(self):
        return list(map(self.lexer.format_token, get_tokens(self.token_s)))

    # tac(3ac): three address code
    def get_tac(self):
        return self.tac

    def get_result(self):
        return self.result


class LanguageCompiler(Compiler):
    def __init__(self, source: SourceLanguage, generator=Generator):
        self.source_name = source.name
        super().__init__(lexer=source.lexer, parser=source.parser, semantic=source.semantic, generator=generator)

    def run(self, input_stream: InputStream):
        return CompileWithLanguage(input_stream, self.source_name,
                                   lexer=self.lexer,
                                   parser=self.parser,
                                   semantic=self.semantic,
                                   generator=self.generator)


class CompileWithLanguage(Compile):
    def __init__(self, input_stream: InputStream, source_name: str,
                 lexer=CPELexer,
                 parser=cpexp.antlr.CPExpParser.CPExpParser,
                 semantic=Semantic,
                 generator=Generator):
        self.source_name = source_name
        super().__init__(input_stream,
                         lexer=lexer,
                         parser=parser,
                         semantic=semantic,
                         generator=generator)

    def lex_only(self):
        update(self.source_name)
        super().lex_only()

    def parse(self):
        update(self.source_name)
        super().parse()
