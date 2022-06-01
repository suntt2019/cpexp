from typing import final

from cpexp.generic.error import MessageException


class Instruction:
    pass


class InstructionContent:

    @final
    def __str__(self):
        raise MessageException(f'Try to convert type {self.__class__.__name__} instruction content into string')

    @final
    def __repr__(self):
        self.__str__()
