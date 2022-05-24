from __future__ import annotations

from antlr4.tree.Tree import TerminalNodeImpl, ParseTreeWalker

from cpexp.antlr.CPExpListener import CPExpListener
from cpexp.generic.context import Context
from cpexp.ir.function import Function
from cpexp.ir.instruction import *
from cpexp.ir.label import *
from cpexp.ir.memory import Type, Place, Constant


class Semantic(CPExpListener):

    def __init__(self, token_value: list):
        self.token_value = token_value
        self.variable_attributes = {}
        self.labels = []
        self.temp = []
        self.global_ = {}
        self.functions = {}
        self.context = Context()
        self.init_code = []

    def get_data(self, x):
        if type(x) == TerminalNodeImpl:
            return self.token_value[x.symbol.tokenIndex]
        else:
            self.variable_attributes.setdefault(x, VA())
            return self.variable_attributes.get(x)

    def new_label(self):
        ret = Label(f'L{len(self.labels)}')
        self.labels.append(ret)
        return ret

    def new_temp(self, _type: Type, *dependencies: Place):
        if len(dependencies) > 0 and all(map(lambda x: isinstance(x, Constant), dependencies)):
            return None
        ret = Place(f't{len(self.temp)}', _type)
        self.temp.append(ret)
        return ret

    def new_global(self, name: str, _type: Type, initial=None):
        if name in self.global_:
            raise Exception(f'Global variable "{name}" already exists.')
        ret = Place(name, _type, initial)
        self.global_[name] = ret
        return ret

    def new_local(self, name: str, _type: Type, initial=None):
        address = -self.context.function.use_memory(_type.byte)
        return self.context.add_local(Local(name, _type, address, initial))

    def get_variable(self, name: str):
        local = self.context[name]
        if local is not None:
            return local
        if name in self.global_:
            return self.global_[name]
        if name in self.functions:
            raise Exception(f'Function {name} is not a variable.')
        raise Exception(f'Undeclared variable {name}.')

    # TODO: refactor 'new_xxx' into a symbol table (symbol manager)
    # Structure: (memory, label, function) -> (symbol table, context)
    # For context free symbols, in the symbol table
    # For context related symbols, in the context
    def new_function(self, name: str, return_type: Type | None, param_types: list[tuple[Type, str]]):
        if name in self.functions:
            raise Exception(f'Function "{name}" already exists.')
        ret = Function(name, return_type, param_types)
        self.functions[name] = ret
        return ret

    def get_function(self, name: str, param_types: list[Type] = None):
        # TODO: add function overload
        if name not in self.functions:
            raise Exception(f'Undeclared function "{name}".')
        return self.functions[name]

    def convert_type(self, dst_type: Type, src: Place) -> tuple[Place, list[ConvertInst]]:
        if src.type == dst_type:
            return src, []
        dst = self.new_temp(dst_type, src)
        if dst is None:
            dst = Constant(dst_type, src.value)
        code = ConvertInst(src, dst)
        return dst, [code]

    def convert_types(self, *places: Place, type_require: Type = None):
        dst_type = max(list(map(lambda x: x.type, places)))
        if type_require is not None:
            dst_type = max(dst_type, type_require)
        ret = [dst_type, []]
        for p in places:
            dst, code = self.convert_type(dst_type, p)
            ret[1] += code
            ret.append(dst)
        return ret

    def convert_type_list(self, places: list[Place], types: list[Type]) -> tuple[list[Place], list[Instruction]]:
        _places = []
        code = []
        if len(places) != len(types):
            raise Exception(f"Count of places({len(places)}) and types({len(types)}) doesn't match")
        for arg_place, _type in zip(places, types):
            _place, c = self.convert_type(_type, arg_place)
            _places.append(_place)
            code += c
        return _places, code

    def enter(self, func=None):
        self.context = self.context.enter(func)

    def exit(self):
        self.context = self.context.exit()

    def analyze(self, ast):
        walker = ParseTreeWalker()
        walker.walk(self, ast)
        init = [FunctionStartInst(Function('init', None, [], internal=True))] + self.init_code + [ReturnInst()]
        data_section = [SectionStartInst('data')]
        bss_section = [SectionStartInst('bss')]
        for var in self.temp + list(self.global_.values()):
            if var.initial is None:
                bss_section.append(BSSInst(var))
            else:
                # TODO: try to calculate initial expression during compile
                if isinstance(var.initial, Constant):
                    data_section.append(DataInst(var))
                else:
                    bss_section.append(BSSInst(var))
        return data_section + bss_section + [SectionStartInst('text')] + init + self.variable_attributes[ast].code


class VA:
    """VA: Variable Attributes"""

    def __init__(self):
        self.code = None  # type: list[Instruction] | None
        self.place = None  # type: Place | None
        self.begin = None  # type: Label | None
        self.next = None  # type: Label | None
        self.true = None  # type: Label | None
        self.false = None  # type: Label | None
        self.other = {}
        self.gen_s_next = False

    def __str__(self):
        return f'(code={self.code}, place={self.place})'

    def __getitem__(self, item):
        return self.other[item]

    def __setitem__(self, key, value):
        self.other[key] = value


def parameterize_children(func):
    def wrapper(self, ctx):
        args = list(filter(
            lambda x: x != '_',
            map(
                lambda x: self.get_data(x),
                [ctx] + list(ctx.getChildren())
            )
        ))
        func(
            self,
            *args
        )

    return wrapper
