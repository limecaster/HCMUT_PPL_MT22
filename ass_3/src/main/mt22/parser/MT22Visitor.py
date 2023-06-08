# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MT22Parser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionPrototype.
    def visitFunctionPrototype(self, ctx:MT22Parser.FunctionPrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterList.
    def visitParameterList(self, ctx:MT22Parser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterListPrime.
    def visitParameterListPrime(self, ctx:MT22Parser.ParameterListPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterDeclarion.
    def visitParameterDeclarion(self, ctx:MT22Parser.ParameterDeclarionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:MT22Parser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDeclShortForm.
    def visitVarDeclShortForm(self, ctx:MT22Parser.VarDeclShortFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varDeclFullForm.
    def visitVarDeclFullForm(self, ctx:MT22Parser.VarDeclFullFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayDeclaration.
    def visitArrayDeclaration(self, ctx:MT22Parser.ArrayDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayDeclShortForm.
    def visitArrayDeclShortForm(self, ctx:MT22Parser.ArrayDeclShortFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayDeclFullForm.
    def visitArrayDeclFullForm(self, ctx:MT22Parser.ArrayDeclFullFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionList.
    def visitExpressionList(self, ctx:MT22Parser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexedExpression.
    def visitIndexedExpression(self, ctx:MT22Parser.IndexedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functionCall.
    def visitFunctionCall(self, ctx:MT22Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexedOperator.
    def visitIndexedOperator(self, ctx:MT22Parser.IndexedOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#booleanOperator.
    def visitBooleanOperator(self, ctx:MT22Parser.BooleanOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalOperator.
    def visitRelationalOperator(self, ctx:MT22Parser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplyOperator.
    def visitMultiplyOperator(self, ctx:MT22Parser.MultiplyOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addingOperator.
    def visitAddingOperator(self, ctx:MT22Parser.AddingOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringOperator.
    def visitStringOperator(self, ctx:MT22Parser.StringOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MT22Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mt22Type.
    def visitMt22Type(self, ctx:MT22Parser.Mt22TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensionArray.
    def visitDimensionArray(self, ctx:MT22Parser.DimensionArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensionsArrayPrime.
    def visitDimensionsArrayPrime(self, ctx:MT22Parser.DimensionsArrayPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignStatement.
    def visitAssignStatement(self, ctx:MT22Parser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#conditionStatement.
    def visitConditionStatement(self, ctx:MT22Parser.ConditionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStatement.
    def visitForStatement(self, ctx:MT22Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalarVariable.
    def visitScalarVariable(self, ctx:MT22Parser.ScalarVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStatement.
    def visitWhileStatement(self, ctx:MT22Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_whileStatement.
    def visitDo_whileStatement(self, ctx:MT22Parser.Do_whileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStatement.
    def visitContinueStatement(self, ctx:MT22Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStatement.
    def visitReturnStatement(self, ctx:MT22Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStatement.
    def visitBreakStatement(self, ctx:MT22Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStatement.
    def visitBlockStatement(self, ctx:MT22Parser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStatementPrime.
    def visitBlockStatementPrime(self, ctx:MT22Parser.BlockStatementPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStatement.
    def visitCallStatement(self, ctx:MT22Parser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifierList.
    def visitIdentifierList(self, ctx:MT22Parser.IdentifierListContext):
        return self.visitChildren(ctx)



del MT22Parser