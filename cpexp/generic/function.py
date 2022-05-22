import math

from cpexp.generic.memory import DataType


class Function:
    def __init__(self, name: str, return_type: DataType | None, param_list: list[tuple[DataType, str]], internal=False):
        self._name = name
        self.return_type = return_type
        self.local_size = 0
        self.param_list = param_list
        self.param_size = sum(map(lambda x: math.ceil(x[0].bits / 8), param_list))
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
