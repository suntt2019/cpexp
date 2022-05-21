import os.path

from cpexp.base import working_dir
from cpexp.external.external import execute
import tempfile
import shutil

nasm_path = 'nasm'
ld_path = 'ld'


def assemble(code: str, clean=True, verbose=0, output_path=os.path.join(working_dir, '..', 'a.out')):
    if verbose > 0:
        print('Assembling...')
    directory = tempfile.mkdtemp()
    asm_file = os.path.join(directory, 'temp.s')
    obj_file = os.path.join(directory, 'temp.o')
    with open(asm_file, 'w') as f:
        f.write(code)
    f.close()

    out, exit_code = execute([nasm_path, '-felf64', asm_file, '-o', obj_file], verbose=verbose)
    if exit_code != 0:
        raise Exception(f'Assemble Failed: \n{out}')

    out, exit_code = execute([ld_path, obj_file, '-o', output_path], verbose=verbose)
    if exit_code != 0:
        raise Exception(f'Assemble Failed: \n{out}')

    if clean:
        shutil.rmtree(directory)
    if verbose > 0:
        print('Assembling finished.')
