from __future__ import annotations

from cpexp.semantic.variable import VA


class Label:
    def __init__(self, _id: int, append):
        self.id = _id
        self.append = append
        self.usage = []
        append(self)

    def use(self, va: VA, field: str):
        self.usage.append((va, field))

    def merge(self, other: Label):
        ret = Label(self.id, self.append)
        ret.usage = self.usage + other.usage
        return ret

    def set_id(self, _id):
        self.id = _id

    def __repr__(self):
        return f'L{self.id}'
