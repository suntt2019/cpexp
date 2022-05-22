import os.path

from cpexp.base import working_dir
from cpexp.compile import *
from cpexp.external.assemble import assemble
from cpexp.external.run import run
from cpexp.generic.optimizer import *
from cpexp.target_related.tac.generator import TACGenerator
from cpexp.target_related.tacp.generator import TACPGenerator
from cpexp.target_related.x86.generator import X86Generator

from cpexp.source_related.exp import source_language as exp
from cpexp.source_related.c4e import source_language as c4e

# Due to the change of source language, only one compile could be executed at a time
compiles = [
    # LanguageCompiler(exp, TACGenerator).run(FileStream('tests/parser/input/example1.in')),
    # LanguageCompiler(c4e, TACPGenerator).run(FileStream('test.c4e')),
    LanguageCompiler(c4e, X86Generator).run(FileStream('test.c4e')),
]
v = 1
c = compiles[0]
# print('\n'.join(c.lex_tokens()))
code = c.compile(merge_labels, rename_labels, verbose=v)
print(code)
# input()
assemble(code, clean=False, verbose=v, directory=os.path.join(working_dir, '..', 'assembly'))
run(verbose=v)
