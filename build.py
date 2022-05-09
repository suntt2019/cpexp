import argparse
from cpexp.antlr.build import update

parser = argparse.ArgumentParser()
parser.add_argument('--language', '-l', default='exp')
parser.add_argument('--quite', '-q', action='store_false')
parser.add_argument('--force', '-f', action='store_true')

args = parser.parse_args()
update(args.language, verbose=args.quite, force_update=args.force)
