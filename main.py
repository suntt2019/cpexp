import sys
from antlr4 import *
from src.frontend.CPExpLexer import CPExpLexer
from src.frontend.CPExpParser import CPExpParser


if __name__ == '__main__':
    input = FileStream('hello.txt')
    lexer = CPExpLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CPExpParser(stream)
    tree = parser.r()
    print(tree.toStringTree(recog=parser))
