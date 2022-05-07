from antlr4.tree.Tree import TerminalNodeImpl

import cpexp.generated.CPExpListener
from cpexp.semantic.helpers import *
from cpexp.semantic.instructions import *


class VA:
    """VA: Variable Attributes"""

    def __init__(self):
        self.code = None
        self.place = None
        self.true = None
        self.false = None
        self.begin = None
        self.next = None
        self.gen_s_next = False

    def __str__(self):
        return f'(code={self.code}, place={self.place})'


def parameterize_children(func):
    def wrapper(self, ctx):
        print(ctx.__class__.__name__[:-7], func.__name__[:3])
        print('before', self.variable_attributes.get(ctx))
        func(
            self,
            *filter(
                lambda x: x != '_',
                map(
                    lambda x: self.get_data(x),
                    [ctx] + list(ctx.getChildren())
                )
            )
        )
        print('after', self.variable_attributes[ctx])

    return wrapper


class CPESemantic(cpexp.generated.CPExpListener.CPExpListener):

    def __init__(self, token_value: list):
        self.token_value = token_value
        self.variable_attributes = {}

    def get_data(self, x):
        if type(x) == TerminalNodeImpl:
            return self.token_value[x.symbol.tokenIndex]
        else:
            self.variable_attributes.setdefault(x, VA())
            return self.variable_attributes.get(x)

    # @parameterize_children
    # def enterTop(self, top: VA, p: VA):
    #     top.next = new_label()
    #     p.next = top.next
    #
    # @parameterize_children
    # def exitTop(self, top: VA, p: VA):
    #     top.code = p.code + [LabelInst(top.next)]

    @parameterize_children
    def exitSingleProgram(self, p: VA, l: VA):
        p.code = l.code

    @parameterize_children
    def exitAppendedProgram(self, p: VA, l: VA, p1: VA):
        p.code = l.code + p1.code

    @parameterize_children
    def exitSingleLine(self, l: VA, s: VA):
        l.code = s.code

    @parameterize_children
    def exitAssignStatement(self, s: VA, _id, e: VA):
        s.code = e.code + [AssignInst(_id, e.place)]

    @parameterize_children
    def enterIfStatement(self, s: VA, c: VA, s1: VA):
        if s.next is None:
            s.next = new_label()
            s.gen_s_next = True
        c.true = new_label()
        c.false = s.next
        s1.next = s.next

    @parameterize_children
    def exitIfStatement(self, s: VA, c: VA, s1: VA):
        s.code = c.code + [LabelInst(c.true)] \
                 + s1.code
        if s.gen_s_next:
            s.code += [LabelInst(s.next)]

    @parameterize_children
    def enterIfElseStatement(self, s: VA, c: VA, s1: VA, s2: VA):
        if s.next is None:
            s.next = new_label()
            s.gen_s_next = True
        c.true = new_label()
        c.false = new_label()
        s1.next = s.next
        s2.next = s.next

    @parameterize_children
    def exitIfElseStatement(self, s: VA, c: VA, s1: VA, s2: VA):
        s.code = c.code + [LabelInst(c.true)] + s1.code \
                 + [LabelInst(c.false)] + s2.code
        if s.gen_s_next:
            s.code += [LabelInst(s.next)]

    @parameterize_children
    def enterWhileStatement(self, s: VA, c: VA, s1: VA):
        if s.next is None:
            s.next = new_label()
            s.gen_s_next = True
        s.begin = new_label()
        c.true = new_label()
        c.false = s.next
        s1.next = s.begin

    @parameterize_children
    def exitWhileStatement(self, s: VA, c: VA, s1: VA):
        s.code = [LabelInst(s.begin)] + c.code \
                 + [LabelInst(c.true)] + s1.code + [GotoInst(s.begin)]
        if s.gen_s_next:
            s.code += [LabelInst(s.next)]

    @parameterize_children
    def exitGreaterCondition(self, c: VA, e1: VA, e2: VA):
        c.code = e1.code + e2.code \
                 + [IfGotoInst(e1.place, '>', e2.place, c.true), GotoInst(c.false)]

    @parameterize_children
    def exitLessCondition(self, c: VA, e1: VA, e2: VA):
        c.code = e1.code + e2.code \
                 + [IfGotoInst(e1.place, '<', e2.place, c.true), GotoInst(c.false)]

    @parameterize_children
    def exitEqualCondition(self, c: VA, e1: VA, e2: VA):
        c.code = e1.code + e2.code \
                 + [IfGotoInst(e1.place, '==', e2.place, c.true), GotoInst(c.false)]

    @parameterize_children
    def exitAddExpression(self, e: VA, e1: VA, t: VA):
        place = new_temp()
        e.place = place
        e.code = e1.code + t.code + [AddInst(place, e1.place, t.place)]

    @parameterize_children
    def exitSubExpression(self, e: VA, e1: VA, t: VA):
        place = new_temp()
        e.place = place
        e.code = e1.code + t.code + [SubInst(place, e1.place, t.place)]

    @parameterize_children
    def exitTermExpression(self, e: VA, t: VA):
        e.place = t.place
        e.code = t.code

    @parameterize_children
    def exitMultipleTerm(self, t: VA, t1: VA, f: VA):
        place = new_temp()
        t.place = place
        t.code = t1.code + f.code + [MultipleInst(place, t1.place, f.place)]

    @parameterize_children
    def exitDivitionTerm(self, t: VA, t1: VA, f: VA):
        place = new_temp()
        t.place = place
        t.code = t1.code + f.code + [DivisionInst(place, t1.place, f.place)]

    @parameterize_children
    def exitFactorTerm(self, t: VA, f: VA):
        t.place = f.place
        t.code = f.code

    @parameterize_children
    def exitBracketedFactor(self, f: VA, e: VA):
        f.place = e.place
        f.code = e.code

    @parameterize_children
    def exitIdentifierFactor(self, f: VA, _id):
        f.place = _id
        f.code = []

    @parameterize_children
    def exitInt8Factor(self, f: VA, int8):
        f.place = int8
        f.code = []

    @parameterize_children
    def exitInt10Factor(self, f: VA, int10):
        f.place = int10
        f.code = []

    @parameterize_children
    def exitInt16Factor(self, f: VA, int16):
        f.place = int16
        f.code = []
