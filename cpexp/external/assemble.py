import os.path

from loguru import logger

from cpexp.base import working_dir
from cpexp.external.external import execute
import tempfile
import shutil

from cpexp.generic.error import MessageException

nasm_path = 'nasm'
ld_path = 'ld'


def assemble(code: str, clean=True, verbose=0, output_path=os.path.join(working_dir, '..', 'a.out'),
             directory: str = tempfile.mkdtemp()):
    if verbose > 0:
        logger.debug('Assembling...')
    asm_file = os.path.join(directory, 'temp.s')
    obj_file = os.path.join(directory, 'temp.o')
    if os.path.exists(asm_file):
        os.remove(asm_file)
    if os.path.exists(obj_file):
        os.remove(obj_file)
    if os.path.exists(output_path):
        os.remove(output_path)
    with open(asm_file, 'w') as f:
        f.write(code)
    f.close()

    out, exit_code = execute([nasm_path, '-felf64', asm_file, '-o', obj_file], verbose=verbose)
    if exit_code != 0:
        raise MessageException(f'Assemble Failed: \n{out}')

    # out, exit_code = execute([ld_path, obj_file, '-o', output_path], verbose=verbose)
    out, exit_code = execute([ld_path, '-dynamic-linker', '/lib64/ld-linux-amd64-64.so.2', '-lc', obj_file, '-o', output_path], verbose=verbose)
    if exit_code != 0:
        raise MessageException(f'Assemble Failed: \n{out}')

    if clean:
        shutil.rmtree(directory)
    if verbose > 0:
        logger.debug('Assembling finished.')
