class VA:
    """VA: Variable Attributes"""

    def __init__(self):
        self.code = None
        self.place = None
        self.begin = None
        self.next = None
        self.true = None
        self.false = None
        self.gen_s_next = False

    def __str__(self):
        return f'(code={self.code}, place={self.place})'
