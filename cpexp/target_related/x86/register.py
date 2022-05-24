from cpexp.generic.memory import DataType
from cpexp.target_related.x86.base import bits_to_data_size


class Register:
    NAME = 'REG'
    b = 'b'
    w = 'w'
    d = 'd'
    q = 'q'

    def __init__(self, size: str | DataType = None):
        self.name = self.NAME
        if size is None:
            return
        if type(size) == str:
            data_size = size
        elif isinstance(size, DataType):
            data_size = bits_to_data_size(size.bits)
        else:
            raise Exception(f'Unsupported type {type(size)} size {size}')
        self.set_size(data_size)

    def set_size(self, data_size: str):
        pass


b_ = Register.b
w_ = Register.w
d_ = Register.d
q_ = Register.q


class GeneralRegister(Register):
    NAME = '?_?'

    def set_size(self, data_size: str):
        if data_size not in 'bwdq':
            raise Exception(f'Invalid data type "{data_size}"')
        name = self.name[1]
        formats = {
            'b': '{}l',
            'w': '{}x',
            'd': 'e{}x',
            'q': 'r{}x'
        }
        self.name = formats[data_size].format(name)


class WordRegister(Register):
    NAME = '?__'

    def set_size(self, data_size: str):
        if data_size not in 'wdq':
            raise Exception(f'Invalid data type "{data_size}"')
        name = self.name[1:]
        formats = {
            'w': '{}',
            'd': 'e{}',
            'q': 'r{}'
        }
        self.name = formats[data_size].format(name)


class AX(GeneralRegister):
    NAME = '?a?'


class BX(GeneralRegister):
    NAME = '?b?'


class CX(GeneralRegister):
    NAME = '?c?'


class DX(GeneralRegister):
    NAME = '?d?'


class SI(WordRegister):
    NAME = '?si'


class DI(WordRegister):
    NAME = '?di'


class SP(WordRegister):
    NAME = '?sp'


class BP(WordRegister):
    NAME = '?bp'
