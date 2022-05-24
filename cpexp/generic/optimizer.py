from cpexp.ir.instruction import *


def merge_labels(ir: list[Instruction]):
    if len(ir) == 0:
        return ir
    ret = []
    c1 = ir.pop(0)
    while len(ir) > 0:
        c2 = ir.pop(0)
        if type(c1) == LabelInst and type(c2) == LabelInst:
            c1.label.merge(c2.label)
        else:
            ret.append(c1)
            c1 = c2
    ret.append(c1)
    return ret


def rename_labels(ir: list[Instruction]):
    s = set()
    for code in ir:
        if hasattr(code, 'label'):
            s.add(code.label)
    for i, label in enumerate(s):
        label.set_id(i)
    return ir
