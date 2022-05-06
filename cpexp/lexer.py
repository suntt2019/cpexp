import os.path
import sys

from antlr4 import CommonTokenStream

from cpexp.base import working_dir

token_dict = {}


def parse_token_dict():
    if len(token_dict) > 0:
        return
    with open(os.path.join(working_dir, 'generated', 'CPExp.tokens')) as f:
        line = f.readline()
        while line != '':
            data = line.rpartition('=')
            k = int(data[2])
            token_dict[k] = data[0]
            line = f.readline()


def get_tokens(s: CommonTokenStream):
    parse_token_dict()
    for t in s.getTokens(0, sys.maxsize):
        print(token_dict[t.type], t.text)
