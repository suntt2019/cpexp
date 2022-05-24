from typing import final


class Instruction:
    pass


class InstructionContent:

    @final
    def __str__(self):
        raise Exception(f'Try to convert type {self.__class__.__name__} instruction content into string')

    @final
    def __repr__(self):
        self.__str__()
