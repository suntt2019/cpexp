from cpexp.ir.instructions import *


def merge_labels(tac: list[Instruction]):
    ret = []
    c1 = tac.pop(0)
    while len(tac) > 0:
        c2 = tac.pop(0)
        if type(c1) == LabelInst and type(c2) == LabelInst:
            c1.label.merge(c2.label)
        else:
            ret.append(c1)
            c1 = c2
    ret.append(c1)
    return ret


def rename_labels(tac: list[Instruction]):
    s = set()
    for code in tac:
        if hasattr(code, 'label'):
            s.add(code.label)
    for i, label in enumerate(s):
        label.set_id(i)
    return tac
