from cpexp.source_related.c4e.lexer import C4eLexer
from cpexp.source_related.c4e.semantic import C4eSemantic
from cpexp.source_related.source import SourceLanguage

source_language = SourceLanguage('c4e',
                                 lexer=C4eLexer,
                                 semantic=C4eSemantic)
