from cpexp.generic.function import Function


class Context:
    def __init__(self):
        self.functions = []

    def enter(self):
        # TODO: enter new IDN namespace
        pass

    def enter_function(self, func: Function):
        self.functions.append(func)
        self.enter()

    def exit_function(self):
        if len(self.functions) == 0:
            raise Exception('Exiting from non-function context')  # Internal error
        self.functions.pop()

    def function(self):
        if len(self.functions) == 0:
            raise Exception('Getting function in non-function context')  # Internal error
        return self.functions[-1]
