from subprocess import Popen, PIPE, STDOUT

from loguru import logger


def execute(command: list[str], stdin=None, verbose=0):
    if verbose > 1:
        logger.debug(f'    Running external program: {" ".join(command)}')
    _stdin = None
    _in = None
    if stdin is not None:
        _stdin = PIPE
        _in = bytes(stdin, encoding='utf-8')
    out = Popen(command, stdin=_stdin, stderr=STDOUT, stdout=PIPE)
    ret = out.communicate(input=_in)[0].decode('utf-8'), out.returncode
    if verbose > 1:
        logger.debug(f'    Run finished with exit code {ret[1]}, ', end='')
        output = ret[0]
        if output.replace('\n', '') == '':
            logger.debug('output is empty')
        else:
            logger.debug(f'output(enclosed in brackets): [\n{output}]')
    return ret
