import operator
from functools import reduce

from cpexp.generic.memory import Constant
from cpexp.ir.instructions import *
from cpexp.generic.semantic import Semantic, parameterize_children, VA
from cpexp.source_related.c4e.memory import C4eType


class C4eSemantic(Semantic):

    @parameterize_children
    def exitProgram(self, p: VA, b: VA, *f: VA):
        p.code = b.code + reduce(lambda a, b: a + b.code, f, [])

    @parameterize_children
    def enterFunction(self, f: VA, _type, _id, b: VA):
        func = self.new_function(_id, C4eType(_type))
        self.enter(func)

    @parameterize_children
    def exitFunction(self, f: VA, _type, _id, b: VA):
        func = self.context.function
        f.code = [FunctionStartInst(func)] \
                 + b.code \
                 + [FunctionEndInst(func)]
        self.exit()

    @parameterize_children
    def exitDeclareBlock(self, b: VA, *s: VA):
        b.code = reduce(lambda a, b: a + b.code, s, [])

    @parameterize_children
    def exitStatementsBlock(self, p: VA, *s: VA):
        p.code = reduce(lambda a, b: a + b.code, s, [])

    @parameterize_children
    def exitStatemenet(self, s: VA, s1: VA):
        s.code = s1.code

    @parameterize_children
    def exitNon_declare_statement(self, s: VA, s1: VA):
        s.code = s1.code

    @parameterize_children
    def exitAssignStatement(self, s: VA, _id, e: VA):
        s.code = e.code + [AssignInst(self.get_variable(_id), e.place)]

    @parameterize_children
    def exitEmptyStatement(self, s: VA):
        s.code = []

    @parameterize_children
    def exitExpressionStatement(self, s: VA, e: VA):
        s.code = e.code

    @parameterize_children
    def exitDeclareStatement(self, s: VA, _type, _id):
        if self.context.function is None:
            self.new_global(_id, C4eType(_type))
            s.code = []
        else:
            place = self.new_local(_id, C4eType(_type))
            s.code = [AllocInst(place)]

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
    def exitReturnStatement(self, s: VA, e: VA):
        func = self.context.function
        _e, code = self.convert_type(func.return_type, e.place)
        s.code = e.code + code + [ReturnInst(_e)]

    @parameterize_children
    def enterBracketedStatement(self, s: VA, b: VA):
        self.enter()

    @parameterize_children
    def exitBracketedStatement(self, s: VA, b: VA):
        s.code = b.code
        self.exit()

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
        dst_type, code, _e1, _t = self.convert_types(e1.place, t.place)
        place = self.new_temp(dst_type)
        e.place = place
        e.code = e1.code + t.code + code + [AddInst(place, _e1, _t)]

    @parameterize_children
    def exitSubExpression(self, e: VA, e1: VA, t: VA):
        place = self.new_temp(max(e1.place.type, t.place.type))
        e.place = place
        e.code = e1.code + t.code + [SubInst(place, e1.place, t.place)]

    @parameterize_children
    def exitTermExpression(self, e: VA, t: VA):
        e.place = t.place
        e.code = t.code

    @parameterize_children
    def exitCallExpression(self, s: VA, _id):
        function = self.get_function(_id)
        s.place = self.new_temp(function.return_type)
        s.code = [CallInst(s.place, function)]

    @parameterize_children
    def exitFactorTerm(self, t: VA, f: VA):
        t.place = f.place
        t.code = f.code

    @parameterize_children
    def exitMultipleTerm(self, t: VA, t1: VA, f: VA):
        place = self.new_temp(max(t1.place.type, f.place.type))
        t.place = place
        t.code = t1.code + f.code + [MultipleInst(place, t1.place, f.place)]

    @parameterize_children
    def exitDivitionTerm(self, t: VA, t1: VA, f: VA):
        place = self.new_temp(max(t1.place.type, f.place.type))
        t.place = place
        t.code = t1.code + f.code + [DivisionInst(place, t1.place, f.place)]

    @parameterize_children
    def exitBracketedFactor(self, f: VA, e: VA):
        f.place = e.place
        f.code = e.code

    @parameterize_children
    def exitIdentifierFactor(self, f: VA, _id):
        f.place = self.get_variable(_id)
        f.code = []

    @parameterize_children
    def exitInt8Factor(self, f: VA, int8):
        f.place = Constant(C4eType('int'), int8)
        f.code = []

    @parameterize_children
    def exitInt10Factor(self, f: VA, int10):
        f.place = Constant(C4eType('int'), int10)
        f.code = []

    @parameterize_children
    def exitInt16Factor(self, f: VA, int16):
        f.place = Constant(C4eType('int'), int16)
        f.code = []
