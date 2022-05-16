# Generated from /home/sun123t2/code/project/cpexp/cpexp/antlr/CPExp.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\5\2\23\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3/\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5H\n\5\f\5\16\5K\13\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\7\6V\n\6\f\6\16\6Y\13\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7c\n\7\3\7\2\4\b\n\b\2\4\6")
        buf.write("\b\n\f\2\2\2m\2\22\3\2\2\2\4.\3\2\2\2\6<\3\2\2\2\b>\3")
        buf.write("\2\2\2\nL\3\2\2\2\fb\3\2\2\2\16\23\5\4\3\2\17\20\5\4\3")
        buf.write("\2\20\21\5\2\2\2\21\23\3\2\2\2\22\16\3\2\2\2\22\17\3\2")
        buf.write("\2\2\23\3\3\2\2\2\24\25\7\25\2\2\25\26\7\21\2\2\26\27")
        buf.write("\5\b\5\2\27\30\7\22\2\2\30/\3\2\2\2\31\32\7\3\2\2\32\33")
        buf.write("\5\6\4\2\33\34\7\4\2\2\34\35\5\4\3\2\35/\3\2\2\2\36\37")
        buf.write("\7\3\2\2\37 \5\6\4\2 !\7\4\2\2!\"\5\4\3\2\"#\7\5\2\2#")
        buf.write("$\5\4\3\2$/\3\2\2\2%&\7\6\2\2&\'\5\6\4\2\'(\7\7\2\2()")
        buf.write("\5\4\3\2)/\3\2\2\2*+\7\23\2\2+,\5\2\2\2,-\7\24\2\2-/\3")
        buf.write("\2\2\2.\24\3\2\2\2.\31\3\2\2\2.\36\3\2\2\2.%\3\2\2\2.")
        buf.write("*\3\2\2\2/\5\3\2\2\2\60\61\5\b\5\2\61\62\7\r\2\2\62\63")
        buf.write("\5\b\5\2\63=\3\2\2\2\64\65\5\b\5\2\65\66\7\f\2\2\66\67")
        buf.write("\5\b\5\2\67=\3\2\2\289\5\b\5\29:\7\16\2\2:;\5\b\5\2;=")
        buf.write("\3\2\2\2<\60\3\2\2\2<\64\3\2\2\2<8\3\2\2\2=\7\3\2\2\2")
        buf.write(">?\b\5\1\2?@\5\n\6\2@I\3\2\2\2AB\f\5\2\2BC\7\b\2\2CH\5")
        buf.write("\n\6\2DE\f\4\2\2EF\7\t\2\2FH\5\n\6\2GA\3\2\2\2GD\3\2\2")
        buf.write("\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J\t\3\2\2\2KI\3\2\2\2")
        buf.write("LM\b\6\1\2MN\5\f\7\2NW\3\2\2\2OP\f\4\2\2PQ\7\n\2\2QV\5")
        buf.write("\f\7\2RS\f\3\2\2ST\7\13\2\2TV\5\f\7\2UO\3\2\2\2UR\3\2")
        buf.write("\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\13\3\2\2\2YW\3\2\2")
        buf.write("\2Z[\7\17\2\2[\\\5\b\5\2\\]\7\20\2\2]c\3\2\2\2^c\7\25")
        buf.write("\2\2_c\7\30\2\2`c\7\32\2\2ac\7\26\2\2bZ\3\2\2\2b^\3\2")
        buf.write("\2\2b_\3\2\2\2b`\3\2\2\2ba\3\2\2\2c\r\3\2\2\2\n\22.<G")
        buf.write("IUWb")
        return buf.getvalue()


