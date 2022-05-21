from cpexp.generic.memory import DataType


class Function:
    def __init__(self, name: str, return_type: DataType, param_list: list[tuple[DataType, str]]):
        self.name = name
        self.return_type = return_type
        self.memory_used = 0
        self.param_list = param_list
        # When add overload and function declaration,
        #   add self.definition to mark if function has been defined and where it's defined

    def __str__(self):
        return self.name

    def use_memory(self, size):
        self.memory_used += size
        return self.memory_used
