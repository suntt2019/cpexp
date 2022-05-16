from antlr4 import *

from cpexp.compile import *
from cpexp.generic.optimizer import *
from cpexp.source_related.exp import source_language
from cpexp.target_related.tac.generator import TACGenerator

c = LanguageCompiler(source_language, TACGenerator).run(FileStream('tests/parser/input/example1.in'))

print(c.compile(merge_labels, rename_labels))
print(*c.lex_tokens(), sep='\n')
