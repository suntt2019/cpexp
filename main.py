import sys
from antlr4 import *

from cpexp.compile import Compile
from cpexp.build import update

from antlr4.Token import CommonToken

update()
c = Compile(FileStream('tests/parser/input/example1.in'))
# c.lex_only()
c.parse()
c.semantic()
print(*c.get_tac(), sep='\n')
# print(*c.get_tokens(), sep='\n')
