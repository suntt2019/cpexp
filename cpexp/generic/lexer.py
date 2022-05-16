import sys
from typing.io import TextIO

from antlr4 import CommonTokenStream
from antlr4.Token import CommonToken
import cpexp.antlr.CPExpLexer


def get_tokens(s: CommonTokenStream) -> list[CommonToken]:
    return s.getTokens(0, sys.maxsize)


class CPELexer(cpexp.antlr.CPExpLexer.CPExpLexer):
    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.token_values = []

    def nextToken(self):
        token = super().nextToken()
        self.token_values.append(self.token_value(token))
        return token

    def get_token_values(self) -> list[any]:
        return self.token_values

    # Overwrite this function to calculate token value
    def token_value(self, token: CommonToken) -> any:
        return token.text

    # Overwrite this function to convert token to string
    def format_token(self, token: CommonToken) -> str:
        return f'<token "{token.text}" {self.token_values[token.tokenIndex]}>'
