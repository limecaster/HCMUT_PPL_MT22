# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:BKOOLParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array.
    def visitArray(self, ctx:BKOOLParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexedArray.
    def visitIndexedArray(self, ctx:BKOOLParser.IndexedArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexedArrayPrime.
    def visitIndexedArrayPrime(self, ctx:BKOOLParser.IndexedArrayPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#associativeArray.
    def visitAssociativeArray(self, ctx:BKOOLParser.AssociativeArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#associativeArrayPrime.
    def visitAssociativeArrayPrime(self, ctx:BKOOLParser.AssociativeArrayPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#associativePair.
    def visitAssociativePair(self, ctx:BKOOLParser.AssociativePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expression.
    def visitExpression(self, ctx:BKOOLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operand.
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        return self.visitChildren(ctx)



del BKOOLParser