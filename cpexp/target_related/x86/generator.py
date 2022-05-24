import os.path

from cpexp.base import working_dir
from cpexp.ir.generator import *
from cpexp.target_related.x86.instruction import *
from cpexp.target_related.x86.register import *

template = None


# TODO: use different register for different size
# TODO: Alloc registers


def get_template():
    global template
    if template is not None:
        return template
    with open(os.path.join(working_dir, 'target_related', 'x86', 'template.s')) as f:
        content = f.read()
    prefix, _, leftover = content.partition('; PREFIX_END')
    _, _, suffix = leftover.partition('; SUFFIX_BEGIN')
    template = (prefix, suffix)
    return template


# Generate intel syntax for nasm
class X86Generator(Generator):
    def generate(self, tac: list[Instruction]) -> str:
        prefix, suffix = get_template()
        generated = ''.join(map(lambda x: ''.join(map(str, self.gen(x))), tac))
        return prefix + generated + suffix

    @meth_dispatch
    def gen(self, inst) -> list:
        raise Exception(f'Unable to generate from type {inst.__class__.__name__}')

    @gen.register
    def _(self, inst: SectionStartInst):
        return [
            f'\n\tsection .{inst.name}\n'
        ]

    @gen.register
    def _(self, inst: DataInst):
        return [
            f'\t{inst.place.name}: d{bits_to_data_size(inst.place.type.bits)} {inst.place.initial}\n'
        ]

    @gen.register
    def _(self, inst: BSSInst):
        return [
            f'\t{inst.place.name}: res{bits_to_data_size(inst.place.type.bits)} 1\n'
        ]

    @gen.register
    def _(self, inst: FunctionStartInst):
        alloc = []
        if inst.function.local_size > 0:
            alloc = [SUB(SP(q_), inst.function.local_size)]
        return [
                   f'\n{inst.function.name}:\n',
                   PUSH(BP(q_)),
                   MOV(BP(q_), SP(q_))
               ] + alloc

    @gen.register
    def _(self, inst: FunctionEndInst):
        return []

    @gen.register
    def _(self, inst: ConvertInst):
        instructions = {
            'int': {
                'long': [
                    CDQ()
                ]
            },
            'long': {
                'int': []
            }
        }
        src = inst.src.type.name
        dst = inst.dst.type.name
        if src == dst:
            raise Exception('Unexpected conversion instruction between two same type variables')
        if src not in instructions:
            raise Exception(f'Unsupported convert source type {src}')
        if dst not in instructions[src]:
            raise Exception(f'Unsupported convert target type {src} from type {dst}')
        return [MOV(AX(inst.src.type), inst.src)] + instructions[src][dst] + [MOV(inst.dst, AX(inst.dst.type))]

    @gen.register
    def _(self, inst: AssignInst):
        return [
            MOV(AX(inst.right.type), inst.right),
            MOV(inst.left, AX(inst.left.type))
        ]

    @gen.register
    def _(self, inst: ReturnInst):
        if inst.value is None:
            assign = []
        else:
            assign = [MOV(AX(inst.value.type), inst.value)]
        return [
                   MOV(SP(q_), BP(q_)),
                   POP(BP(q_)),
               ] + assign + [
                   RET()
               ]

    @gen.register
    def _(self, inst: CallInst):
        push_args = []
        for arg, param in zip(inst.arguments, inst.function.param_list):
            push_args += [
                MOV(AX(arg.type), arg),
                MOV(param, AX(param.type))
            ]
        assign = []
        if not isinstance(inst.place, VoidPlace):
            assign = [MOV(inst.place, AX(inst.place.type))]
        return [SUB(SP(q_), len(inst.function.param_list) * 8)] \
               + push_args + [CALL(inst.function.name)] + assign \
               + [ADD(SP(q_), len(inst.function.param_list) * 8)]  # 64-bit mode, 8byte per word

    @gen.register
    def _(self, inst: AllocInst):
        return []

    @gen.register
    def _(self, inst: TwoOperandAssignInst):
        instructions = {
            '+': {
                'long': [ADD(AX(q_), inst.operand2)],
                'int': [ADD(AX(d_), inst.operand2)]
            },
            '-': {
                'long': [SUB(AX(q_), inst.operand2)],
                'int': [SUB(AX(d_), inst.operand2)]
            },
            '*': {
                'long': [MOV(BX(q_), inst.operand2), IMUL(BX(q_))],
                'int': [MOV(BX(d_), inst.operand2), IMUL(BX(d_))]
            },
            '/': {
                'long': [XOR(DX(q_), DX(q_)), MOV(BX(q_), inst.operand2), IDIV(BX(q_))],
                'int': [XOR(DX(d_), DX(d_)), MOV(BX(d_), inst.operand2), IDIV(BX(d_))]
            }
        }
        op = inst.OP
        type_name = inst.target.type.name
        if op not in instructions:
            raise Exception(f'Unsupported operator {op}')
        if type_name not in instructions[op]:
            raise Exception(f'Unsupported type {type_name} for operator {op}')
        return [MOV(AX(inst.operand1.type), inst.operand1)] \
               + instructions[op][type_name] \
               + [MOV(inst.target, AX(inst.target.type))]

    @gen.register
    def _(self, inst: IfGotoInst):
        instructions = {
            '>': {
                'long': [JG(inst.label)]
            },
            '<': {
                'long': [JL(inst.label)]
            },
            '==': {
                'long': [JE(inst.label)]
            },
        }
        op = inst.op
        type_name = inst.operand1.type.name
        if op not in instructions:
            raise Exception(f'Unsupported operator {op}')
        if type_name not in instructions[op]:
            raise Exception(f'Unsupported type {type_name} for operator {op}')
        return [
                   MOV(AX(inst.operand1.type), inst.operand1),
                   CMP(AX(inst.operand2.type), inst.operand2),
               ] + instructions[op][type_name]

    @gen.register
    def _(self, inst: GotoInst):
        return [JMP(inst.label)]

    @gen.register
    def _(self, inst: LabelInst):
        return [f'{inst.label}:']

    @gen.register
    def _(self, inst: AsmInst):
        return [f'{inst.code}\n']
