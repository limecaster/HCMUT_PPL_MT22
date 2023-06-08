from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([y for x in ctx.declaration() for y in self.visit(x)])

    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx: MT22Parser.DeclarationContext):
        if ctx.variableDeclaration():
            return self.visit(ctx.variableDeclaration())
        elif ctx.functionDeclaration():
            return self.visit(ctx.functionDeclaration())

    # functionDeclaration: functionPrototype functionBody;

    def visitFunctionDeclaration(self, ctx: MT22Parser.FunctionDeclarationContext):
        lst = self.visit(ctx.functionPrototype())
        name = lst[0]
        returntype = lst[1]
        params = lst[2]
        inherit = ""
        if len(lst) == 4:
            inherit = lst[3]
        blkstmt = self.visit(ctx.blockStatement())
        return [FuncDecl(name, returntype, params, inherit, blkstmt)]

    # functionPrototype:  Identifier Colon Function type LeftParen parameterList RightParen
    #                   | Identifier Colon Function type LeftParen parameterList RightParen Inherit Identifier;
    def visitFunctionPrototype(self, ctx: MT22Parser.FunctionPrototypeContext):
        FuncPrt = []
        if ctx.getChildCount() == 7:
            FuncPrt.append(ctx.getChild(0).getText())
            FuncPrt.append(self.visit(ctx.getChild(3)))
            FuncPrt.append(self.visit(ctx.getChild(5)))
        else:
            FuncPrt.append(ctx.getChild(0).getText())
            FuncPrt.append(self.visit(ctx.getChild(3)))
            FuncPrt.append(self.visit(ctx.getChild(5)))
            FuncPrt.append(ctx.getChild(8).getText())
        return FuncPrt

    # parameterList: parameterListPrime | ;
    def visitParameterList(self, ctx: MT22Parser.ParameterListContext):
        if ctx.getChildCount() == 1:
            return [x for x in self.visit(ctx.parameterListPrime())]
        return []

    # parameterListPrime:  parameterDeclarion Comma parameterListPrime
    #          | parameterDeclarion;
    def visitParameterListPrime(self, ctx: MT22Parser.ParameterListPrimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameterDeclarion())]
        return [self.visit(ctx.parameterDeclarion())] + self.visit(ctx.parameterListPrime())

    # parameterDeclarion: Identifier Colon type
    #              | Out Identifier Colon type
    #              | Inherit Identifier Colon type
    #              | Inherit Out Identifier Colon type;
    def visitParameterDeclarion(self, ctx: MT22Parser.ParameterDeclarionContext):
        if ctx.getChildCount() == 3:
            return ParamDecl(ctx.Identifier().getText(), self.visit(ctx.mt22Type()), False, False)
        elif ctx.getChildCount() == 4:
            if ctx.getChild(0) == ctx.Out():
                return ParamDecl(ctx.Identifier().getText(), self.visit(ctx.mt22Type()), True, False)
            elif ctx.getChild(0) == ctx.Inherit():
                return ParamDecl(ctx.Identifier().getText(), self.visit(ctx.mt22Type()), False, True)
        else:
            return ParamDecl(ctx.Identifier().getText(), self.visit(ctx.mt22Type()), True, True)
    # variableDeclaration: varDeclShortForm | arrayDeclaration | arrayDeclaration;

    def visitVariableDeclaration(self, ctx: MT22Parser.VariableDeclarationContext):
        if ctx.varDeclShortForm():
            return self.visit(ctx.varDeclShortForm())
        elif ctx.arrayDeclaration():
            return self.visit(ctx.arrayDeclaration())
        else:
            VarDeclLst = self.visit(ctx.varDeclFullForm())
            # [id(0), exp(end), id(1), exp(end-1),..., id(end), exp(0), type]
            type = VarDeclLst.pop()
            ids, exps = [], []
            while len(VarDeclLst) > 0:
                exps.append(VarDeclLst.pop())
                ids.insert(0, VarDeclLst.pop())

            res = []
            for x in range(len(ids)):
                res.append(VarDecl(ids[x], type, exps[x]))

            return res

    # varDeclShortForm:  identifierList Colon type;
    def visitVarDeclShortForm(self, ctx: MT22Parser.VarDeclShortFormContext):
        res = []
        ids = self.visit(ctx.identifierList())
        type_ = self.visit(ctx.mt22Type())
        for x in range(len(ids)):
            res.append(VarDecl(ids[x], type_))
        return res

    # varDeclFullForm:  Identifier Comma varDeclFullForm Comma expression
    #            | Identifier Colon type Assign expression;

    def visitVarDeclFullForm(self, ctx: MT22Parser.VarDeclFullFormContext):
        if ctx.getChild(1) is ctx.Colon():
            return [ctx.Identifier().getText(), self.visit(ctx.expression()), self.visit(ctx.mt22Type())]

        return [ctx.Identifier().getText(), self.visit(ctx.expression())] + self.visit(ctx.varDeclFullForm())

    # arrayDeclaration: arrayDeclShortForm | arrayDeclFullForm;

    def visitArrayDeclaration(self, ctx: MT22Parser.ArrayDeclarationContext):
        if ctx.arrayDeclShortForm():
            return self.visit(ctx.arrayDeclShortForm())
        else:
            VarDeclLst = self.visit(ctx.arrayDeclFullForm())
            # [id(0), exp(end), id(1), exp(end-1),..., id(end), exp(0), type]
            type = VarDeclLst.pop()
            ids, exps = [], []
            while len(VarDeclLst) > 0:
                exps.append(VarDeclLst.pop())
                ids.insert(0, VarDeclLst.pop())

            res = []
            for x in range(len(ids)):
                res.append(VarDecl(ids[x], type, exps[x]))

            return res

    # arrayDeclShortForm: identifierList Colon Array dimensionArray Of atomicType;
    def visitArrayDeclShortForm(self, ctx: MT22Parser.ArrayDeclShortFormContext):
        name = self.visit(ctx.identifierList())
        type = ArrayType(self.visit(ctx.dimensionArray()),
                         self.visit(ctx.atomicType()))
        return [VarDecl(x, type, ) for x in name]

    #  arrayDeclFullForm:    Identifier Comma arrayDeclFullForm Comma expression
    #               |  Identifier Colon Array dimensionArray Of mt22Type Assign expression;

    def visitArrayDeclFullForm(self, ctx: MT22Parser.ArrayDeclFullFormContext):
        if ctx.getChild(1) is ctx.Colon():
            return [ctx.Identifier().getText(), self.visit(ctx.expression()),
                    ArrayType(self.visit(ctx.dimensionArray()), self.visit(ctx.atomicType()))]

        return [ctx.Identifier().getText(), self.visit(ctx.expression())] + self.visit(ctx.arrayDeclFullForm())

    # expression: LeftParen expression RightParen
    #        | indexedExpression
    #        | Minus expression
    #        | Not expression
    #        | expression multiplyOperator expression
    #        | expression addingOperator expression
    #        | expression booleanOperator expression
    #        | expression relationalOperator expression
    #        | expression stringOperator expression
    #        | operand
    #        ;

    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        if ctx.getChildCount() == 2:
            if ctx.getChild(0) is ctx.Minus():
                return UnExpr(ctx.Minus().getText(), self.visit(ctx.getChild(1)))
            elif ctx.getChild(0) is ctx.Not():
                return UnExpr(ctx.Not().getText(), self.visit(ctx.getChild(1)))
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0) is ctx.LeftParen():
                return self.visit(ctx.getChild(1))
            elif ctx.getChild(1) is ctx.multiplyOperator():
                return BinExpr(self.visit(ctx.multiplyOperator()), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            elif ctx.getChild(1) is ctx.addingOperator():
                return BinExpr(self.visit(ctx.addingOperator()), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            elif ctx.getChild(1) is ctx.booleanOperator():
                return BinExpr(self.visit(ctx.booleanOperator()), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            elif ctx.getChild(1) is ctx.relationalOperator():
                return BinExpr(self.visit(ctx.relationalOperator()), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
            elif ctx.getChild(1) is ctx.stringOperator():
                return BinExpr(self.visit(ctx.stringOperator()), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        elif ctx.getChildCount() == 1:
            if ctx.getChild(0) is ctx.indexedExpression():
                return self.visit(ctx.indexedExpression())
            return self.visit(ctx.operand())

    # expressionList: expression Comma expressionList
    #          | expression;
    def visitExpressionList(self, ctx: MT22Parser.ExpressionListContext):
        if ctx.getChildCount() == 1:
            if self.visit(ctx.expression()) is None:
                return []
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.expressionList())

    # indexedExpression:  Identifier indexedOperator;
    def visitIndexedExpression(self, ctx: MT22Parser.IndexedExpressionContext):
        return ArrayCell((ctx.Identifier().getText()), self.visit(ctx.indexedOperator()))

    # indexedOperator:  LeftBracket expressionList RightBracket;
    def visitIndexedOperator(self, ctx: MT22Parser.IndexedOperatorContext):
        return self.visit(ctx.expressionList())

    # functionCall: Identifier LeftParen expressionList RightParen
    #        | Identifier LeftParen RightParen;
    def visitFunctionCall(self, ctx: MT22Parser.FunctionCallContext):
        if ctx.getChildCount() == 3:
            return FuncCall((ctx.Identifier().getText()), [])
        return FuncCall((ctx.Identifier().getText()), self.visit(ctx.expressionList()))

    # operand:  literal
    #    | Identifier
    #    | functionCall
    #    ;
    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        return Id(ctx.Identifier().getText())

    # booleanOperator:  AndAnd | OrOr;
    def visitBooleanOperator(self, ctx: MT22Parser.BooleanOperatorContext):
        if ctx.AndAnd():
            return ctx.AndAnd().getText()
        return ctx.OrOr().getText()

    # relationalOperator: Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual;.
    def visitRelationalOperator(self, ctx: MT22Parser.RelationalOperatorContext):
        if ctx.Equal():
            return ctx.Equal().getText()
        elif ctx.NotEqual():
            return ctx.NotEqual().getText()
        elif ctx.Less():
            return ctx.Less().getText()
        elif ctx.Greater():
            return ctx.Greater().getText()
        elif ctx.LessEqual():
            return ctx.LessEqual().getText()
        return ctx.GreaterEqual().getText()

    # multiplyOperator: Star | Div | Mod;
    def visitMultiplyOperator(self, ctx: MT22Parser.MultiplyOperatorContext):
        if ctx.Star():
            return ctx.Star().getText()
        elif ctx.Div():
            return ctx.Div().getText()
        return ctx.Mod().getText()

    # addingOperator: Plus | Minus;
    def visitAddingOperator(self, ctx: MT22Parser.AddingOperatorContext):
        if ctx.Plus():
            return ctx.Plus().getText()
        return ctx.Minus().getText()

    # stringOperator: Doublecolon;
    def visitStringOperator(self, ctx: MT22Parser.StringOperatorContext):
        return ctx.Doublecolon().getText()

    # arrayLiteral: LeftBrace expressionList RightBrace;

    def visitArrayLiteral(self, ctx: MT22Parser.ArrayLiteralContext):
        return ArrayLit(self.visit(ctx.expressionList()))

    # mt22type: atomicType | Void | Auto | Array;
    def visitMt22Type(self, ctx: MT22Parser.Mt22TypeContext):
        if ctx.Void():
            return VoidType()
        if ctx.Auto():
            return AutoType()
        if ctx.Array():
            return ArrayType(self.visit(ctx.dimensionArray()), self.visit(ctx.atomicType()))
        return self.visit(ctx.atomicType())

    def visitAtomicType(self, ctx: MT22Parser.AtomicTypeContext):
        if ctx.Integer():
            return IntegerType()
        if ctx.Float():
            return FloatType()
        if ctx.String():
            return StringType()
        if ctx.Boolean():
            return BooleanType()

    # dimensionArray: LeftBracket dimensionsArrayPrime RightBracket;
    def visitDimensionArray(self, ctx: MT22Parser.DimensionArrayContext):
        return self.visit(ctx.dimensionsArrayPrime())

    # dimensionsArrayPrime: IntegerLiteral Comma dimensionsArrayPrime
    #                | IntegerLiteral;.
    def visitDimensionsArrayPrime(self, ctx: MT22Parser.DimensionsArrayPrimeContext):
        if ctx.getChildCount() == 1:
            return [(ctx.IntegerLiteral().getText())]
        return [(ctx.IntegerLiteral().getText())] + self.visit(ctx.dimensionsArrayPrime())

    # literal:  StringLiteral
    #    | IntegerLiteral
    #    | FloatLiteral
    #    | BooleanLiteral
    #    | arrayLiteral
    #    ;
    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if ctx.StringLiteral():
            return StringLit(ctx.StringLiteral().getText())
        elif ctx.FloatLiteral():
            val = str(ctx.FloatLiteral().getText())
            if val[0] == '.':
                val = ''.join(('0', val))
            return FloatLit(float(("%.17f" % float(val)).rstrip('0').rstrip('.')))
        elif ctx.IntegerLiteral():
            return IntegerLit(ctx.IntegerLiteral().getText())
        elif ctx.BooleanLiteral():
            return BooleanLit(ctx.BooleanLiteral().getText())
        return self.visit(ctx.arrayLiteral())

    # statement:    assignStatement
    #        | conditionStatement
    #        | forStatement
    #        | whileStatement
    #        | do_whileStatement
    #        | breakStatement
    #        | continueStatement
    #        | returnStatement
    #        | callStatement
    #        | blockStatement
    #        ;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.assignStatement():
            return self.visit(ctx.assignStatement())
        elif ctx.conditionStatement():
            return self.visit(ctx.conditionStatement())
        elif ctx.forStatement():
            return self.visit(ctx.forStatement())
        elif ctx.whileStatement():
            return self.visit(ctx.whileStatement())
        elif ctx.do_whileStatement():
            return self.visit(ctx.do_whileStatement())
        elif ctx.breakStatement():
            return self.visit(ctx.breakStatement())
        elif ctx.continueStatement():
            return self.visit(ctx.continueStatement())
        elif ctx.returnStatement():
            return self.visit(ctx.returnStatement())
        elif ctx.callStatement():
            return self.visit(ctx.callStatement())
        elif ctx.blockStatement():
            return self.visit(ctx.blockStatement())

    # assignStatement:  scalarVariable Assign expression Semicolon;
    def visitAssignStatement(self, ctx: MT22Parser.AssignStatementContext):
        return AssignStmt(self.visit(ctx.scalarVariable()), self.visit(ctx.expression()))

    # conditionStatement: If LeftParen expression RightParen statement
    #              | If LeftParen expression RightParen statement Else statement;
    def visitConditionStatement(self, ctx: MT22Parser.ConditionStatementContext):
        if ctx.getChildCount() == 5:
            return IfStmt(self.visit(ctx.expression()), self.visit(ctx.getChild(4)))
        return IfStmt(self.visit(ctx.expression()), self.visit(ctx.getChild(4)), self.visit(ctx.getChild(6)))

    # forStatement: For LeftParen scalarVariable Assign expression
    #          Comma expression Comma expression RightParen
    #          statement;

    def visitForStatement(self, ctx: MT22Parser.ForStatementContext):
        init = AssignStmt(self.visit(ctx.getChild(2)),
                          self.visit(ctx.getChild(4)))
        cond = self.visit(ctx.getChild(6))
        upcond = self.visit(ctx.getChild(8))
        stmt = self.visit(ctx.getChild(10))
        return ForStmt(init, cond, upcond, stmt)

    # scalarVariable: Identifier | indexedExpression;
    def visitScalarVariable(self, ctx: MT22Parser.ScalarVariableContext):
        if ctx.Identifier():
            return Id(ctx.Identifier().getText())
        return self.visit(ctx.indexedExpression())

    # whileStatement: While LeftParen expression RightParen statement;
    def visitWhileStatement(self, ctx: MT22Parser.WhileStatementContext):
        return WhileStmt(self.visit(ctx.expression()), self.visit(ctx.statement()))

    # do_whileStatement:  Do blockStatement While LeftParen expression RightParen Semicolon;
    def visitDo_whileStatement(self, ctx: MT22Parser.Do_whileStatementContext):
        return DoWhileStmt(self.visit(ctx.blockStatement()), self.visit(ctx.expression()))

    # Visit a parse tree produced by MT22Parser#continueStatement.
    def visitContinueStatement(self, ctx: MT22Parser.ContinueStatementContext):
        return ContinueStmt()

    # returnStatement:  Return Semicolon
    #            | Return expression Semicolon;
    def visitReturnStatement(self, ctx: MT22Parser.ReturnStatementContext):
        if ctx.getChildCount() == 2:
            return ReturnStmt()
        return ReturnStmt(self.visit(ctx.expression()))

    # Visit a parse tree produced by MT22Parser#breakStatement.
    def visitBreakStatement(self, ctx: MT22Parser.BreakStatementContext):
        return BreakStmt()

    # blockStatement: LeftBrace blockStatementPrime RightBrace
    #          | LeftBrace RightBrace;
    def visitBlockStatement(self, ctx: MT22Parser.BlockStatementContext):
        return BlockStmt(self.visit(ctx.blockStatementPrime())) if ctx.getChildCount() == 3 else BlockStmt([])

    # blockStatementPrime:  statement blockStatementPrime
    #                | variableDeclaration blockStatementPrime
    #                | statement
    #                | variableDeclaration;
    def visitBlockStatementPrime(self, ctx: MT22Parser.BlockStatementPrimeContext):
        if ctx.getChildCount() == 1:
            if ctx.statement():
                return [self.visit(ctx.statement())]
            elif ctx.variableDeclaration():
                return self.visit(ctx.variableDeclaration())
        else:
            if ctx.getChild(0) is ctx.statement():
                return [self.visit(ctx.getChild(0))] + self.visit(ctx.getChild(1))
            elif ctx.getChild(0) is ctx.variableDeclaration():
                return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(1))

    # callStatement:  functionCall Semicolon;
    def visitCallStatement(self, ctx: MT22Parser.CallStatementContext):
        return CallStmt(self.visit(ctx.functionCall()).name, self.visit(ctx.functionCall()).args)

    # identifierList: Identifier Comma identifierList
    #               | Identifier;

    def visitIdentifierList(self, ctx: MT22Parser.IdentifierListContext):
        if ctx.getChildCount() == 1:
            return [(ctx.Identifier().getText())]
        return [(ctx.Identifier().getText())] + self.visit(ctx.identifierList())
