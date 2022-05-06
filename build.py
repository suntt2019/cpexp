import argparse
from cpexp.build import update

parser = argparse.ArgumentParser()

parser.add_argument('--quite', '-q', action='store_false')
parser.add_argument('--force', '-f', action='store_true')
arg = parser.parse_args()
update(verbose=arg.quite, force_update=arg.force)
