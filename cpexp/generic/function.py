from cpexp.generic.memory import DataType


class Function:
    def __init__(self, name: str, return_type: DataType):
        self.name = name
        self.return_type = return_type

    def __str__(self):
        return f'{self.name}[() -> {self.return_type}]'
