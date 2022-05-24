import math

from cpexp.ir.base import InstructionContent
from cpexp.ir.memory import Type, Local


class Function(InstructionContent):
    def __init__(self, name: str, return_type: Type | None, param_list: list[tuple[Type, str]], internal=False):
        self._name = name  # type: str
        self.return_type = return_type  # type: Type
        self.local_size = 0  # type: int
        self.param_list = list(map(lambda x: Local(x[1], x[0], 0), param_list))  # type: list[Local]
        self.internal = internal
        # When add overload and function declaration,
        #   add self.definition to mark if function has been defined and where it's defined

    @property
    def name(self):
        if self.internal:
            return f'_{self._name}'
        else:
            return f'func_{self._name}'

    def use_memory(self, size):
        self.local_size += size
        return self.local_size
