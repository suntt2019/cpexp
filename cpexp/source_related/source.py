import cpexp.antlr.CPExpParser
from cpexp.generic.lexer import CPELexer
from cpexp.generic.semantic import Semantic


class SourceLanguage:
    def __init__(self, name: str,
                 lexer=CPELexer,
                 parser=cpexp.antlr.CPExpParser.CPExpParser,
                 semantic=Semantic):
        self.name = name
        self.lexer = lexer
        self.parser = parser
        self.semantic = semantic
