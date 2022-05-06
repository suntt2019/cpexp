import sys
from antlr4 import *
from cpexp.generated.CPExpLexer import CPExpLexer
from cpexp.generated.CPExpParser import CPExpParser


# if __name__ == '__main__':
#     input = FileStream('hello.txt')
#     lexer = CPExpLexer(input)
#     stream = CommonTokenStream(lexer)
#     parser = CPExpParser(stream)
#     tree = parser.r()
#     print(tree.toStringTree(recog=parser))

from cpexp.build import *

update(verbose=True)

