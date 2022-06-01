import importlib
import os
import time
import shutil

from loguru import logger

from cpexp.base import *

antlr_alias = 'java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'


def build(language: str, verbose=0):
    src_path = os.path.join(working_dir, 'source_related', language, f'{language}.g4')
    dst_path = grammar_file
    if verbose > 1:
        logger.debug(f'Copy and change grammar file:')
        logger.debug(f'    Path: {src_path} -> {dst_path}')
    with open(src_path, 'r') as f:
        lines = f.readlines()
    first_line = f'grammar CPExp; // {language}'
    if verbose > 1:
        logger.debug(f'    Finished reading')
        logger.debug(f'    Change first line: "{first_line}"')
    lines[0] = first_line
    with open(dst_path, 'w') as f:
        f.writelines(lines)
    if verbose > 1:
        logger.debug(f'    Finished writing')
        logger.debug('Run ANTLR:')
        logger.debug(f'    ANTLR alias is: {antlr_alias}')
    cmd = f'{antlr_alias} -Dlanguage=Python3 {dst_path}'
    if verbose > 1:
        logger.debug(f'    Run build command: {cmd}')
    os.system(cmd)
    if verbose > 1:
        logger.debug(f'    Reload packages.')
    if verbose > 1:
        logger.debug('Build finished.')


def clean(verbose=0):
    if verbose > 1:
        logger.debug('Clean existing files:')
    directory = os.path.join(working_dir, 'antlr')
    for filename in os.listdir(directory):
        if filename.split('.')[-1] == 'g4':
            continue
        if filename in ['__init__.py', 'build.py', '.gitignore']:
            continue
        if verbose > 1:
            logger.debug(f'    Remove file {filename}')
        path = os.path.join(working_dir, 'antlr', filename)
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)
    if verbose > 1:
        logger.debug('Clean finished.')


def up_to_date(language, verbose=0):
    if not all(map(lambda x: os.path.exists(x), generated_files)):
        if verbose > 1:
            logger.debug("Some generated file doesn't exist, build isn't up to date.")
        return False
    with open(grammar_file, 'r') as f:
        original_language = f.readline().rpartition('// ')[2][:-1]
    if original_language != language:
        return False
    gen_time = min(map(lambda x: os.stat(x).st_mtime, generated_files))
    source_grammar_file = os.path.join(working_dir, 'source_related', language, f'{language}.g4')
    grammar_time = os.stat(source_grammar_file).st_mtime
    if verbose > 1:
        logger.debug(f'Generated files earliest updated time: {time.strftime("%Y%m%d-%H:%M:%S", time.localtime(gen_time))}')
        logger.debug(f'Grammar file updated time: {time.strftime("%Y%m%d-%H:%M:%S", time.localtime(grammar_time))}')
    if gen_time < grammar_time:
        if verbose > 1:
            logger.debug("Grammar file updated later, need to update.")
        return False
    if verbose > 1:
        logger.debug("Grammar file updated earlier, build is up to date.")
    return True


def update(language, verbose=0, force_update=False):
    if not force_update and up_to_date(language, verbose=verbose):
        if verbose > 0:
            logger.debug('Build already up to date.')
        return
    if verbose > 0:
        logger.debug('Rebuilding...')
    clean(verbose=verbose)
    build(language, verbose=verbose)
    if verbose > 0:
        logger.debug('Rebuild finished.')
    logger.info('Rebuilt code, Please run the program again to compile.')
    exit(1)
