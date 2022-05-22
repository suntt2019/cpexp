from antlr4.Token import CommonToken
from cpexp.generic.lexer import CPELexer


class C4eLexer(CPELexer):
    def token_value(self, token: CommonToken) -> any:
        txt = token.text
        ret = txt
        type_id = token.type
        type_name = self.symbolicNames[type_id]
        if type_id < len(self.literalNames) and type_name != 'VOID':
            ret = '_'
        elif type_name.startswith('INT'):
            base = int(type_name[3:])
            ret = int(txt, base)
        elif type_name.startswith('REAL'):
            base = int(type_name[4:])
            prefix_digit = len({
                                   8: '0',
                                   10: '',
                                   16: '0x'
                               }[base])
            integral, dec = txt[prefix_digit:].split('.')
            a = int(integral + dec, base)
            ret = a / (base ** len(dec))
        elif type_name == 'STR':
            ret = txt[1:-1]
        return ret

    def format_token(self, token: CommonToken) -> str:
        type_id = token.type
        if type_id < len(self.literalNames):
            type_name = self.literalNames[type_id][1:-1]
        else:
            type_name = self.symbolicNames[type_id]
        return f'{type_name}\t{self.token_values[token.tokenIndex]}'
