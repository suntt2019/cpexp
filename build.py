import argparse
from cpexp.antlr.build import update

parser = argparse.ArgumentParser()
parser.add_argument('--language', '-l', default='exp')
parser.add_argument('--verbose', '-v', action='count')
parser.add_argument('--force', '-f', action='store_true')

args = parser.parse_args()
if args.verbose is None:
    args.verbose = 0
update(args.language, verbose=args.verbose, force_update=args.force)
