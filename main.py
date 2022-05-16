from antlr4 import *

from cpexp.compile import *
from cpexp.generic.optimizer import *
from cpexp.source_related.c4e import source_language
from cpexp.target_related.tacp.generator import TACPGenerator

c = LanguageCompiler(source_language, TACPGenerator).run(FileStream('test.c4e'))

print(c.compile(merge_labels, rename_labels))
print(*c.lex_tokens(), sep='\n')
