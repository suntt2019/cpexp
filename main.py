import argparse
import os.path

from loguru import logger

from cpexp.compile import *
from cpexp.external.assemble import assemble
from cpexp.external.run import run
from cpexp.generic.optimizer import *
from cpexp.target_related.tac.generator import TACGenerator
from cpexp.target_related.tacp.generator import TACPGenerator
from cpexp.target_related.amd64.generator import AMD64Generator

from cpexp.source_related.exp import source_language as exp
from cpexp.source_related.c4e import source_language as c4e

# Due to the change of source language, only one compile could be executed at a time

sources = {
    'c4e': c4e,
    'exp': exp
}

targets = {
    'tac': TACGenerator,
    'tacp': TACPGenerator,
    'amd64asm': AMD64Generator,
    'amd64elf': AMD64Generator
}

parser = argparse.ArgumentParser()
input_group = parser.add_mutually_exclusive_group()
input_group.add_argument('input', nargs='?', help='Path to the input file')
input_group.add_argument('--STDIN', action='store_true', help='Get input from STDIN instead of file')
parser.add_argument('-s', '--source', choices=list(sources.keys()), required=False, help='Source language')
parser.add_argument('-t', '--target', choices=list(targets.keys()), required=False, help='Target language')
parser.add_argument('-o', '--output', required=False, help='Path to the output file')

parser.add_argument('--tokens', action='store_true', help='Only lex and print tokens instead of compile')
parser.add_argument('-r', '--run', action='store_true', help='Run after compile')
parser.add_argument('-v', '--verbose', action='count', default=0, help='Verbosity')

args = parser.parse_args()

source = args.source
target = args.target

# Input stream, and set source language if needed
input_stream = None
if args.STDIN:
    input_stream = StdinStream()
elif args.input is None:
    logger.error('No input file or stream.')
    exit(1)
else:
    if not os.path.isfile(args.input):
        logger.error(f"{args.input}: Isn't a file.")
        exit(1)
    name, sep, extension = args.input.rpartition('.')
    if args.source is None and sep == '.':
        source = extension
    input_stream = FileStream(args.input)

# Default source and target language
if source is None:
    source = 'c4e'
if target is None:
    target = {
        'c4e': 'amd64elf',
        'exp': 'tac'
    }[source]

# Output method
if args.output is not None:
    output = args.output
else:  # Default output
    if isinstance(input_stream, StdinStream):
        output = None  # None: print to STDOUT
    else:
        output = {
            'tac': 'a.txt',
            'tacp': 'a.txt',
            'amd64asm': 'a.asm',
            'amd64elf': 'a.out'
        }[target]

c = LanguageCompiler(sources[source], targets[target]).run(input_stream)
if args.tokens:
    print('\n'.join(c.lex_tokens()))
else:
    code = c.compile(merge_labels, rename_labels, verbose=args.verbose)
    if output is None:
        print(code)
    else:
        if target == 'amd64elf':
            assemble(code, clean=False, verbose=args.verbose, output_path=output)
        else:
            with open(output, 'w') as f:
                f.write(code)
        if args.run:
            run(verbose=args.verbose)
