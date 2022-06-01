from cpexp.generic.error import MessageException
from cpexp.generic.generator import Register
from cpexp.ir.memory import Place


class AMD64Reg(Register):
    pass


class GeneralRegister(AMD64Reg):
    NAME = '?_?'

    def __init__(self, size: int | Place | None = None):
        if isinstance(size, Place):
            size = size.type.byte
        if size not in [1, 2, 4, 8]:
            raise MessageException(f'Invalid size "{size}"')
        formats = {
            1: '{}l',
            2: '{}x',
            4: 'e{}x',
            8: 'r{}x'
        }
        self.name = formats[size].format(self.NAME[1])
        super().__init__(size)


class WordRegister(AMD64Reg):
    NAME = '?__'

    def __init__(self, size: int | Place | None = None):
        if isinstance(size, Place):
            size = size.type.byte
        if size not in [1, 2, 4, 8]:
            raise MessageException(f'Invalid size "{size}"')
        formats = {
            1: '{}l',
            2: '{}',
            4: 'e{}',
            8: 'r{}'
        }
        self.name = formats[size].format(self.NAME[1:])
        super().__init__(size)


class AdditionalRegister(AMD64Reg):
    NAME = 'r?'

    def __init__(self, size: int | Place | None = None):
        if isinstance(size, Place):
            size = size.type.byte
        if size not in [1, 2, 4, 8]:
            raise MessageException(f'Invalid size "{size}"')
        formats = {
            1: 'r{}b',
            2: 'r{}w',
            4: 'r{}d',
            8: 'r{}'
        }
        self.name = formats[size].format(self.NAME[1:])
        super().__init__(size)


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


class R8(AdditionalRegister):
    NAME = 'r8'


class R9(AdditionalRegister):
    NAME = 'r9'


class R10(AdditionalRegister):
    NAME = 'r10'


class R11(AdditionalRegister):
    NAME = 'r11'


class R12(AdditionalRegister):
    NAME = 'r12'


class R13(AdditionalRegister):
    NAME = 'r13'


class R14(AdditionalRegister):
    NAME = 'r14'


class R15(AdditionalRegister):
    NAME = 'r15'


rax = AX(8)
rbx = BX(8)
rcx = CX(8)
rdx = DX(8)
rsi = SI(8)
rdi = DI(8)
rbp = BP(8)
rsp = SP(8)
r8 = R8(8)
r9 = R9(8)
r10 = R10(8)
r11 = R11(8)
r12 = R12(8)
r13 = R13(8)
r14 = R14(8)
r15 = R15(8)
