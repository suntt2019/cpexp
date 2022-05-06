import sys
from antlr4 import *
from src.frontend.HelloLexer import HelloLexer
from src.frontend.HelloParser import HelloParser


if __name__ == '__main__':
    input = FileStream('hello.txt')
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()
    print(tree.toStringTree(recog=parser))
