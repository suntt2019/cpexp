import math

from cpexp.generic.memory import DataType, Local


class Function:
    def __init__(self, name: str, return_type: DataType | None, param_list: list[tuple[DataType, str]], internal=False):
        self._name = name
        self.return_type = return_type
        self.local_size = 0
        self.param_list = []
        address = 8  # The original rbp is set in the first quad-word
        for _type, _id in param_list:
            address += math.ceil(_type.bits / 8)
            self.param_list.append(Local(_id, _type, address))
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
