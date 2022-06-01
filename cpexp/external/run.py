import os.path
import time

from loguru import logger

from cpexp.base import working_dir
from cpexp.external.external import execute


def run(verbose=0, path=os.path.join(working_dir, '..', 'a.out')):
    if verbose > 0:
        logger.debug(f'Running {path}')
    # out, exit_code = execute([path], verbose=verbose)
    # print(out)
    # Use this method to receive content from printf, remember to check 'emulate terminal in output console' in pycharm
    exit_code = os.system(path)
    if verbose > 0:
        logger.debug(f'\nProcess finished with exit code {exit_code}.')
