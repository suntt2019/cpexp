import os
import subprocess
import time


def rm(filename: str):
    if os.path.exists(filename):
        print(f'Removed file {filename}')
        os.remove(filename)

def run(cmd):
    out = None
    err = None
    try:
        out = subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        err = e
    print(f'run {" ".join(cmd)}:\n'
          f'{out}\n'
          f'error: {err}')


rm('test.o')
rm('a.out')
run(['nasm', '-felf64', 'test.s'])
run(['ld', 'test.o'])
# run(['gcc', 'test.o'])
# run(['./a.out'])
print('\nRun the result:')
ret = os.system('./a.out')
print(f'<-[end here]\n\nwith exit code {ret}')
