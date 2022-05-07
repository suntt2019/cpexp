import importlib
import os
import time
import shutil

from cpexp.base import *
import cpexp.generated.CPExpParser
import cpexp.generated.CPExpLexer

antlr_alias = 'java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'


def build(verbose=False):
    if verbose:
        print('Run ANTLR:')
        print(f'    ANTLR alias is: {antlr_alias}')
    path = os.path.join(working_dir, 'generated', 'CPExp.g4')
    cmd = f'{antlr_alias} -Dlanguage=Python3 {path}'
    if verbose:
        print(f'    Run build command: {cmd}')
    os.system(cmd)
    if verbose:
        print(f'    Reload packages.')
    importlib.reload(cpexp.generated.CPExpParser)
    importlib.reload(cpexp.generated.CPExpLexer)
    if verbose:
        print('Build finished.')


def clean(verbose=False):
    if verbose:
        print('Clean existing files:')
    directory = os.path.join(working_dir, 'generated')
    for filename in os.listdir(directory):
        if filename.split('.')[-1] == 'g4':
            continue
        if filename == '__init__.py':
            continue
        if verbose:
            print(f'    Remove file {filename}')
        path = os.path.join(working_dir, 'generated', filename)
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
    if verbose:
        print('Clean finished.')


def up_to_date(verbose=False):
    if not all(map(lambda x: os.path.exists(x), generated_files)):
        if verbose:
            print("Some generated file doesn't exist, build isn't up to date.")
        return False
    gen_time = min(map(lambda x: os.stat(x).st_mtime, generated_files))
    grammar_time = os.stat(grammar_file).st_mtime
    if verbose:
        print(f'Generated files earliest updated time: {time.strftime("%Y%m%d-%H:%M:%S", time.localtime(gen_time))}')
        print(f'Grammar file updated time: {time.strftime("%Y%m%d-%H:%M:%S", time.localtime(grammar_time))}')
    if gen_time < grammar_time:
        if verbose:
            print("Grammar file updated later, need to update.")
        return False
    if verbose:
        print("Grammar file updated earlier, build is up to date.")
    return True


def update(verbose=False, force_update=False):
    if not force_update and up_to_date(verbose=verbose):
        if verbose:
            print('Build already up to date.')
        return
    print('Rebuilding...')
    clean(verbose=verbose)
    build(verbose=verbose)
    print('Rebuild finished.')
