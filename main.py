from antlr4 import *

from cpexp.compile import Compile
from cpexp.antlr.build import update
from cpexp.generic.optimizer import merge_labels

update()
c = Compile(FileStream('tests/parser/input/example1.in'))
# c.lex_only()
c.parse()
c.semantic()
c.optimize(merge_labels)
print(*c.get_tac(), sep='\n')
# print(*c.get_tokens(), sep='\n')
