from __future__ import annotations

from cpexp.ir.base import InstructionContent
from cpexp.ir.instruction import *


# TODO: Label table

class Label(InstructionContent):
    def __init__(self, _id: int):
        self.id = _id
        self.usage = []

    def use(self, inst: WithLabelInst):
        self.usage.append(inst)

    def merge(self, other: Label):
        self.usage += other.usage
        for inst in other.usage:
            inst.set_label(self)
        del other

    def set_id(self, _id):
        self.id = _id

    def __repr__(self):
        return f'L{self.id}'