class CPExpParser ( Parser ):

    grammarFileName = "CPExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'else'", "'while'", 
                     "'do'", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'=='", 
                     "'('", "')'", "'='", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "IF", "THEN", "ELSE", "WHILE", "DO", 
                      "ADD", "SUB", "MUL", "DIV", "LT", "GT", "EQ", "LP", 
                      "RP", "ASSIGN", "SEM", "LB", "RB", "IDN", "INT16", 
                      "REAL16", "INT8", "REAL8", "INT10", "REAL10", "WS" ]

    RULE_p = 0
    RULE_s = 1
    RULE_c = 2
    RULE_e = 3
    RULE_t = 4
    RULE_f = 5

    ruleNames =  [ "p", "s", "c", "e", "t", "f" ]

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
    ASSIGN=15
    SEM=16
    LB=17
    RB=18
    IDN=19
    INT16=20
    REAL16=21
    INT8=22
    REAL8=23
    INT10=24
    REAL10=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPExpParser.RULE_p

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AppendedProgramContext(PContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.PContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def s(self):
            return self.getTypedRuleContext(CPExpParser.SContext,0)

        def p(self):
            return self.getTypedRuleContext(CPExpParser.PContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAppendedProgram" ):
                listener.enterAppendedProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAppendedProgram" ):
                listener.exitAppendedProgram(self)


    class SingleProgramContext(PContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.PContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def s(self):
            return self.getTypedRuleContext(CPExpParser.SContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleProgram" ):
                listener.enterSingleProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleProgram" ):
                listener.exitSingleProgram(self)



    def p(self):

        localctx = CPExpParser.PContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_p)
        try:
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = CPExpParser.SingleProgramContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.s()
                pass

            elif la_ == 2:
                localctx = CPExpParser.AppendedProgramContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.s()
                self.state = 14
                self.p()
                pass


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


        def getRuleIndex(self):
            return CPExpParser.RULE_s

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BracketedStatementContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(CPExpParser.LB, 0)
        def p(self):
            return self.getTypedRuleContext(CPExpParser.PContext,0)

        def RB(self):
            return self.getToken(CPExpParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracketedStatement" ):
                listener.enterBracketedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracketedStatement" ):
                listener.exitBracketedStatement(self)


    class IfStatementContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(CPExpParser.IF, 0)
        def c(self):
            return self.getTypedRuleContext(CPExpParser.CContext,0)

        def THEN(self):
            return self.getToken(CPExpParser.THEN, 0)
        def s(self):
            return self.getTypedRuleContext(CPExpParser.SContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)


    class IfElseStatementContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseStatement" ):
                listener.enterIfElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseStatement" ):
                listener.exitIfElseStatement(self)


    class WhileStatementContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(CPExpParser.WHILE, 0)
        def c(self):
            return self.getTypedRuleContext(CPExpParser.CContext,0)

        def DO(self):
            return self.getToken(CPExpParser.DO, 0)
        def s(self):
            return self.getTypedRuleContext(CPExpParser.SContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class AssignStatementContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.SContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDN(self):
            return self.getToken(CPExpParser.IDN, 0)
        def ASSIGN(self):
            return self.getToken(CPExpParser.ASSIGN, 0)
        def e(self):
            return self.getTypedRuleContext(CPExpParser.EContext,0)

        def SEM(self):
            return self.getToken(CPExpParser.SEM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)



    def s(self):

        localctx = CPExpParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_s)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CPExpParser.AssignStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(CPExpParser.IDN)
                self.state = 19
                self.match(CPExpParser.ASSIGN)
                self.state = 20
                self.e(0)
                self.state = 21
                self.match(CPExpParser.SEM)
                pass

            elif la_ == 2:
                localctx = CPExpParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(CPExpParser.IF)
                self.state = 24
                self.c()
                self.state = 25
                self.match(CPExpParser.THEN)
                self.state = 26
                self.s()
                pass

            elif la_ == 3:
                localctx = CPExpParser.IfElseStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(CPExpParser.IF)
                self.state = 29
                self.c()
                self.state = 30
                self.match(CPExpParser.THEN)
                self.state = 31
                self.s()
                self.state = 32
                self.match(CPExpParser.ELSE)
                self.state = 33
                self.s()
                pass

            elif la_ == 4:
                localctx = CPExpParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(CPExpParser.WHILE)
                self.state = 36
                self.c()
                self.state = 37
                self.match(CPExpParser.DO)
                self.state = 38
                self.s()
                pass

            elif la_ == 5:
                localctx = CPExpParser.BracketedStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.match(CPExpParser.LB)
                self.state = 41
                self.p()
                self.state = 42
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


        def getRuleIndex(self):
            return CPExpParser.RULE_c

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LessConditionContext(CContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.CContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPExpParser.EContext)
            else:
                return self.getTypedRuleContext(CPExpParser.EContext,i)

        def LT(self):
            return self.getToken(CPExpParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessCondition" ):
                listener.enterLessCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessCondition" ):
                listener.exitLessCondition(self)


    class GreaterConditionContext(CContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.CContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPExpParser.EContext)
            else:
                return self.getTypedRuleContext(CPExpParser.EContext,i)

        def GT(self):
            return self.getToken(CPExpParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterCondition" ):
                listener.enterGreaterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterCondition" ):
                listener.exitGreaterCondition(self)


    class EqualConditionContext(CContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.CContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPExpParser.EContext)
            else:
                return self.getTypedRuleContext(CPExpParser.EContext,i)

        def EQ(self):
            return self.getToken(CPExpParser.EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualCondition" ):
                listener.enterEqualCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualCondition" ):
                listener.exitEqualCondition(self)



    def c(self):

        localctx = CPExpParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_c)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CPExpParser.GreaterConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.e(0)
                self.state = 47
                self.match(CPExpParser.GT)
                self.state = 48
                self.e(0)
                pass

            elif la_ == 2:
                localctx = CPExpParser.LessConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.e(0)
                self.state = 51
                self.match(CPExpParser.LT)
                self.state = 52
                self.e(0)
                pass

            elif la_ == 3:
                localctx = CPExpParser.EqualConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.e(0)
                self.state = 55
                self.match(CPExpParser.EQ)
                self.state = 56
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


        def getRuleIndex(self):
            return CPExpParser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TermExpressionContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(CPExpParser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpression" ):
                listener.enterTermExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpression" ):
                listener.exitTermExpression(self)


    class AddExpressionContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(CPExpParser.EContext,0)

        def ADD(self):
            return self.getToken(CPExpParser.ADD, 0)
        def t(self):
            return self.getTypedRuleContext(CPExpParser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpression" ):
                listener.enterAddExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpression" ):
                listener.exitAddExpression(self)


    class SubExpressionContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(CPExpParser.EContext,0)

        def SUB(self):
            return self.getToken(CPExpParser.SUB, 0)
        def t(self):
            return self.getTypedRuleContext(CPExpParser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpression" ):
                listener.enterSubExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpression" ):
                listener.exitSubExpression(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPExpParser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CPExpParser.TermExpressionContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 61
            self.t(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CPExpParser.AddExpressionContext(self, CPExpParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 63
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 64
                        self.match(CPExpParser.ADD)
                        self.state = 65
                        self.t(0)
                        pass

                    elif la_ == 2:
                        localctx = CPExpParser.SubExpressionContext(self, CPExpParser.EContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 66
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 67
                        self.match(CPExpParser.SUB)
                        self.state = 68
                        self.t(0)
                        pass

             
                self.state = 73
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


        def getRuleIndex(self):
            return CPExpParser.RULE_t

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultipleTermContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(CPExpParser.TContext,0)

        def MUL(self):
            return self.getToken(CPExpParser.MUL, 0)
        def f(self):
            return self.getTypedRuleContext(CPExpParser.FContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultipleTerm" ):
                listener.enterMultipleTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultipleTerm" ):
                listener.exitMultipleTerm(self)


    class DivitionTermContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(CPExpParser.TContext,0)

        def DIV(self):
            return self.getToken(CPExpParser.DIV, 0)
        def f(self):
            return self.getTypedRuleContext(CPExpParser.FContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivitionTerm" ):
                listener.enterDivitionTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivitionTerm" ):
                listener.exitDivitionTerm(self)


    class FactorTermContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def f(self):
            return self.getTypedRuleContext(CPExpParser.FContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorTerm" ):
                listener.enterFactorTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorTerm" ):
                listener.exitFactorTerm(self)



    def t(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPExpParser.TContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_t, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CPExpParser.FactorTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 75
            self.f()
            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 83
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CPExpParser.MultipleTermContext(self, CPExpParser.TContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                        self.state = 77
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 78
                        self.match(CPExpParser.MUL)
                        self.state = 79
                        self.f()
                        pass

                    elif la_ == 2:
                        localctx = CPExpParser.DivitionTermContext(self, CPExpParser.TContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_t)
                        self.state = 80
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 81
                        self.match(CPExpParser.DIV)
                        self.state = 82
                        self.f()
                        pass

             
                self.state = 87
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


        def getRuleIndex(self):
            return CPExpParser.RULE_f

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BracketedFactorContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(CPExpParser.LP, 0)
        def e(self):
            return self.getTypedRuleContext(CPExpParser.EContext,0)

        def RP(self):
            return self.getToken(CPExpParser.RP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracketedFactor" ):
                listener.enterBracketedFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracketedFactor" ):
                listener.exitBracketedFactor(self)


    class Int10FactorContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT10(self):
            return self.getToken(CPExpParser.INT10, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt10Factor" ):
                listener.enterInt10Factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt10Factor" ):
                listener.exitInt10Factor(self)


    class IdentifierFactorContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDN(self):
            return self.getToken(CPExpParser.IDN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierFactor" ):
                listener.enterIdentifierFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierFactor" ):
                listener.exitIdentifierFactor(self)


    class Int16FactorContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT16(self):
            return self.getToken(CPExpParser.INT16, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt16Factor" ):
                listener.enterInt16Factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt16Factor" ):
                listener.exitInt16Factor(self)


    class Int8FactorContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CPExpParser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT8(self):
            return self.getToken(CPExpParser.INT8, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt8Factor" ):
                listener.enterInt8Factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt8Factor" ):
                listener.exitInt8Factor(self)



    def f(self):

        localctx = CPExpParser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_f)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPExpParser.LP]:
                localctx = CPExpParser.BracketedFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(CPExpParser.LP)
                self.state = 89
                self.e(0)
                self.state = 90
                self.match(CPExpParser.RP)
                pass
            elif token in [CPExpParser.IDN]:
                localctx = CPExpParser.IdentifierFactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(CPExpParser.IDN)
                pass
            elif token in [CPExpParser.INT8]:
                localctx = CPExpParser.Int8FactorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(CPExpParser.INT8)
                pass
            elif token in [CPExpParser.INT10]:
                localctx = CPExpParser.Int10FactorContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.match(CPExpParser.INT10)
                pass
            elif token in [CPExpParser.INT16]:
                localctx = CPExpParser.Int16FactorContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 95
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
        self._predicates[3] = self.e_sempred
        self._predicates[4] = self.t_sempred
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
         




