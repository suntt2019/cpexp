import importlib
import os
import time
import shutil

from cpexp.base import *

antlr_alias = 'java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'


def build(language: str, verbose=False):
    src_path = os.path.join(working_dir, 'source_related', language, f'{language}.g4')
    dst_path = grammar_file
    if verbose:
        print(f'Copy and change grammar file:')
        print(f'    Path: {src_path} -> {dst_path}')
    with open(src_path, 'r') as f:
        lines = f.readlines()
    first_line = f'grammar CPExp; // {language}'
    if verbose:
        print(f'    Finished reading')
        print(f'    Change first line: "{first_line}"')
    lines[0] = first_line
    with open(dst_path, 'w') as f:
        f.writelines(lines)
    if verbose:
        print(f'    Finished writing')
        print('Run ANTLR:')
        print(f'    ANTLR alias is: {antlr_alias}')
    cmd = f'{antlr_alias} -Dlanguage=Python3 {dst_path}'
    if verbose:
        print(f'    Run build command: {cmd}')
    os.system(cmd)
    if verbose:
        print(f'    Reload packages.')
    import cpexp.antlr.CPExpParser
    import cpexp.antlr.CPExpLexer
    import cpexp.antlr.CPExpListener
    importlib.reload(cpexp.antlr.CPExpParser)
    importlib.reload(cpexp.antlr.CPExpLexer)
    importlib.reload(cpexp.antlr.CPExpListener)
    if verbose:
        print('Build finished.')


def clean(verbose=False):
    if verbose:
        print('Clean existing files:')
    directory = os.path.join(working_dir, 'antlr')
    for filename in os.listdir(directory):
        if filename.split('.')[-1] == 'g4':
            continue
        if filename in ['__init__.py', 'build.py', '.gitignore']:
            continue
        if verbose:
            print(f'    Remove file {filename}')
        path = os.path.join(working_dir, 'antlr', filename)
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
    if verbose:
        print('Clean finished.')


def up_to_date(language, verbose=False):
    if not all(map(lambda x: os.path.exists(x), generated_files)):
        if verbose:
            print("Some generated file doesn't exist, build isn't up to date.")
        return False
    with open(grammar_file, 'r') as f:
        original_language = f.readline().rpartition('// ')[2][:-1]
    if original_language != language:
        return False
    gen_time = min(map(lambda x: os.stat(x).st_mtime, generated_files))
    source_grammar_file = os.path.join(working_dir, 'source_related', language, f'{language}.g4')
    grammar_time = os.stat(source_grammar_file).st_mtime
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


def update(language, verbose=False, force_update=False):
    if not force_update and up_to_date(language, verbose=verbose):
        if verbose:
            print('Build already up to date.')
        return
    print('Rebuilding...')
    clean(verbose=verbose)
    build(language, verbose=verbose)
    print('Rebuild finished.')
