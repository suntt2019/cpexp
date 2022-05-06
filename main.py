import sys
from antlr4 import *

from cpexp.compile import Compile
from cpexp.build import update
from cpexp.generated.CPExpLexer import CPExpLexer
from cpexp.generated.CPExpParser import CPExpParser

from antlr4.Token import CommonToken

update()
c = Compile(FileStream('tests/code-example1.txt'))
c.compile()
c.tokens()

