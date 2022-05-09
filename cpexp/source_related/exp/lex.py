import os.path
import sys
from typing.io import TextIO

from antlr4 import CommonTokenStream
from antlr4.Token import CommonToken, Token
import cpexp.antlr.CPExpLexer

from cpexp.base import *


class CPELexer(cpexp.antlr.CPExpLexer.CPExpLexer):
    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.token_values = []

    def nextToken(self):
        token = super().nextToken()
        self.token_values.append(self.token_value(token))
        return token

    def token_value(self, token: CommonToken) -> any:
        txt = token.text
        ret = txt
        type_id = token.type
        type_name = self.symbolicNames[type_id]
        if type_id < len(self.literalNames):
            ret = '_'
        elif type_name.startswith('INT'):
            base = int(type_name[3:])
            ret = int(txt, base)
        elif type_name.startswith('REAL'):
            base = int(type_name[4:])
            prefix_digit = len({
                                   8: '0',
                                   10: '',
                                   16: '0x'
                               }[base])
            integral, dec = txt[prefix_digit:].split('.')
            a = int(integral + dec, base)
            ret = a / (base ** len(dec))
        return ret

    def format_token(self, token: CommonToken) -> str:
        type_id = token.type
        if type_id < len(self.literalNames):
            type_name = self.literalNames[type_id][1:-1]
        else:
            type_name = self.symbolicNames[type_id]
        return f'{type_name}\t{self.token_values[token.tokenIndex]}'


def get_tokens(s: CommonTokenStream) -> list[CommonToken]:
    return s.getTokens(0, sys.maxsize)
