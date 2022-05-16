from cpexp.source_related.exp.lexer import ExpLexer
from cpexp.source_related.exp.semantic import ExpSemantic
from cpexp.source_related.source import SourceLanguage

source_language = SourceLanguage('exp',
                                 lexer=ExpLexer,
                                 semantic=ExpSemantic)
