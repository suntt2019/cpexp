class VA:
    """VA: Variable Attributes"""

    def __init__(self):
        self.code = None
        self.place = None
        self.labels = {
            'begin': None,
            'next': None,
            'true': None,
            'false': None
        }
        self.gen_s_next = False

    def set_label(self, field: str, label):
        self.labels[field] = label

    @property
    def begin(self):
        return self.labels['begin']

    @begin.setter
    def begin(self, label):
        label.use(self, 'begin')
        self.labels['begin'] = label

    @property
    def next(self):
        return self.labels['next']

    @next.setter
    def next(self, label):
        label.use(self, 'next')
        self.labels['next'] = label

    @property
    def true(self):
        return self.labels['true']

    @true.setter
    def true(self, label):
        label.use(self, 'true')
        self.labels['true'] = label

    @property
    def false(self):
        return self.labels['false']

    @false.setter
    def false(self, label):
        label.use(self, 'false')
        self.labels['false'] = label

    def __str__(self):
        return f'(code={self.code}, place={self.place})'
