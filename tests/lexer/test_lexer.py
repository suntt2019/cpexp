import os.path

from cpexp.antlr.build import update
from cpexp.compile import *
from tests.base import *

directory = os.path.join(test_dir, 'lexer')


import unittest


class TestLexer(unittest.TestCase):
    def test_overall(self):
        update('exp')
        for filename in os.listdir(os.path.join(directory, 'input')):
            name, _, extension = filename.rpartition('.')
            with self.subTest(name=name):
                c = Compile(FileStream(os.path.join(directory, 'input', filename)))
                c.lex()
                with open(os.path.join(directory, 'output', f'{name}.ans')) as f:
                    expected = f.read()
                actual = '\n'.join(c.get_tokens())
                self.assertEqual(actual, expected)
