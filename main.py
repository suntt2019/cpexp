import sys
from antlr4 import *

from cpexp.compile import Compile
from cpexp.build import update

from antlr4.Token import CommonToken

update()
c = Compile(FileStream('tests/tokens-example.txt'))
c.lex_only()
# c.compile()
print(*c.get_tokens(), sep='\n')

