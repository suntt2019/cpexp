from cpexp.generic.generator import Register


class X86Reg(Register):
    pass


class GeneralRegister(X86Reg):
    NAME = '?_?'

    def __init__(self, size: int | None = None):
        if size not in [1, 2, 4, 8]:
            raise Exception(f'Invalid size "{size}"')
        formats = {
            1: '{}l',
            2: '{}x',
            4: 'e{}x',
            8: 'r{}x'
        }
        self.name = formats[size].format(self.NAME[1])
        super().__init__(size)


class WordRegister(X86Reg):
    NAME = '?__'

    def __init__(self, size: int | None = None):
        if size not in [2, 4, 8]:
            raise Exception(f'Invalid size "{size}"')
        formats = {
            2: '{}',
            4: 'e{}',
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


rax = AX(8)
rbx = BX(8)
rcx = CX(8)
rdx = DX(8)
rsi = SI(8)
rdi = DI(8)
rbp = BP(8)
rsp = SP(8)
