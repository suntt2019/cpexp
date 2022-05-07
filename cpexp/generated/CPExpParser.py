# Generated from /home/sun123t2/code/project/cpexp/cpexp/generated/CPExp.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("i\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\5\2\25\n\2\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\63\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5A\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6L\n\6\f\6\16\6O")
        buf.write("\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7Z\n\7\f\7")
        buf.write("\16\7]\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bg\n\b\3")
        buf.write("\b\2\4\n\f\t\2\4\6\b\n\f\16\2\2\2p\2\24\3\2\2\2\4\26\3")
        buf.write("\2\2\2\6\62\3\2\2\2\b@\3\2\2\2\nB\3\2\2\2\fP\3\2\2\2\16")
        buf.write("f\3\2\2\2\20\25\5\4\3\2\21\22\5\4\3\2\22\23\5\2\2\2\23")
        buf.write("\25\3\2\2\2\24\20\3\2\2\2\24\21\3\2\2\2\25\3\3\2\2\2\26")
        buf.write("\27\5\6\4\2\27\5\3\2\2\2\30\31\7\24\2\2\31\32\7\16\2\2")
        buf.write("\32\33\5\n\6\2\33\34\7\21\2\2\34\63\3\2\2\2\35\36\7\3")
        buf.write("\2\2\36\37\5\b\5\2\37 \7\4\2\2 !\5\6\4\2!\63\3\2\2\2\"")
        buf.write("#\7\3\2\2#$\5\b\5\2$%\7\4\2\2%&\5\6\4\2&\'\7\5\2\2\'(")
        buf.write("\5\6\4\2(\63\3\2\2\2)*\7\6\2\2*+\5\b\5\2+,\7\7\2\2,-\5")
        buf.write("\6\4\2-\63\3\2\2\2./\7\22\2\2/\60\5\2\2\2\60\61\7\23\2")
        buf.write("\2\61\63\3\2\2\2\62\30\3\2\2\2\62\35\3\2\2\2\62\"\3\2")
        buf.write("\2\2\62)\3\2\2\2\62.\3\2\2\2\63\7\3\2\2\2\64\65\5\n\6")
        buf.write("\2\65\66\7\r\2\2\66\67\5\n\6\2\67A\3\2\2\289\5\n\6\29")
        buf.write(":\7\f\2\2:;\5\n\6\2;A\3\2\2\2<=\5\n\6\2=>\7\16\2\2>?\5")
        buf.write("\n\6\2?A\3\2\2\2@\64\3\2\2\2@8\3\2\2\2@<\3\2\2\2A\t\3")
        buf.write("\2\2\2BC\b\6\1\2CD\5\f\7\2DM\3\2\2\2EF\f\5\2\2FG\7\b\2")
        buf.write("\2GL\5\n\6\6HI\f\4\2\2IJ\7\t\2\2JL\5\n\6\5KE\3\2\2\2K")
        buf.write("H\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\13\3\2\2\2OM")
        buf.write("\3\2\2\2PQ\b\7\1\2QR\5\16\b\2R[\3\2\2\2ST\f\4\2\2TU\7")
        buf.write("\n\2\2UZ\5\16\b\2VW\f\3\2\2WX\7\13\2\2XZ\5\16\b\2YS\3")
        buf.write("\2\2\2YV\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\r\3")
        buf.write("\2\2\2][\3\2\2\2^_\7\17\2\2_`\5\n\6\2`a\7\20\2\2ag\3\2")
        buf.write("\2\2bg\7\24\2\2cg\7\27\2\2dg\7\31\2\2eg\7\25\2\2f^\3\2")
        buf.write("\2\2fb\3\2\2\2fc\3\2\2\2fd\3\2\2\2fe\3\2\2\2g\17\3\2\2")
        buf.write("\2\n\24\62@KMY[f")
        return buf.getvalue()


