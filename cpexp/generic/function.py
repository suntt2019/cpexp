from cpexp.generic.memory import DataType


class Function:
    def __init__(self, name: str, return_type: DataType):
        self.name = name
        self.return_type = return_type
        self.memory_used = 0

    def __str__(self):
        return f'{self.name}[() -> {self.return_type}]'

    def use_memory(self, size):
        self.memory_used += size
