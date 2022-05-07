# Generated from /home/sun123t2/code/project/cpexp/cpexp/generated/CPExp.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CPExpParser import CPExpParser
else:
    from CPExpParser import CPExpParser

# This class defines a complete listener for a parse tree produced by CPExpParser.
class CPExpListener(ParseTreeListener):

    # Enter a parse tree produced by CPExpParser#SingleProgram.
    def enterSingleProgram(self, ctx:CPExpParser.SingleProgramContext):
        pass

    # Exit a parse tree produced by CPExpParser#SingleProgram.
    def exitSingleProgram(self, ctx:CPExpParser.SingleProgramContext):
        pass


    # Enter a parse tree produced by CPExpParser#AppendedProgram.
    def enterAppendedProgram(self, ctx:CPExpParser.AppendedProgramContext):
        pass

    # Exit a parse tree produced by CPExpParser#AppendedProgram.
    def exitAppendedProgram(self, ctx:CPExpParser.AppendedProgramContext):
        pass


    # Enter a parse tree produced by CPExpParser#SingleLine.
    def enterSingleLine(self, ctx:CPExpParser.SingleLineContext):
        pass

    # Exit a parse tree produced by CPExpParser#SingleLine.
    def exitSingleLine(self, ctx:CPExpParser.SingleLineContext):
        pass


    # Enter a parse tree produced by CPExpParser#AssignStatement.
    def enterAssignStatement(self, ctx:CPExpParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by CPExpParser#AssignStatement.
    def exitAssignStatement(self, ctx:CPExpParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by CPExpParser#IfStatement.
    def enterIfStatement(self, ctx:CPExpParser.IfStatementContext):
        pass

    # Exit a parse tree produced by CPExpParser#IfStatement.
    def exitIfStatement(self, ctx:CPExpParser.IfStatementContext):
        pass


    # Enter a parse tree produced by CPExpParser#IfElseStatement.
    def enterIfElseStatement(self, ctx:CPExpParser.IfElseStatementContext):
        pass

    # Exit a parse tree produced by CPExpParser#IfElseStatement.
    def exitIfElseStatement(self, ctx:CPExpParser.IfElseStatementContext):
        pass


    # Enter a parse tree produced by CPExpParser#WhileStatement.
    def enterWhileStatement(self, ctx:CPExpParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by CPExpParser#WhileStatement.
    def exitWhileStatement(self, ctx:CPExpParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by CPExpParser#BracketedStatement.
    def enterBracketedStatement(self, ctx:CPExpParser.BracketedStatementContext):
        pass

    # Exit a parse tree produced by CPExpParser#BracketedStatement.
    def exitBracketedStatement(self, ctx:CPExpParser.BracketedStatementContext):
        pass


    # Enter a parse tree produced by CPExpParser#GreaterCondition.
    def enterGreaterCondition(self, ctx:CPExpParser.GreaterConditionContext):
        pass

    # Exit a parse tree produced by CPExpParser#GreaterCondition.
    def exitGreaterCondition(self, ctx:CPExpParser.GreaterConditionContext):
        pass


    # Enter a parse tree produced by CPExpParser#LessCondition.
    def enterLessCondition(self, ctx:CPExpParser.LessConditionContext):
        pass

    # Exit a parse tree produced by CPExpParser#LessCondition.
    def exitLessCondition(self, ctx:CPExpParser.LessConditionContext):
        pass


    # Enter a parse tree produced by CPExpParser#EqualCondition.
    def enterEqualCondition(self, ctx:CPExpParser.EqualConditionContext):
        pass

    # Exit a parse tree produced by CPExpParser#EqualCondition.
    def exitEqualCondition(self, ctx:CPExpParser.EqualConditionContext):
        pass


    # Enter a parse tree produced by CPExpParser#TermExpression.
    def enterTermExpression(self, ctx:CPExpParser.TermExpressionContext):
        pass

    # Exit a parse tree produced by CPExpParser#TermExpression.
    def exitTermExpression(self, ctx:CPExpParser.TermExpressionContext):
        pass


    # Enter a parse tree produced by CPExpParser#AddExpression.
    def enterAddExpression(self, ctx:CPExpParser.AddExpressionContext):
        pass

    # Exit a parse tree produced by CPExpParser#AddExpression.
    def exitAddExpression(self, ctx:CPExpParser.AddExpressionContext):
        pass


    # Enter a parse tree produced by CPExpParser#SubExpression.
    def enterSubExpression(self, ctx:CPExpParser.SubExpressionContext):
        pass

    # Exit a parse tree produced by CPExpParser#SubExpression.
    def exitSubExpression(self, ctx:CPExpParser.SubExpressionContext):
        pass


    # Enter a parse tree produced by CPExpParser#MultipleTerm.
    def enterMultipleTerm(self, ctx:CPExpParser.MultipleTermContext):
        pass

    # Exit a parse tree produced by CPExpParser#MultipleTerm.
    def exitMultipleTerm(self, ctx:CPExpParser.MultipleTermContext):
        pass


    # Enter a parse tree produced by CPExpParser#DivitionTerm.
    def enterDivitionTerm(self, ctx:CPExpParser.DivitionTermContext):
        pass

    # Exit a parse tree produced by CPExpParser#DivitionTerm.
    def exitDivitionTerm(self, ctx:CPExpParser.DivitionTermContext):
        pass


    # Enter a parse tree produced by CPExpParser#FactorTerm.
    def enterFactorTerm(self, ctx:CPExpParser.FactorTermContext):
        pass

    # Exit a parse tree produced by CPExpParser#FactorTerm.
    def exitFactorTerm(self, ctx:CPExpParser.FactorTermContext):
        pass


    # Enter a parse tree produced by CPExpParser#BracketedFactor.
    def enterBracketedFactor(self, ctx:CPExpParser.BracketedFactorContext):
        pass

    # Exit a parse tree produced by CPExpParser#BracketedFactor.
    def exitBracketedFactor(self, ctx:CPExpParser.BracketedFactorContext):
        pass


    # Enter a parse tree produced by CPExpParser#IdentifierFactor.
    def enterIdentifierFactor(self, ctx:CPExpParser.IdentifierFactorContext):
        pass

    # Exit a parse tree produced by CPExpParser#IdentifierFactor.
    def exitIdentifierFactor(self, ctx:CPExpParser.IdentifierFactorContext):
        pass


    # Enter a parse tree produced by CPExpParser#Int8Factor.
    def enterInt8Factor(self, ctx:CPExpParser.Int8FactorContext):
        pass

    # Exit a parse tree produced by CPExpParser#Int8Factor.
    def exitInt8Factor(self, ctx:CPExpParser.Int8FactorContext):
        pass


    # Enter a parse tree produced by CPExpParser#Int10Factor.
    def enterInt10Factor(self, ctx:CPExpParser.Int10FactorContext):
        pass

    # Exit a parse tree produced by CPExpParser#Int10Factor.
    def exitInt10Factor(self, ctx:CPExpParser.Int10FactorContext):
        pass


    # Enter a parse tree produced by CPExpParser#Int16Factor.
    def enterInt16Factor(self, ctx:CPExpParser.Int16FactorContext):
        pass

    # Exit a parse tree produced by CPExpParser#Int16Factor.
    def exitInt16Factor(self, ctx:CPExpParser.Int16FactorContext):
        pass



del CPExpParser