class CPExpParser ( Parser ):

    grammarFileName = "CPExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'else'", "'while'", 
                     "'do'", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'='", 
                     "'('", "')'", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "IF", "THEN", "ELSE", "WHILE", "DO", 
                      "ADD", "SUB", "MUL", "DIV", "LT", "GT", "EQ", "LP", 
                      "RP", "SEM", "LB", "RB", "IDN", "INT16", "REAL16", 
                      "INT8", "REAL8", "INT10", "REAL10", "WS" ]

    RULE_p = 0
    RULE_l = 1
    RULE_s = 2
    RULE_c = 3
    RULE_e = 4
    RULE_t = 5
    RULE_f = 6

    ruleNames =  [ "p", "l", "s", "c", "e", "t", "f" ]

    EOF = Token.EOF
    IF=1
    THEN=2
    ELSE=3
    WHILE=4
    DO=5
    ADD=6
    SUB=7
    MUL=8
    DIV=9
    LT=10
    GT=11
    EQ=12
    LP=13
    RP=14
    SEM=15
    LB=16
    RB=17
    IDN=18
    INT16=19
    REAL16=20
    INT8=21
    REAL8=22
    INT10=23
    REAL10=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def l(self):
            return self.getTypedRuleContext(CPExpParser.LContext,0)


        def p(self):
            return self.getTypedRuleContext(CPExpParser.PContext,0)


        def getRuleIndex(self):
            return CPExpParser.RULE_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP" ):
                listener.enterP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP" ):
                listener.exitP(self)




    def p(self):

        localctx = CPExpParser.PContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_p)
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.l()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.l()
                self.state = 16
                self.p()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s(self):
            return self.getTypedRuleContext(CPExpParser.SContext,0)


        def getRuleIndex(self):
            return CPExpParser.RULE_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL" ):
                listener.enterL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL" ):
                listener.exitL(self)




    def l(self):

        localctx = CPExpParser.LContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_l)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.s()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDN(self):
            return self.getToken(CPExpParser.IDN, 0)

        def EQ(self):
            return self.getToken(CPExpParser.EQ, 0)

        def e(self):
            return self.getTypedRuleContext(CPExpParser.EContext,0)


        def SEM(self):
            return self.getToken(CPExpParser.SEM, 0)

        def IF(self):
            return self.getToken(CPExpParser.IF, 0)

        def c(self):
            return self.getTypedRuleContext(CPExpParser.CContext,0)


        def THEN(self):
            return self.getToken(CPExpParser.THEN, 0)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPExpParser.SContext)
            else:
                return self.getTypedRuleContext(CPExpParser.SContext,i)


        def ELSE(self):
            return self.getToken(CPExpParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(CPExpParser.WHILE, 0)

        def DO(self):
            return self.getToken(CPExpParser.DO, 0)

        def LB(self):
            return self.getToken(CPExpParser.LB, 0)

        def p(self):
            return self.getTypedRuleContext(CPExpParser.PContext,0)


        def RB(self):
            return self.getToken(CPExpParser.RB, 0)

        def getRuleIndex(self):
            return CPExpParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = CPExpParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(CPExpParser.IDN)
                self.state = 23
                self.match(CPExpParser.EQ)
                self.state = 24
                self.e(0)
                self.state = 25
                self.match(CPExpParser.SEM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(CPExpParser.IF)
                self.state = 28
                self.c()
                self.state = 29
                self.match(CPExpParser.THEN)
                self.state = 30
                self.s()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(CPExpParser.IF)
                self.state = 33
                self.c()
                self.state = 34
                self.match(CPExpParser.THEN)
                self.state = 35
                self.s()
                self.state = 36
                self.match(CPExpParser.ELSE)
                self.state = 37
                self.s()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(CPExpParser.WHILE)
                self.state = 40
                self.c()
                self.state = 41
                self.match(CPExpParser.DO)
                self.state = 42
                self.s()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.match(CPExpParser.LB)
                self.state = 45
                self.p()
                self.state = 46
                self.match(CPExpParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPExpParser.EContext)
            else:
                return self.getTypedRuleContext(CPExpParser.EContext,i)


        def GT(self):
            return self.getToken(CPExpParser.GT, 0)

        def LT(self):
            return self.getToken(CPExpParser.LT, 0)

        def EQ(self):
            return self.getToken(CPExpParser.EQ, 0)

        def getRuleIndex(self):
            return CPExpParser.RULE_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC" ):
                listener.enterC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC" ):
                listener.exitC(self)




    def c(self):

        localctx = CPExpParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_c)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.e(0)
                self.state = 51
                self.match(CPExpParser.GT)
                self.state = 52
                self.e(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.e(0)
                self.state = 55
                self.match(CPExpParser.LT)
                self.state = 56
                self.e(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.e(0)
                self.state = 59
                self.match(CPExpParser.EQ)
                self.state = 60
                self.e(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t(self):
            return self.getTypedRuleContext(CPExpParser.TContext,0)


        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPExpParser.EContext)
            else:
                return self.getTypedRuleContext(CPExpParser.EContext,i)


        def ADD(self):
            return self.getToken(CPExpParser.ADD, 0)

        def SUB(self):
            return self.getToken(CPExpParser.SUB, 0)

        def getRuleIndex(self):
            return CPExpParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPExpParser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.t(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CPExpParser.EContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 67
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 68
                        self.match(CPExpParser.ADD)
                        self.state = 69
                        self.e(4)
                        pass

                    elif la_ == 2:
                        localctx = CPExpParser.EContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 70
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 71
                        self.match(CPExpParser.SUB)
                        self.state = 72
                        self.e(3)
                        pass

             
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f(self):
            return self.getTypedRuleContext(CPExpParser.FContext,0)


        def t(self):
            return self.getTypedRuleContext(CPExpParser.TContext,0)


        def MUL(self):
            return self.getToken(CPExpParser.MUL, 0)

        def DIV(self):
            return self.getToken(CPExpParser.DIV, 0)

        def getRuleIndex(self):
            return CPExpParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)



    def t(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPExpParser.TContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.f()
            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CPExpParser.TContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                        self.state = 81
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 82
                        self.match(CPExpParser.MUL)
                        self.state = 83
                        self.f()
                        pass

                    elif la_ == 2:
                        localctx = CPExpParser.TContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                        self.state = 84
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 85
                        self.match(CPExpParser.DIV)
                        self.state = 86
                        self.f()
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CPExpParser.LP, 0)

        def e(self):
            return self.getTypedRuleContext(CPExpParser.EContext,0)


        def RP(self):
            return self.getToken(CPExpParser.RP, 0)

        def IDN(self):
            return self.getToken(CPExpParser.IDN, 0)

        def INT8(self):
            return self.getToken(CPExpParser.INT8, 0)

        def INT10(self):
            return self.getToken(CPExpParser.INT10, 0)

        def INT16(self):
            return self.getToken(CPExpParser.INT16, 0)

        def getRuleIndex(self):
            return CPExpParser.RULE_f

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF" ):
                listener.enterF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF" ):
                listener.exitF(self)




    def f(self):

        localctx = CPExpParser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_f)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPExpParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(CPExpParser.LP)
                self.state = 93
                self.e(0)
                self.state = 94
                self.match(CPExpParser.RP)
                pass
            elif token in [CPExpParser.IDN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(CPExpParser.IDN)
                pass
            elif token in [CPExpParser.INT8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(CPExpParser.INT8)
                pass
            elif token in [CPExpParser.INT10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.match(CPExpParser.INT10)
                pass
            elif token in [CPExpParser.INT16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 99
                self.match(CPExpParser.INT16)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.e_sempred
        self._predicates[5] = self.t_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx:EContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def t_sempred(self, localctx:TContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




