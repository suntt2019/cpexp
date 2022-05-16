from antlr4 import *

from cpexp.compile import Compile
from cpexp.antlr.build import update
from cpexp.generic.optimizer import *
from cpexp.target_related.tac.generator import TACGenerator

update('exp')
c = Compile(FileStream('tests/parser/input/example1.in'))
c.parse()
c.semantic()
c.optimize(merge_labels, rename_labels)
c.generate()
print(c.result)
# c.lex_only()
# print(*c.get_tokens(), sep='\n')
