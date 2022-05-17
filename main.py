from antlr4 import *

import cpexp.antlr.CPExpLexer
import cpexp.antlr.CPExpParser
import cpexp.antlr.CPExpListener
import cpexp.generic.lexer
import cpexp.generic.parser

import cpexp.source_related.exp
import cpexp.source_related.c4e
from cpexp.compile import *
from cpexp.generic.optimizer import *
from cpexp.target_related.tac.generator import TACGenerator
from cpexp.target_related.tacp.generator import TACPGenerator

exp = cpexp.source_related.exp.source_language
c4e = cpexp.source_related.c4e.source_language

# Due to the change of source language, only one compile could be executed at a time
compiles = [
    # LanguageCompiler(exp, TACGenerator).run(FileStream('tests/parser/input/example1.in')),
    LanguageCompiler(c4e, TACPGenerator).run(FileStream('test.c4e')),
]

for c in compiles:
    print(c.compile(merge_labels, rename_labels))
    print(*c.lex_tokens(), sep='\n')
