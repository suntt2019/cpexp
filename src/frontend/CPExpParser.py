# Generated from CPExp.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\n\4\2\t\2\3\2\3\2\3\2\5\2\b\n\2\3\2\2\2\3\2\2\2\2\t\2")
        buf.write("\7\3\2\2\2\4\5\7\3\2\2\5\b\5\2\2\2\6\b\7\3\2\2\7\4\3\2")
        buf.write("\2\2\7\6\3\2\2\2\b\3\3\2\2\2\3\7")
        return buf.getvalue()


class CPExpParser ( Parser ):

    grammarFileName = "CPExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", 
                     "'='", "'('", "')'", "';'", "'if'", "'then'", "'else'", 
                     "'while'", "'do'" ]

    symbolicNames = [ "<INVALID>", "TOKEN", "IDN", "INT16", "REAL16", "INT8", 
                      "REAL8", "INT10", "REAL10", "ADD", "SUB", "MUL", "DIV", 
                      "LT", "GT", "EQ", "LB", "RB", "SEM", "IF", "THEN", 
                      "ELSE", "WHILE", "DO", "WS" ]

    RULE_r = 0

    ruleNames =  [ "r" ]

    EOF = Token.EOF
    TOKEN=1
    IDN=2
    INT16=3
    REAL16=4
    INT8=5
    REAL8=6
    INT10=7
    REAL10=8
    ADD=9
    SUB=10
    MUL=11
    DIV=12
    LT=13
    GT=14
    EQ=15
    LB=16
    RB=17
    SEM=18
    IF=19
    THEN=20
    ELSE=21
    WHILE=22
    DO=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN(self):
            return self.getToken(CPExpParser.TOKEN, 0)

        def r(self):
            return self.getTypedRuleContext(CPExpParser.RContext,0)


        def getRuleIndex(self):
            return CPExpParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)




    def r(self):

        localctx = CPExpParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.state = 5
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2
                self.match(CPExpParser.TOKEN)
                self.state = 3
                self.r()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 4
                self.match(CPExpParser.TOKEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





