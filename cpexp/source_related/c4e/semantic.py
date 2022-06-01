import base64
from functools import reduce
from itertools import zip_longest

from cpexp.ir.memory import Constant, VoidPlace
from cpexp.ir.instruction import *
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
    def exitFunctionPrototype(self, fp: VA, type_name: str, _id: str, *param_list: str):
        # Merge each two elements into a tuple in a list
        # Reference: https://segmentfault.com/q/1010000007881319
        if type_name == 'void':
            _type = None
        else:
            _type = C4eType(type_name)
        varargs = False
        if len(param_list) > 0 and param_list[-1] == '...':
            param_list = param_list[:-1]
            varargs = True
        parameters = []
        for param_type, param_id in zip_longest(*([iter(param_list)] * 2)):
            parameters.append((C4eType(param_type), param_id))
        with self.at('_id'):
            fp['func'] = self.new_function(Function(_id, _type, parameters, varargs))

    @parameterize_children
    def enterFunctionBody(self, fb: VA, b: VA):
        fb['prototype']['func'].implement()
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
        with self.at('_id'):
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
    def exitDeclare_statement(self, s: VA, _type: str, _id: str, e: VA = None):
        if e is None:
            initial = None
        else:
            initial = e.place
        if self.context.function is None:
            with self.at('_id'):
                place = self.new_global(_id, C4eType(_type), initial)
            s.code = []
            if e is not None and len(e.code) > 0:
                with self.at('_id'):  # TODO: we should at 'e' in fact, but the feature isn't supported for now
                    raise MessageException('Global variable initializer should be const')
        else:
            place = self.new_local(_id, C4eType(_type), initial)
            s.code = []
            if e is not None:
                s.code += e.code
            if initial is not None:
                _e, code = self.convert_type(C4eType(_type), e.place)
                s.code += code + [AssignInst(place, _e)]

    @parameterize_children
    def enterIfStatement(self, s: VA, e: VA, s1: VA):
        if s.next is None:
            s.next = self.new_label()
            s.gen_next = True
        e.true = self.new_label()
        e.false = s.next
        s1.next = s.next

    @parameterize_children
    def exitIfStatement(self, s: VA, e: VA, s1: VA):
        s.code = e.code + [LabelInst(e.true)] \
                 + s1.code
        if s.gen_next:
            s.code += [LabelInst(s.next)]

    @parameterize_children
    def enterIfElseStatement(self, s: VA, e: VA, s1: VA, s2: VA):
        if s.next is None:
            s.next = self.new_label()
            s.gen_next = True
        e.true = self.new_label()
        e.false = self.new_label()
        s1.next = s.next
        s2.next = s.next

    @parameterize_children
    def exitIfElseStatement(self, s: VA, e: VA, s1: VA, s2: VA):
        s.code = e.code + [LabelInst(e.true)] + s1.code \
                 + [GotoInst(s.next), LabelInst(e.false)] + s2.code
        if s.gen_next:
            s.code += [LabelInst(s.next)]

    @parameterize_children
    def enterWhileStatement(self, s: VA, e: VA, s1: VA):
        if s.next is None:
            s.next = self.new_label()
            s.gen_next = True
        s.begin = self.new_label()
        e.true = self.new_label()
        e.false = s.next
        s1.next = s.begin

    @parameterize_children
    def exitWhileStatement(self, s: VA, e: VA, s1: VA):
        s.code = [LabelInst(s.begin)] + e.code \
                 + [LabelInst(e.true)] + s1.code + [GotoInst(s.begin)]
        if s.gen_next:
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
    def exitAsmStatement(self, s: VA, string: str):
        s.code = [AsmInst(string)]

    @parameterize_children
    def enterConditionExpression(self, e: VA, c: VA):
        if e.next is None:
            e.next = self.new_label()
            e.gen_next = True
        c.true = self.new_label()
        c.false = self.new_label()

    @parameterize_children
    def exitConditionExpression(self, e: VA, c: VA):
        _bool = C4eType('bool')
        e.place = self.new_temp(_bool)
        e.code = c.code + [
            LabelInst(c.true),
            AssignInst(e.place, Constant(_bool, 1)),
            GotoInst(e.next),
            LabelInst(c.false),
            AssignInst(e.place, Constant(_bool, 0))
        ]
        if e.gen_next:
            e.code += [LabelInst(e.next)]

    @parameterize_children
    def exitValueExpressionExpression(self, e: VA, ve: VA):
        e.place = ve.place
        e.code = ve.code

    @parameterize_children
    def enterAndCondition(self, c: VA, c1: VA, ac: VA):
        c1.false = c.false
        ac.false = c.false
        c1.true = self.new_label()
        ac.true = c.true

    @parameterize_children
    def exitAndCondition(self, c: VA, c1: VA, ac: VA):
        c.code = c1.code + [
            LabelInst(c1.true)
        ] + ac.code

    @parameterize_children
    def enterAtomicConditionCondition(self, c: VA, ac: VA):
        ac.true = c.true
        ac.false = c.false

    @parameterize_children
    def exitAtomicConditionCondition(self, c: VA, ac: VA):
        c.code = ac.code

    @parameterize_children
    def exitValueExpressionAtomicCondition(self, c: VA, ve: VA):
        _bool = C4eType('bool')
        _ve, code = self.convert_type(_bool, ve.place)
        c.code = ve.code + code \
                 + [IfGotoInst(_ve, '==', Constant(_bool, 1), c.true), GotoInst(c.false)]

    @parameterize_children
    def exitGreaterAtomicCondition(self, ac: VA, ve1: VA, ve2: VA):
        dst_type, code, _e1, _e2 = self.convert_types(ve1.place, ve2.place)
        ac.code = ve1.code + ve2.code + code \
                  + [IfGotoInst(_e1, '>', _e2, ac.true), GotoInst(ac.false)]

    @parameterize_children
    def exitLessAtomicCondition(self, ac: VA, ve1: VA, ve2: VA):
        dst_type, code, _e1, _e2 = self.convert_types(ve1.place, ve2.place)
        ac.code = ve1.code + ve2.code + code \
                  + [IfGotoInst(_e1, '<', _e2, ac.true), GotoInst(ac.false)]

    @parameterize_children
    def exitEqualAtomicCondition(self, ac: VA, ve1: VA, ve2: VA):
        dst_type, code, _e1, _e2 = self.convert_types(ve1.place, ve2.place)
        ac.code = ve1.code + ve2.code + code \
                  + [IfGotoInst(_e1, '==', _e2, ac.true), GotoInst(ac.false)]

    @parameterize_children
    def exitAddValueExpression(self, ve: VA, ve1: VA, t: VA):
        dst_type, code, _e1, _t = self.convert_types(ve1.place, t.place)
        ve.place = self.new_temp(dst_type, ve1.place, t.place)
        ve.code = ve1.code + t.code + code
        if ve.place is None:
            ve.place = Constant(dst_type, ve1.place.value + t.place.value)
        else:
            ve.code += [AddInst(ve.place, _e1, _t)]

    @parameterize_children
    def exitSubValueExpression(self, ve: VA, ve1: VA, t: VA):
        dst_type, code, _e1, _t = self.convert_types(ve1.place, t.place)
        ve.place = self.new_temp(dst_type, ve1.place, t.place)
        ve.code = ve1.code + t.code + code
        if ve.place is None:
            ve.place = Constant(dst_type, ve1.place.value - t.place.value)
        else:
            ve.code += [SubInst(ve.place, _e1, _t)]

    @parameterize_children
    def exitTermValueExpression(self, ve: VA, t: VA):
        ve.place = t.place
        ve.code = t.code

    @parameterize_children
    def exitCallValueExpression(self, s: VA, _id: str, *e: VA):
        arg_code = reduce(lambda a, b: a + b.code, e, [])
        arg_places = list(map(lambda x: x.place, e))
        arg_types = list(map(lambda x: x.type, arg_places))
        with self.at('_id'):
            func = self.get_function(_id, arg_types)
        param_types = list(map(lambda x: x.type, func.param_list))
        with self.at('_id'):  # TODO: should be at 'e' in fact
            if func.varargs:
                _arg_places, arg_conv_code = self.convert_type_list(arg_places[:len(param_types)], param_types)
                _arg_places += arg_places[len(param_types):]
            else:
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
        dst_type, code, _t1, _u = self.convert_types(t1.place, u.place)
        t.place = self.new_temp(dst_type, t1.place, u.place)
        t.code = t1.code + u.code + code
        if t.place is None:
            t.place = Constant(dst_type, t1.place.value * u.place.value)
        else:
            t.code += [MultipleInst(t.place, _t1, _u)]

    @parameterize_children
    def exitDivitionTerm(self, t: VA, t1: VA, u: VA):
        dst_type, code, _t1, _u = self.convert_types(t1.place, u.place)
        t.place = self.new_temp(dst_type, t1.place, u.place)
        t.code = t1.code + u.code + code
        if t.place is None:
            t.place = Constant(dst_type, int(t1.place.value / u.place.value))
        else:
            t.code += [DivisionInst(t.place, _t1, _u)]

    @parameterize_children
    def exitNegUnary(self, u: VA, f: VA):
        u.place = self.new_temp(f.place.type, f.place)
        u.code = []
        if u.place is None:
            u.place = Constant(f.place.type, -f.place.value)
        else:
            u.code += [SubInst(u.place, Constant(f.place.type, 0), f.place)]

    @parameterize_children
    def exitFactorUnary(self, u: VA, f: VA):
        u.place = f.place
        u.code = []

    @parameterize_children
    def exitBracketedFactor(self, f: VA, e: VA):
        f.place = e.place
        f.code = e.code

    @parameterize_children
    def exitIdentifierFactor(self, f: VA, _id: str):
        with self.at('_id'):
            f.place = self.get_variable(_id)
        f.code = []

    @parameterize_children
    def exitInt8Factor(self, f: VA, int8: int):
        f.place = Constant(C4eType('long'), int8)
        f.code = []

    @parameterize_children
    def exitInt10Factor(self, f: VA, int10: int):
        f.place = Constant(C4eType('long'), int10)
        f.code = []

    @parameterize_children
    def exitInt16Factor(self, f: VA, int16: int):
        f.place = Constant(C4eType('long'), int16)
        f.code = []

    @parameterize_children
    def exitReal8Factor(self, f: VA, float8: float):
        f.place = Constant(C4eType('float'), float8)
        f.code = []

    @parameterize_children
    def exitReal10Factor(self, f: VA, float10: float):
        f.place = Constant(C4eType('float'), float10)
        f.code = []

    @parameterize_children
    def exitReal16Factor(self, f: VA, float16: float):
        f.place = Constant(C4eType('float'), float16)
        f.code = []

    @parameterize_children
    def exitStringFactor(self, f: VA, string: str):
        if string.isalnum():
            _id = string
        else:
            _id = base64.b64encode(string.encode("ascii")).decode("ascii").replace('=', '')
        _id = f'str_{_id}'
        _type = C4eType('string')
        # TODO: a bug here, same string constant can't be used twice
        with self.at('string'):
            f.place = self.new_global(_id, _type, Constant(_type, string))
        f.code = []

    @parameterize_children
    def exitCharFactor(self, f: VA, char: str):
        f.place = Constant(C4eType('char'), ord(char))
        f.code = []
