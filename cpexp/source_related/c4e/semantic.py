import operator
from functools import reduce
from itertools import zip_longest

from cpexp.generic.memory import Constant, VoidPlace
from cpexp.ir.instructions import *
from cpexp.generic.semantic import Semantic, parameterize_children, VA
from cpexp.source_related.c4e.memory import C4eType


class C4eSemantic(Semantic):

    @parameterize_children
    def exitProgram(self, p: VA, *pp: VA):  # pp: program part
        p.code = reduce(lambda a, b: a + b.code, pp, [])

    @parameterize_children
    def enterFunctionDefinition(self, f: VA, fp: VA, fb: VA):
        fb['prototype'] = fp

    @parameterize_children
    def exitFunctionDefinition(self, fd: VA, fp: VA, fb: VA):
        fd.code = fb.code

    @parameterize_children
    def exitFunctionDeclaration(self, fd: VA, fp: VA):
        fd.code = []

    @parameterize_children
    def exitFunctionPrototype(self, fp: VA, type_name, _id, *param_list):
        # Merge each two elements into a tuple in a list
        # Reference: https://segmentfault.com/q/1010000007881319
        if type_name == 'void':
            _type = None
        else:
            _type = C4eType(type_name)
        parameters = []
        for param_type, param_id in zip_longest(*([iter(param_list)] * 2)):
            parameters.append((C4eType(param_type), param_id))
        fp['func'] = self.new_function(_id, _type, parameters)

    @parameterize_children
    def enterFunctionBody(self, fb: VA, b: VA):
        self.enter(fb['prototype']['func'])

    @parameterize_children
    def exitFunctionBody(self, fb: VA, b: VA):
        func = fb['prototype']['func']
        fb.code = [FunctionStartInst(func)] \
                  + b.code \
                  + [FunctionEndInst(func)]
        self.exit()

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
        target = self.get_variable(_id)
        _e, code = self.convert_type(target.type, e.place)
        s.code = e.code + code + [AssignInst(target, _e)]

    @parameterize_children
    def exitEmptyStatement(self, s: VA):
        s.code = []

    @parameterize_children
    def exitExpressionStatement(self, s: VA, e: VA):
        s.code = e.code

    @parameterize_children
    def exitDeclare_statement(self, s: VA, _type, _id, e: VA = None):
        if e is None:
            initial = None
        else:
            initial = e.place
        if self.context.function is None:
            place = self.new_global(_id, C4eType(_type), initial)
            s.code = []
            if e is not None and len(e.code) > 0:
                self.init_code += e.code + [AssignInst(place, e.place)]
        else:
            place = self.new_local(_id, C4eType(_type), initial)
            s.code = e.code + [AllocInst(place)]  # TODO: remove AllocInst class since it's useless
            if initial is not None:
                s.code.append(AssignInst(place, e.place))

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
                 + [GotoInst(s.next), LabelInst(c.false)] + s2.code
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
    def exitReturnValueStatement(self, s: VA, e: VA):
        func = self.context.function
        _e, code = self.convert_type(func.return_type, e.place)
        s.code = e.code + code + [ReturnInst(_e)]

    @parameterize_children
    def exitReturnVoidStatement(self, s: VA):
        s.code = [ReturnInst()]

    @parameterize_children
    def enterBracketedStatement(self, s: VA, b: VA):
        self.enter()

    @parameterize_children
    def exitBracketedStatement(self, s: VA, b: VA):
        s.code = b.code
        self.exit()

    @parameterize_children
    def exitAsmStatement(self, s: VA, string):
        s.code = [AsmInst(string)]

    @parameterize_children
    def exitGreaterCondition(self, c: VA, e1: VA, e2: VA):
        dst_type, code, _e1, _e2 = self.convert_types(e1.place, e2.place)
        c.code = e1.code + e2.code + code \
                 + [IfGotoInst(_e1, '>', _e2, c.true), GotoInst(c.false)]

    @parameterize_children
    def exitLessCondition(self, c: VA, e1: VA, e2: VA):
        dst_type, code, _e1, _e2 = self.convert_types(e1.place, e2.place)
        c.code = e1.code + e2.code + code \
                 + [IfGotoInst(_e1, '<', _e2, c.true), GotoInst(c.false)]

    @parameterize_children
    def exitEqualCondition(self, c: VA, e1: VA, e2: VA):
        dst_type, code, _e1, _e2 = self.convert_types(e1.place, e2.place)
        c.code = e1.code + e2.code + code \
                 + [IfGotoInst(_e1, '==', _e2, c.true), GotoInst(c.false)]

    @parameterize_children
    def exitAddExpression(self, e: VA, e1: VA, t: VA):
        dst_type, code, _e1, _t = self.convert_types(e1.place, t.place)
        e.place = self.new_temp(dst_type)
        e.code = e1.code + t.code + code + [AddInst(e.place, _e1, _t)]

    @parameterize_children
    def exitSubExpression(self, e: VA, e1: VA, t: VA):
        e.place = self.new_temp(max(e1.place.type, t.place.type))
        e.code = e1.code + t.code + [SubInst(e.place, e1.place, t.place)]

    @parameterize_children
    def exitTermExpression(self, e: VA, t: VA):
        e.place = t.place
        e.code = t.code

    @parameterize_children
    def exitCallExpression(self, s: VA, _id, *e: VA):
        arg_code = reduce(lambda a, b: a + b.code, e, [])
        arg_places = list(map(lambda x: x.place, e))
        arg_types = list(map(lambda x: x.type, arg_places))
        func = self.get_function(_id, arg_types)
        param_types = list(map(lambda x: x.type, func.param_list))
        _arg_places, arg_conv_code = self.convert_type_list(arg_places, param_types)
        if func.return_type is not None:
            s.place = self.new_temp(func.return_type)
        else:
            s.place = VoidPlace()
        s.code = arg_code + arg_conv_code + [CallInst(s.place, func, _arg_places)]

    @parameterize_children
    def exitUnaryTerm(self, t: VA, u: VA):
        t.place = u.place
        t.code = u.code

    @parameterize_children
    def exitMultipleTerm(self, t: VA, t1: VA, u: VA):
        t.place = self.new_temp(max(t1.place.type, u.place.type))
        t.code = t1.code + u.code + [MultipleInst(t.place, t1.place, u.place)]

    @parameterize_children
    def exitDivitionTerm(self, t: VA, t1: VA, u: VA):
        t.place = self.new_temp(max(t1.place.type, u.place.type))
        t.code = t1.code + u.code + [DivisionInst(t.place, t1.place, u.place)]

    @parameterize_children
    def exitNegUnary(self, u: VA, f: VA):
        u.place = self.new_temp(f.place.type)
        u.code = [SubInst(u.place, Constant(C4eType('long'), 0), f.place)]

    @parameterize_children
    def exitFactorUnary(self, u: VA, f: VA):
        u.place = f.place
        u.code = []

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
        f.place = Constant(C4eType('long'), int8)
        f.code = []

    @parameterize_children
    def exitInt10Factor(self, f: VA, int10):
        f.place = Constant(C4eType('long'), int10)
        f.code = []

    @parameterize_children
    def exitInt16Factor(self, f: VA, int16):
        f.place = Constant(C4eType('long'), int16)
        f.code = []

    @parameterize_children
    def exitReal8Factor(self, f: VA, float8):
        f.place = Constant(C4eType('float'), float8)
        f.code = []

    @parameterize_children
    def exitReal10Factor(self, f: VA, float10):
        f.place = Constant(C4eType('float'), float10)
        f.code = []

    @parameterize_children
    def exitReal16Factor(self, f: VA, float16):
        f.place = Constant(C4eType('float'), float16)
        f.code = []
