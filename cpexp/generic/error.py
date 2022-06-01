import sys

from antlr4.error.ErrorListener import ErrorListener
from loguru import logger


class CompileException(Exception):
    def log(self):
        pass


class SingleException(CompileException):
    pass


class MultipleException(CompileException):
    def __init__(self, children: list[SingleException]):
        self.children = children

    def log(self):
        for e in self.children:
            e.log()


class MessageException(SingleException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

    def log(self):
        logger.error(self.message)


class PositionException(SingleException):
    def __init__(self, message: str, line: int, column: int, line_str: str | None = None):
        self.message = message
        self.line = line
        self.column = column
        self.content = line_str
        super().__init__(message)

    def log(self):
        logger.error(f'line {self.line}:{self.column} {self.message}')
        if self.content is not None:
            line = str(self.line)
            prefix = f'{(4 - len(line)) * " "}{line} |'
            logger.error(f'{prefix} {self.content}')
            logger.error(f'{(len(prefix) - 1) * " "}| {self.column * " "}^')


class CPEErrorListener(ErrorListener):
    INSTANCE = None

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        content = None
        if hasattr(recognizer, 'source'):
            content = recognizer.source[line - 1]
        self.errors.append(PositionException(msg, line, column, content))


CPEErrorListener.INSTANCE = CPEErrorListener()


def try_compile(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except CompileException as e:
            e.log()
            logger.critical(f'{func.__name__.capitalize()} failed.')
            exit(1)

    return wrapper
