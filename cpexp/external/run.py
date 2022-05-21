import os.path

from cpexp.base import working_dir
from cpexp.external.external import execute


def run(verbose=0, path=os.path.join(working_dir, '..', 'a.out')):
    if verbose > 0:
        print(f'Running {path}')
    out, exit_code = execute([path], verbose=verbose)
    print(out)
    if verbose > 0:
        print(f'\nProcess finished with exit code {exit_code}.')
