from cpexp.generic.lexer import CPELexer
from cpexp.generic.parser import CPEParser
from cpexp.generic.semantic import Semantic


class SourceLanguage:
    def __init__(self, name: str,
                 lexer=CPELexer,
                 parser=CPEParser,
                 semantic=Semantic):
        self.name = name
        self.lexer = lexer
        self.parser = parser
        self.semantic = semantic
