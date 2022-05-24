from cpexp.ir.memory import Type
from cpexp.ir.instruction import AssignInst, LabelInst, GotoInst, IfGotoInst, AddInst, SubInst, MultipleInst, \
    DivisionInst
from cpexp.generic.semantic import Semantic, parameterize_children, VA


class ExpSemantic(Semantic):

    def new_temp(self):
        return self.new_temp(Type('_'))

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
            s.next = self.new_label()
            s.gen_s_next = True
        c.true = self.new_label()
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
            s.next = self.new_label()
            s.gen_s_next = True
        c.true = self.new_label()
        c.false = self.new_label()
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
            s.next = self.new_label()
            s.gen_s_next = True
        s.begin = self.new_label()
        c.true = self.new_label()
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
                 + [IfGotoInst(e1.place, '=', e2.place, c.true), GotoInst(c.false)]

    @parameterize_children
    def exitAddExpression(self, e: VA, e1: VA, t: VA):
        place = self.new_temp()
        e.place = place
        e.code = e1.code + t.code + [AddInst(place, e1.place, t.place)]

    @parameterize_children
    def exitSubExpression(self, e: VA, e1: VA, t: VA):
        place = self.new_temp()
        e.place = place
        e.code = e1.code + t.code + [SubInst(place, e1.place, t.place)]

    @parameterize_children
    def exitTermExpression(self, e: VA, t: VA):
        e.place = t.place
        e.code = t.code

    @parameterize_children
    def exitFactorTerm(self, t: VA, f: VA):
        t.place = f.place
        t.code = f.code

    @parameterize_children
    def exitMultipleTerm(self, t: VA, t1: VA, f: VA):
        place = self.new_temp()
        t.place = place
        t.code = t1.code + f.code + [MultipleInst(place, t1.place, f.place)]

    @parameterize_children
    def exitDivitionTerm(self, t: VA, t1: VA, f: VA):
        place = self.new_temp()
        t.place = place
        t.code = t1.code + f.code + [DivisionInst(place, t1.place, f.place)]

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
