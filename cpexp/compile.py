import sys

from antlr4 import *
from loguru import logger

from cpexp.antlr.build import update
from cpexp.generic.error import try_compile
from cpexp.generic.lexer import get_tokens, CPELexer
from cpexp.generic.parser import CPEParser
from cpexp.generic.generator import Generator
from cpexp.generic.semantic import *
from cpexp.source_related.source import SourceLanguage


class Compiler:
    def __init__(self,
                 lexer=CPELexer,
                 parser=CPEParser,
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
                 parser=CPEParser,
                 semantic=Semantic,
                 generator=Generator):
        self.input_s = input_stream
        self.source = self.input_s.getText(0, self.input_s.size).split('\n')
        self.lexer = lexer(self.input_s)
        self.token_s = CommonTokenStream(self.lexer)
        self.parser = parser(self.token_s)
        self.ast = None
        self.semantic_analyzer = semantic(self.lexer.get_token_values())
        self.ir = None
        self.generator = generator()
        self.result = None

    def compile(self, *optimizers, verbose=0):
        if verbose > 0:
            logger.debug('Compiling...')
        if verbose > 1:
            logger.debug('    Parsing(with lexing on the fly)...')
        self.parse()
        if verbose > 1:
            logger.debug('    Semantic analyzing...')
        self.semantic()
        if verbose > 1:
            logger.debug('    General optimizing...')
        self.optimize(*optimizers)
        if verbose > 1:
            logger.debug('    Generating...')
        self.generate()
        if verbose > 0:
            logger.debug('Compile finished.')
        return self.result

    def lex_tokens(self):
        self.lex()
        return self.get_tokens()

    @try_compile
    def lex(self):
        self.token_s.fetch(sys.maxsize)

    @try_compile
    def parse(self):
        self.parser.source = self.source
        self.ast = self.parser.parse()

    @try_compile
    def semantic(self):
        self.semantic_analyzer.source = self.source
        self.ir = self.semantic_analyzer.analyze(self.ast)

    @try_compile
    def optimize(self, *optimizers):
        for func in optimizers:
            self.ir = func(self.ir)

    @try_compile
    def generate(self):
        self.result = self.generator.generate(self.ir)

    def get_tokens(self):
        return list(map(self.lexer.format_token, get_tokens(self.token_s)))

    # tac(3ac): three address code
    def get_ir(self):
        return self.ir

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
                 parser=CPEParser,
                 semantic=Semantic,
                 generator=Generator):
        self.source_name = source_name
        super().__init__(input_stream,
                         lexer=lexer,
                         parser=parser,
                         semantic=semantic,
                         generator=generator)

    def lex(self):
        update(self.source_name)
        super().lex()

    def parse(self):
        update(self.source_name)
        super().parse()
