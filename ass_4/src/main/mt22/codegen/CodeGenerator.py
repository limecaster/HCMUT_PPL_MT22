from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *
from CodeGenError import *


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class ArrayPointerType(Type):
    def __init__(self, finfo):
        # cname: String
        self.eleType = finfo

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym, isGlobal=False):
        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal

    def __str__(self):
        return "SubBody(" + str(self.frame) + ", " + str(self.sym) + ")"


class Access():
    def __init__(self, frame, sym, isLeft=False, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, init=None, isGlobal=True):
        self.name = name
        self.isGlobal = isGlobal
        self.value = value
        self.init = init
        self.mtype = mtype

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class FunctionPrototype:
    # FunctionPrototype contains info function prototype
    # FunctionPrototype(Id name, Id type/return type,
    #       params = List of ParamPrototype, inherit = name of father func)
    def __init__(self, name_: str, type_: Type, params: list or None, inherit: str or None):
        self.name_ = name_
        self.type_ = type_
        self.inherit = inherit
        self.params = params


class ParamPrototype:
    def __init__(self, name_: str, type_: Type, out_: bool, inherit_: bool):
        self.name_ = name_
        self.type_ = type_
        self.out_ = out_
        self.inherit_ = inherit_


class VarPrototype:
    def __init__(self, name_: str, type_: Type):
        self.name_ = name_
        self.type_ = type_


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType([], IntegerType()), CName(self.libName)),
                Symbol("readFloat", MType([], FloatType()),
                       CName(self.libName)),
                Symbol("readBoolean", MType(
                    [], BooleanType()), CName(self.libName)),
                Symbol("readString", MType(
                    [], StringType()), CName(self.libName)),
                Symbol("printInteger", MType(
                    [IntegerType()], VoidType()), CName(self.libName)),
                Symbol("printFloat", MType(
                    [FloatType()], VoidType()), CName(self.libName)),
                Symbol("printBoolean", MType(
                    [BooleanType()], VoidType()), CName(self.libName)),
                Symbol("printString", MType(
                    [StringType()], VoidType()), CName(self.libName)),
                Symbol("super", MType(list(), VoidType()), CName(self.libName)),
                Symbol("preventDefault", MType(
                    [], VoidType()), CName(self.libName)),
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        typeinfer = TypeInferred(ast, gl).check()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class FindReturnStmt:
    def __init__(self, ctx):
        self.ctx = ctx

    def visit(self, ast, param):
        return ast.accept(self, param)

    def find(self):
        # Return ctx if there is a break/continue stmt in stmt
        flag = []
        flag = self.visit(self.ctx, flag)
        return flag

    def visitBlockStmt(self, ctx: BlockStmt, o: object):
        # body: List[Stmt or VarDecl]
        for stmt in ctx.body:
            if type(stmt) is ReturnStmt:
                o += [stmt]
            else:
                o = self.visit(stmt, o)

        return o

    def visitIfStmt(self, ctx: IfStmt, o: object):
        # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
        o = self.visit(ctx.tstmt, o)
        if ctx.fstmt is not None:
            o = self.visit(ctx.fstmt, o)

        return o

    def visitForStmt(self, ctx: ForStmt, o: object):
        o = self.visit(ctx.stmt, o)
        return o

    def visitWhileStmt(self, ctx: WhileStmt, o: object):
        o = self.visit(ctx.stmt, o)
        return o

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o: object):
        o = self.visit(ctx.stmt, o)
        return o

    def visitVarDecl(self, ctx, o):
        return o

    def visitCallStmt(self, ctx, o):
        return o

    def visitAssignStmt(self, ctx, o):
        return o

    def visitReturnStmt(self, ctx, o):
        return o

    def visitBreakStmt(self, ctx: BreakStmt, o: object):
        return o

    def visitContinueStmt(self, ctx: ContinueStmt, o: object):
        return o


class PreTraversal(Visitor):
    # PreTraversal has a mission that collect all function prototype and global vardecl
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, None)

    def visitProgram(self, ctx: Program, o: object):
        o = []
        for decl in ctx.decls:
            o = self.visit(decl, o)
        return o

    def visitVarDecl(self, ctx: VarDecl, o: object):
        # name: str, typ: Type, init: Expr or None = None
        o += [VarPrototype(ctx.name, ctx.typ)]
        return o

    def visitParamDecl(self, ctx: ParamDecl, o: object):
        # name: str, typ: Type, out: bool = False, inherit: bool = False
        # It's useless
        return o

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt

        if len(ctx.params) == 0:
            paramdecl = []
        else:
            paramdecl = []
            for pdecl in ctx.params:
                paramdecl += [ParamPrototype(pdecl.name,
                                             pdecl.typ, pdecl.out, pdecl.inherit)]

        o += [FunctionPrototype(ctx.name, ctx.return_type, paramdecl, ctx.inherit)]
        return o


class TypeInferred(Visitor):

    def __init__(self, astTree, env):
        self.astTree = astTree
        self.env = env

    def check(self):
        return self.visitProgram(self.astTree, None)

    def visitProgram(self, ctx: Program, o: object):
        o = PreTraversal(self.astTree).check()
        # In PreTraversal, we get info of all global decl and store in o
        funcdecls = []
        for fdecl in o:
            funcdecls += [fdecl]

        # env[0] = local env, env[-1] = global env, else is nonlocal
        env = [[]] + [o]
        for decl in ctx.decls:
            env = self.visit(decl, env)

    def visitVarDecl(self, ctx: VarDecl, o: object):
        # name: str, typ: Type, init: Expr or None = None

        # Check redeclared if redeclared in env of vardecl
        varinfo = VarPrototype(ctx.name, ctx.typ)
        # Raise Invalid: <variable name> if AutoType and init is None
        if type(varinfo.type_) is AutoType:
            varinfo.type_ = self.visit(ctx.init, o)
            ctx.typ = varinfo.type_

        init_type = self.visit(ctx.init, o) if ctx.init is not None else None
        if type(varinfo.type_) is FloatType and type(init_type) is IntegerType:
            varinfo.type_ = FloatType()
        elif type(varinfo.type_) is ArrayType and type(init_type) is ArrayType:
            decl_atomicType = varinfo.type_.typ
            init_atomicType = init_type.typ

            if type(decl_atomicType) == AutoType:
                decl_atomicType = init_atomicType
                varinfo.type_.typ = init_atomicType
                ctx.typ = varinfo.type_

        elif type(init_type) == AutoType:
            if type(ctx.init) in [FuncCall, CallStmt]:
                self.infer(ctx.init, o, ctx.typ)
            if type(ctx.init) is UnExpr:
                if type(ctx.init.val) in [FuncCall, CallStmt]:
                    self.infer(ctx.init.val, o, ctx.typ)
        # varinfo.type_ = init_type if init_type is not None else varinfo.type_
        o[0] += [varinfo]

        return o

    def visitParamDecl(self, ctx: ParamDecl, o: object):
        # name: str, typ: Type, out: bool = False, inherit: bool = False
        # It's useless
        return ctx.name

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
        # Check redeclared func
        childParam = []

        env = [[]] + o
        
        childParam = [ParamPrototype(
            x.name, x.typ, x.out, x.inherit) for x in ctx.params]

        # If this is child function
        if ctx.inherit is not None:
            # If child function inherit non-declared father function, raise Undeclared Function
            for fdecl in env[-1]:
                if fdecl.name_ == ctx.inherit:
                    break

            # Else, get father params
            fatherParams = list(filter(lambda x: x.name_ == ctx.inherit and type(
                x) == FunctionPrototype, env[-1]))[0].params
            # Get father params with inherit keyword
            fatherParams = list(
                filter(lambda x: x.inherit_ == True, fatherParams))

        # After all, we append childparam as local VarPrototype of childFunction
        env[0] += childParam

        self.visit(ctx.body, env)

        # Find return stmt
        indoorReturnStmt = []  # ReturnStmt that lay in another stmt else this blockstmt

        outdoorReturnStmt = []  # ReturnStmt that lay directly in this blockstmt
        hasReturnStmts = []
        returnTyp = None
        func_info = None
        for stmt in ctx.body.body:
            if type(stmt) is ReturnStmt:
                returnTyp = self.visit(stmt, env)
                outdoorReturnStmt = [stmt]
                # We only need to check first outdoor returnstmt,
                # another with same kind but lay after the first is pass by
                break
        for stmt in ctx.body.body:
            if type(stmt) is not ReturnStmt:
                indoorReturnStmt = FindReturnStmt(stmt).find()
                # Find all returnstmt that lay in another stmt that is not this blockstmt
                # Each of them must be check type

        # This procedure to get 2 kinds of returnstmt in this blockstmt, store in hasReturnStmts.
        # returnTyp is the type of firstly seen returnstmt
        if len(outdoorReturnStmt) == 0:
            if len(indoorReturnStmt) == 0:
                hasReturnStmts = []
            else:
                returnTyp = self.visit(indoorReturnStmt[0], env)
                hasReturnStmts = indoorReturnStmt
        else:
            if len(indoorReturnStmt) == 0:
                hasReturnStmts = outdoorReturnStmt
            else:
                firstReturnStmt = FindReturnStmt(ctx.body).find()[0]
                returnTyp = self.visit(firstReturnStmt, env)
                hasReturnStmts = outdoorReturnStmt + indoorReturnStmt

        # Find func_info in env[-1]
        for decl in env[-1]:
            if decl.name_ == ctx.name:
                func_info = decl

        if len(hasReturnStmts) > 0:
            for hasReturnStmt in hasReturnStmts:
                # Type inferring
                if hasReturnStmt.expr is None:
                    if type(func_info.type_) == AutoType:
                        func_info.type_ = VoidType()
                        ctx.return_type = VoidType()
                elif type(hasReturnStmt.expr) in [FuncCall, CallStmt]:
                    if type(returnTyp) is AutoType:
                        # Then infer type of Id in expr with return type of function
                        for envi in env:
                            for decl in envi:
                                # return expr is AutoType, so it is Id, or FuncCall/CallStmt,
                                # all of them have .name field
                                if decl.name_ == hasReturnStmt.expr.name and type(decl.type_) == AutoType:
                                    decl.type_ = func_info.type_
                    # If type of function is Auto and returntype is not None, then infer its type to returntype
                    if type(func_info.type_) == AutoType or type(ctx.return_type) == AutoType:
                        func_info.type_ = returnTyp
                        ctx.return_type = returnTyp
                elif type(hasReturnStmt.expr) is Id:
                    if type(func_info.type_) == AutoType or type(ctx.return_type) == AutoType:
                        func_info.type_ = returnTyp
                        ctx.return_type = returnTyp
                        
                else:
                    # return expr is Literal/binexpr/unexpr => value
                    if type(func_info.type_) == AutoType or type(ctx.return_type) == AutoType:
                        func_info.type_ = returnTyp
                        ctx.return_type = returnTyp

        return o

    def visitAssignStmt(self, ctx: AssignStmt, o: object):
        # lhs: LHS (Id or ArrayCell), rhs: Expr
        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)
        if type(left) == AutoType:
            for decl in o[-1]:
                if left.name == decl.name_:
                    decl.type_ = right
        if type(right) == AutoType:
            for decl in o[-1]:
                if left.name == decl.name_:
                    decl.type_ = left

        left = self.visit(ctx.lhs, o)
        right = self.visit(ctx.rhs, o)

    def visitBlockStmt(self, ctx: BlockStmt, o: object):
        # body: List[Stmt or VarDecl]
        if len(ctx.body) > 0:
            for stmt in ctx.body:
                if type(stmt) is not ReturnStmt:
                    # Cause we check returnstmt in funcdecl
                    self.visit(stmt, o)

    def visitIfStmt(self, ctx: IfStmt, o: object):
        # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
        if type(ctx.tstmt) is BlockStmt:
            env = [[]] + o
            self.visit(ctx.tstmt, env)
        else:
            self.visit(ctx.tstmt, o)
        if ctx.fstmt is not None:
            if type(ctx.fstmt) is BlockStmt:
                env = [[]] + o
                self.visit(ctx.fstmt, env)
            else:
                self.visit(ctx.fstmt, o)

    def visitForStmt(self, ctx: ForStmt, o: object):
        # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
        if type(ctx.stmt) is BlockStmt:
            env = [[]] + o
            self.visit(ctx.stmt, env)
        else:
            self.visit(ctx.stmt, o)

    def visitWhileStmt(self, ctx: WhileStmt, o: object):
        # cond: Expr, stmt: Stmt
        if type(ctx.stmt) is BlockStmt:
            env = [[]] + o
            self.visit(ctx.stmt, env)
        else:
            self.visit(ctx.stmt, o)

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o: object):
        # cond: Expr, stmt: BlockStmt

        env = [[]] + o
        self.visit(ctx.stmt, env)

    def visitBreakStmt(self, ctx: BreakStmt, o: object): pass

    def visitContinueStmt(self, ctx: ContinueStmt, o: object): pass

    def visitReturnStmt(self, ctx: ReturnStmt, o: object):
        # expr: Expr or None = None
        return self.visit(ctx.expr, o) if ctx.expr is not None else VoidType()

    def visitCallStmt(self, ctx: CallStmt, o: object):
        # name: str, args: List[Expr]
        # Raise Undeclared if Function not declared in o[-1]
        isDeclared = False
        func_info = None
        for func_info in o[-1]:
            if type(func_info) == FunctionPrototype:
                if func_info.name_ == ctx.name:
                    break

        if ctx.name in ['printInteger', 'printFloat', 'printBoolean', 'printString']:
            arguTyp = self.visit(ctx.args[0], o)
            if ctx.name == 'printInteger':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, IntegerType())
            if ctx.name == 'printFloat':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, FloatType())
            if ctx.name == 'printBoolean':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, BooleanType())
            if ctx.name == 'printString':
                if type(arguTyp) == AutoType:
                    self.infer(ctx.args[0], o, StringType())
            # To do, check type binding and coercion of dafault function
        elif ctx.name == 'super':
            pass
        else:
            for i in range(len(ctx.args)):
                argTyp = type(self.visit(ctx.args[i], o))
                paramTyp = type(func_info.params[i].type_)
                if argTyp == AutoType:
                    argTyp = paramTyp
                    ctx.args[i].typ = paramTyp
                if paramTyp == AutoType:
                    func_info.type_ = argTyp
                    for globaldecl in self.astTree.decls:
                        if type(globaldecl) is FuncDecl and globaldecl.name == ctx.name:
                            globaldecl.params[i].typ = argTyp
                    paramTyp = argTyp
        return VoidType()

    def visitFuncCall(self, ctx: FuncCall, o: object):
        # name: str, args: List[Expr]
        # Raise Undeclared if Function not declared in o[-1]
        func_info = None
        returnTyp = None
        for func_info in o[-1]:
            if func_info.name_ == ctx.name:
                returnTyp = func_info.type_
                break

        if ctx.name in ['readInteger', 'readFloat', 'readBoolean', 'readString']:
            if ctx.name == 'readInteger':
                returnTyp = IntegerType()
            if ctx.name == 'readFloat':
                returnTyp = FloatType()
            if ctx.name == 'readBoolean':
                returnTyp = BooleanType()
            if ctx.name == 'readString':
                returnTyp = StringType()
        else:
            for i in range(len(ctx.args)):
                argTyp = self.visit(ctx.args[i], o)
                paramTyp = func_info.params[i].type_
                if type(argTyp) == AutoType:
                    argTyp = paramTyp
                    ctx.args[i].typ = paramTyp
                if type(paramTyp) == AutoType:
                    for globaldecl in self.astTree.decls:
                        if type(globaldecl) is FuncDecl and globaldecl.name == ctx.name:
                            globaldecl.params[i].typ = argTyp
                    paramTyp = argTyp

        return returnTyp

    def infer(self, ctx, o, targetType):
        for env in o:
            for decl in env:
                if decl.name_ == ctx.name and type(decl.type_) == AutoType:
                    decl.type_ = targetType

    def visitBinExpr(self, ctx: BinExpr, o: object):
        # op: str, left: Expr, right: Expr
        exp_1 = self.visit(ctx.left, o)
        exp_2 = self.visit(ctx.right, o)
        returnTyp = BooleanType()
        if type(exp_1) == type(exp_2):
            returnTyp = exp_1
        if ctx.op in ['+', '-', '*', '/']:
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, exp_2)
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, exp_1)
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) == IntegerType and type(exp_2) == IntegerType:
                returnTyp = FloatType() if ctx.op == '/' else IntegerType()
            elif type(exp_1) in [IntegerType, FloatType] and type(exp_2) in [IntegerType, FloatType]:
                returnTyp = FloatType()

        if ctx.op == '%':
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, IntegerType())
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, IntegerType())
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) == IntegerType and type(exp_2) == IntegerType:
                returnTyp = IntegerType()

        if ctx.op in ['&&', '||']:
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, exp_2)
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, exp_1)
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) in [BooleanType, IntegerType] and type(exp_2) in [BooleanType, IntegerType]:
                returnTyp = BooleanType()

        if ctx.op == '::':
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, StringType())
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, StringType())
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) == StringType and type(exp_2) == StringType:
                returnTyp = StringType()

        if ctx.op in ['>', '>=', '<', '<=', '==', '!=']:
            if type(exp_1) == AutoType:
                self.infer(ctx.left, o, exp_2)
            if type(exp_2) == AutoType:
                self.infer(ctx.right, o, exp_1)
            exp_1 = self.visit(ctx.left, o)
            exp_2 = self.visit(ctx.right, o)
            if type(exp_1) in [IntegerType, FloatType] and type(exp_2) in [IntegerType, FloatType]:
                returnTyp = BooleanType()

        return returnTyp

    def visitUnExpr(self, ctx: UnExpr, o: object):
        # op: str, val: Expr
        returnTyp = BooleanType()
        exp = self.visit(ctx.val, o)
        if ctx.op == '!':
            if type(exp) == AutoType:
                self.infer(ctx.val, o, BooleanType())
                exp = self.visit(ctx.val, o)
            if type(exp) == BooleanType:
                returnTyp = BooleanType()

        if ctx.op == '-':
            if type(exp) == IntegerType:
                returnTyp = IntegerType()
            if type(exp) == FloatType:
                returnTyp = FloatType()
            if type(exp) == AutoType:
                returnTyp = AutoType()

        return returnTyp

    def visitId(self, ctx: Id, o: object):
        # name: str
        # Find in all env, if id name not appear in all env, raise Undeclared
        for env in o:
            for decl in env:
                if type(decl) in [VarPrototype, ParamPrototype]:
                    if decl.name_ == ctx.name:
                        return decl.type_

    def visitArrayCell(self, ctx: ArrayCell, o: object):
        # name: str, cell: List[Expr]

        idtyp = self.visit(Id(ctx.name), o)

        cellVal = []
        for exp in ctx.cell:
            e = self.visit(exp, o)
            if type(e) == AutoType:
                # If auto type funccall then infer to IntegerType
                for decl in o[-1]:
                    if exp.name == decl.name_ and decl.type_ == AutoType:
                        decl.type_ = IntegerType
            elif type(exp) is IntegerLit:
                cellVal += [int(exp.val)]
            elif type(e) == IntegerType:
                cellVal += [e]

        return idtyp.typ

    def visitArrayLit(self, ctx: ArrayLit, o: object):
        # explist: List[Expr]
        typeMatrix = []
        commonType = AutoType
        for exp in ctx.explist:
            eleTyp = self.visit(exp, o)
            if type(eleTyp) != AutoType:
                commonType = eleTyp
            typeMatrix += [eleTyp]

        for i in range(len(ctx.explist)):
            if type(typeMatrix[i]) == AutoType:
                # It must be function with auto type return
                for decl in o[-1]:
                    if decl.name_ == ctx.explist[i].name:
                        decl.type_ = commonType
                        typeMatrix[i] = commonType

        dimension = [len(ctx.explist)]

        if type(commonType) == ArrayType:
            resolutionArrayType = self.visit(ctx.explist[0], o)
            resolutionArrayType.dimensions = list(
                map(lambda x: int(x), resolutionArrayType.dimensions))
            dimension += resolutionArrayType.dimensions
            commonType = resolutionArrayType.typ

        return ArrayType(dimension, commonType)

    def visitIntegerLit(self, ctx: IntegerLit, o: object):
        return IntegerType()

    def visitFloatLit(self, ctx: FloatLit, o: object):
        return FloatType()

    def visitStringLit(self, ctx: StringLit, o: object):
        return StringType()

    def visitBooleanLit(self, ctx: BooleanLit, o: object):
        return BooleanType()


class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = "MT22Class"
        self.emit = Emitter(self.path + '/' + self.className + '.j')

    def visitProgram(self, ctx: Program, o):
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))

        staticDecl = self.env
        for decl in ctx.decls:
            if type(decl) is FuncDecl:
                partype = [i.typ for i in decl.params]
                staticDecl = [Symbol(decl.name, MType(
                    partype, decl.return_type), CName(self.className))] + staticDecl
            else:
                newSym = self.visit(decl, SubBody(None, None, True))
                staticDecl = [newSym] + staticDecl

        [self.visit(decl, SubBody(None, staticDecl))
         for decl in ctx.decls if type(decl) is FuncDecl]

        # generate default constructor
        self.genMETHOD(FuncDecl("<init>", VoidType(), list(), None, BlockStmt(
            [])), staticDecl, Frame("<init>", VoidType()))

        # class init - static field declare
        self.genMETHOD(FuncDecl("<clinit>", VoidType(), list(), None, BlockStmt(
            [])), staticDecl, Frame("<clinit>", VoidType()))

        self.emit.emitEPILOG()
        return

    def visitFuncDecl(self, ctx: FuncDecl, o):
        frame = Frame(ctx.name, ctx.return_type)
        o.sym += [Symbol(paramdecl.name, paramdecl.typ,
                         Index(frame.getNewIndex())) for paramdecl in ctx.params]
        self.genMETHOD(ctx, o.sym, frame)
        return Symbol(ctx.name, MType([x.typ for x in ctx.params], ctx.return_type), CName(self.className))

    def genMETHOD(self, Funcdecl: FuncDecl, o, frame):
        isInit = Funcdecl.name == "<init>"

        isMain = Funcdecl.name == "main" and len(Funcdecl.params) == 0 \
            and type(Funcdecl.return_type) is VoidType

        returnType = VoidType() if isInit else Funcdecl.return_type
        methodName = "<init>" if isInit else Funcdecl.name
        intype = [ArrayPointerType(StringType())] if isMain else list(
            map(lambda x: x.typ, Funcdecl.params))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(False)
        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(), "this",
                    ClassType(Id(self.className)),
                    frame.getStartLabel(), frame.getEndLabel(), frame)
            )
        elif isMain:
            self.emit.printout(
                self.emit.emitVAR(
                    frame.getNewIndex(), "args",
                    ArrayPointerType(StringType()),
                    frame.getStartLabel(), frame.getEndLabel(), frame)
            )
        # else:
        #     # If param has "inherit" keyword, it's as a field of function,
        #     # function as a class
        #     [self.emit.printout(
        #         self.emit.emitINSTANCEFIELD(
        #             Funcdecl.name + "/" + paramdecl.name,
        #             paramdecl.typ, frame)
        #         )
        #         for paramdecl in Funcdecl.params if paramdecl.inherit
        #     ]

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        if Funcdecl.name == "<clinit>":
            # Initialize global variable declare
            for vardecl in glenv:
                if type(vardecl.mtype) is not MType and vardecl.isGlobal:
                    if type(vardecl.mtype) is ArrayType:
                        if vardecl.init is None:
                            self.emit.printout(self.emit.emitInitNewArray(
                                self.className + "/" + vardecl.name,
                                vardecl.mtype.dimensions, vardecl.mtype.typ, frame, None)
                            )
                        else:
                            # Treat initialize a vảiable to arraylit
                            # as assignstmt of arraycell to each of value in arraylit

                            # Sorry for stupid method for generate init array code

                            dimension = list(
                                map(lambda x: int(x), vardecl.mtype.dimensions))
                            initList = self.ListOfList_to_List(vardecl.init)
                            if len(dimension) == 1:
                                initcode = [self.visit(exp, Access(frame, glenv))[
                                    0] for exp in initList]
                                initList = initcode

                            indexOfInit = 0
                            # Allocate memory for array
                            self.emit.printout(
                                self.emit.emitInitNewArray(
                                    self.className + "/" + vardecl.name,
                                    vardecl.mtype.dimensions,
                                    vardecl.mtype.typ, frame,
                                    initList, None
                                )
                            )

                            # If array is 2D
                            if len(dimension) == 2:
                                for i in range(dimension[0]):
                                    for j in range(dimension[1]):
                                        initAssignStmt = AssignStmt(
                                            ArrayCell(vardecl.name, [
                                                      IntegerLit(i), IntegerLit(j)]),
                                            initList[indexOfInit]
                                        )
                                        self.visit(initAssignStmt,
                                                   Access(frame, glenv))
                                        indexOfInit += 1

                            # If array is 3D
                            # Ehe
                            if len(dimension) == 3:
                                for i in range(dimension[0]):
                                    for j in range(dimension[1]):
                                        for k in range(dimension[2]):
                                            initAssignStmt = AssignStmt(
                                                ArrayCell(vardecl.name,
                                                          [IntegerLit(i), IntegerLit(j), IntegerLit(k)]),
                                                initList[indexOfInit]
                                            )
                                            self.visit(
                                                initAssignStmt, Access(frame, glenv))
                                            indexOfInit += 1

                            # If array is 4D
                            if len(dimension) == 4:
                                for i in range(dimension[0]):
                                    for j in range(dimension[1]):
                                        for k in range(dimension[2]):
                                            for m in range(dimension[3]):
                                                initAssignStmt = AssignStmt(
                                                    ArrayCell(
                                                        vardecl.name,
                                                        [IntegerLit(i), IntegerLit(j),
                                                         IntegerLit(k), IntegerLit(m)]),
                                                    initList[indexOfInit]
                                                )
                                                self.visit(
                                                    initAssignStmt, Access(frame, glenv))
                                                indexOfInit += 1

                            # If array is 5D, i think there is no guy use more dimension
                            if len(dimension) == 5:
                                for i in range(dimension[0]):
                                    for j in range(dimension[1]):
                                        for k in range(dimension[2]):
                                            for m in range(dimension[3]):
                                                for n in range(dimension[4]):
                                                    initAssignStmt = AssignStmt(
                                                        ArrayCell(
                                                            vardecl.name,
                                                            [IntegerLit(i), IntegerLit(j),
                                                             IntegerLit(k), IntegerLit(m), IntegerLit(n)]),
                                                        initList[indexOfInit]
                                                    )
                                                    self.visit(
                                                        initAssignStmt, Access(frame, glenv))
                                                    indexOfInit += 1
                    else:
                        if vardecl.init is not None:
                            initCode, initType = self.visit(
                                vardecl.init, Access(frame, glenv, False, True))
                            self.emit.printout(initCode)
                            self.emit.printout(self.emit.emitPUTSTATIC(
                                self.className + "/" + vardecl.name, vardecl.mtype, frame)
                            )

        # Visit body of FuncDecl
        for decl in Funcdecl.body.body:
            self.visit(decl, SubBody(frame, glenv, False))

        # Visit return
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # if type(returnType) is VoidType:
        # Generate dufault return
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()

    def ListOfList_to_List(self, expr):
        # arraylit = list of expr
        if type(expr) not in [list, ArrayLit]:
            return [expr]

        res = []
        if type(expr) is list:
            for exp in expr:
                res.append(self.ListOfList_to_List(exp))
        elif type(expr) is ArrayLit:
            for exp in expr.explist:
                res.append(self.ListOfList_to_List(exp))
        return reduce(lambda prev, curr: prev + curr, res, [])

    def visitVarDecl(self, ctx: VarDecl, o):
        if o.frame is None:
            o.sym = []
            if ctx.init is not None:
                initCode, initType = self.visit(
                    ctx.init,
                    Access(Frame("<clinit>", VoidType()), o.sym, False, True)
                )
                ctx.typ = initType if type(ctx.typ) is AutoType else ctx.typ
                code = self.emit.emitATTRIBUTE(
                    ctx.name, ctx.typ, False, initCode)
            else:
                code = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False, None)
            self.emit.printout(code)
            o.sym += [Symbol(ctx.name, ctx.typ,
                             CName(self.className), ctx.init, True)]
            return o.sym[-1]

        else:
            idx = o.frame.getNewIndex()
            if type(ctx.typ) is AutoType:
                ctx.typ = self.visit(ctx.init, Access(
                    o.frame, o.sym, False, True))[1]
            code = self.emit.emitVAR(
                idx, ctx.name, ctx.typ,
                o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame
            )
            self.emit.printout(code)
            o.sym += [Symbol(ctx.name, ctx.typ, Index(idx), ctx.init, False)]

            if ctx.init is not None:
                initCode, initType = self.visit(
                    ctx.init, Access(o.frame, o.sym, False, True))
                if type(ctx.typ) is ArrayType:
                    if len(ctx.typ.dimensions) == 1:
                        # Single dimensional array
                        initcode = self.ListOfList_to_List(
                            self.visit(ctx.init, Access(o.frame, o.sym))[0]
                        )
                        self.emit.printout(
                            self.emit.emitInitNewArray(
                                ctx.name, ctx.typ.dimensions, ctx.typ.typ, o.frame, initcode, idx
                            )
                        )
                    else:
                        # Multi dimensional array
                        # Treat initialize a vảiable to arraylit
                        # as assignstmt of arraycell to each of value in arraylit
                        initList = self.ListOfList_to_List(ctx.init)

                        # Allocate array
                        self.emit.printout(self.emit.emitInitNewArray(
                            ctx.name, ctx.typ.dimensions, ctx.typ.typ, o.frame, ctx.init, idx)
                        )

                        # Sorry for stupid method for generate init array code
# ⣿⣿⣿⣿⣿⣿⡷⣯⢿⣿⣷⣻⢯⣿⡽⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠸⣿⣿⣆⠹⣿⣿⢾⣟⣯⣿⣿⣿⣿⣿⣿⣽⣻⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣻⣽⡿⣿⣎⠙⣿⣞⣷⡌⢻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⡄⠹⣿⣿⡆⠻⣿⣟⣯⡿⣽⡿⣿⣿⣿⣿⣽⡷⣯⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣟⣷⣿⣿⣿⡀⠹⣟⣾⣟⣆⠹⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⡘⣿⣿⡄⠉⢿⣿⣽⡷⣿⣻⣿⣿⣿⣿⡝⣷⣯⢿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣯⢿⣾⢿⣿⡄⢄⠘⢿⣞⡿⣧⡈⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣧⠘⣿⣷⠈⣦⠙⢿⣽⣷⣻⣽⣿⣿⣿⣿⣌⢿⣯⢿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣟⣯⣿⢿⣿⡆⢸⡷⡈⢻⡽⣷⡷⡄⠻⣽⣿⣿⡿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣏⢰⣯⢷⠈⣿⡆⢹⢷⡌⠻⡾⢋⣱⣯⣿⣿⣿⣿⡆⢻⡿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⡎⣿⢾⡿⣿⡆⢸⣽⢻⣄⠹⣷⣟⣿⣄⠹⣟⣿⣿⣟⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⢸⣯⣟⣧⠘⣷⠈⡯⠛⢀⡐⢾⣟⣷⣻⣿⣿⣿⡿⡌⢿⣻⣿⣿
# ⣿⣿⣿⣿⣿⣿⣧⢸⡿⣟⣿⡇⢸⣯⣟⣮⢧⡈⢿⣞⡿⣦⠘⠏⣹⣿⣽⢿⣿⣿⣿⣿⣯⣿⣿⣿⡇⢸⣿⣿⣾⡆⠹⢀⣠⣾⣟⣷⡈⢿⣞⣯⢿⣿⣿⣿⢷⠘⣯⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⡈⣿⢿⣽⡇⠘⠛⠛⠛⠓⠓⠈⠛⠛⠟⠇⢀⢿⣻⣿⣯⢿⣿⣿⣿⣷⢿⣿⣿⠁⣾⣿⣿⣿⣧⡄⠇⣹⣿⣾⣯⣿⡄⠻⣽⣯⢿⣻⣿⣿⡇⢹⣾⣿
# ⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⡽⡇⢸⣿⣿⣿⣿⣿⣞⣆⠰⣶⣶⡄⢀⢻⡿⣯⣿⡽⣿⣿⣿⢯⣟⡿⢀⣿⣿⣿⣿⣿⣧⠐⣸⣿⣿⣷⣿⣿⣆⠹⣯⣿⣻⣿⣿⣿⢀⣿⢿
# ⣿⣿⣿⣿⣿⣿⣿⣿⠘⣯⡿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣧⡈⢿⣳⠘⡄⠻⣿⢾⣽⣟⡿⣿⢯⣿⡇⢸⣿⣿⣿⣿⣿⣿⡀⢾⣿⣿⣿⣿⣿⣿⣆⠹⣾⣷⣻⣿⡿⡇⢸⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠻⡇⢹⣆⠹⣟⣾⣽⣻⣟⣿⣽⠁⣾⣿⣿⣿⣿⣿⣿⣇⣿⣿⠿⠛⠛⠉⠙⠋⢀⠁⢘⣯⣿⣿⣧⠘⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⣿⡃⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⠌⣿⣆⠘⣿⣞⡿⣞⡿⡞⢠⣿⣿⣿⣿⣿⡿⠛⠉⠁⢀⣀⣠⣤⣤⣶⣶⣶⡆⢻⣽⣞⡿⣷⠈⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠘⠁⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⠛⢿⣄⢻⣿⣧⠘⢯⣟⡿⣽⠁⣾⣿⣿⣿⣿⣿⡃⢀⢀⠘⠛⠿⢿⣻⣟⣯⣽⣻⣵⡀⢿⣯⣟⣿⢀⣿
# ⣿⣿⣿⣟⣿⣿⣿⣿⣶⣶⡆⢀⣿⣾⣿⣾⣷⣿⣶⠿⠚⠉⢀⢀⣤⣿⣷⣿⣿⣷⡈⢿⣻⢃⣼⣿⣿⣿⣿⣻⣿⣿⣿⡶⣦⣤⣄⣀⡀⠉⠛⠛⠷⣯⣳⠈⣾⡽⣾⢀⣿
# ⣿⢿⣿⣿⣻⣿⣿⣿⣿⣿⡿⠐⣿⣿⣿⣿⠿⠋⠁⢀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣌⣥⣾⡿⣿⣿⣷⣿⣿⢿⣷⣿⣿⣟⣾⣽⣳⢯⣟⣶⣦⣤⡾⣟⣦⠘⣿⢾⡁⢺
# ⣿⣻⣿⣿⡷⣿⣿⣿⣿⣿⡗⣦⠸⡿⠋⠁⢀⢀⣠⣴⢿⣿⣽⣻⢽⣾⣟⣷⣿⣟⣿⣿⣿⣳⠿⣵⣧⣼⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣽⣳⣯⣿⣿⣿⣽⢀⢷⣻⠄⠘
# ⣿⢷⣻⣿⣿⣷⣻⣿⣿⣿⡷⠛⣁⢀⣀⣤⣶⣿⣛⡿⣿⣮⣽⡻⣿⣮⣽⣻⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢀⢸⣿⢀⡆
# ⠸⣟⣯⣿⣿⣷⢿⣽⣿⣿⣷⣿⣷⣆⠹⣿⣶⣯⠿⣿⣶⣟⣻⢿⣷⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣯⣟⢀⡇
# ⣇⠹⣟⣾⣻⣿⣿⢾⡽⣿⣿⣿⣿⣿⣆⢹⣶⣿⣻⣷⣯⣟⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⡿⡇⢸⡇
# ⣿⣆⠹⣷⡻⣽⣿⣯⢿⣽⣻⣿⣿⣿⣿⣆⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⠇⣼⡇
# ⡙⠾⣆⠹⣿⣦⠛⣿⢯⣷⢿⡽⣿⣿⣿⣿⣆⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠎⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣿⣾⣣⡿⡇
# ⣿⣷⡌⢦⠙⣿⣿⣌⠻⣽⢯⣿⣽⣻⣿⣿⣿⣧⠩⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢰⢣⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⢀⢀⢿⣞⣷⢿⡇
# ⣿⣽⣆⠹⣧⠘⣿⣿⡷⣌⠙⢷⣯⡷⣟⣿⣿⣿⣷⡀⡹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣈⠃⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢀⣴⡧⢀⠸⣿⡽⣿⢀
# ⢻⣽⣿⡄⢻⣷⡈⢿⣿⣿⢧⢀⠙⢿⣻⡾⣽⣻⣿⣿⣄⠌⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢁⣰⣾⣟⡿⢀⡄⢿⣟⣿⢀
# ⡄⢿⣿⣷⢀⠹⣟⣆⠻⣿⣿⣆⢀⣀⠉⠻⣿⡽⣯⣿⣿⣷⣈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣠⠘⣯⣷⣿⡟⢀⢆⠸⣿⡟⢸
# ⣷⡈⢿⣿⣇⢱⡘⢿⣷⣬⣙⠿⣧⠘⣆⢀⠈⠻⣷⣟⣾⢿⣿⣆⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⡞⢡⣿⢀⣿⣿⣿⠇⡄⢸⡄⢻⡇⣼
# ⣿⣷⡈⢿⣿⡆⢣⡀⠙⢾⣟⣿⣿⣷⡈⠂⠘⣦⡈⠿⣯⣿⢾⣿⣆⠙⠻⠿⠿⠿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢋⣠⣾⡟⢠⣿⣿⢀⣿⣿⡟⢠⣿⢈⣧⠘⢠⣿
# ⣿⣿⣿⣄⠻⣿⡄⢳⡄⢆⡙⠾⣽⣿⣿⣆⡀⢹⡷⣄⠙⢿⣿⡾⣿⣆⢀⡀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⣀⣠⣴⡿⣯⠏⣠⣿⣿⡏⢸⣿⡿⢁⣿⣿⢀⣿⠆⢸⣿
# ⣿⣿⣿⣿⣦⡙⣿⣆⢻⡌⢿⣶⢤⣉⣙⣿⣷⡀⠙⠽⠷⠄⠹⣿⣟⣿⣆⢙⣋⣤⣤⣤⣄⣀⢀⢀⢀⢀⣾⣿⣟⡷⣯⡿⢃⣼⣿⣿⣿⠇⣼⡟⣡⣿⣿⣿⢀⡿⢠⠈⣿
# ⣿⣿⣿⣿⣿⣷⣮⣿⣿⣿⡌⠁⢤⣤⣤⣤⣬⣭⣴⣶⣶⣶⣆⠈⢻⣿⣿⣆⢻⣿⣿⣿⣿⣿⣿⣷⣶⣤⣌⣉⡘⠛⠻⠶⣿⣿⣿⣿⡟⣰⣫⣴⣿⣿⣿⣿⠄⣷⣿⣿⣿
                        dimension = list(
                            map(lambda x: int(x), ctx.typ.dimensions))
                        indexOfInit = 0

                        # If array is 2D
                        if len(dimension) == 2:
                            for i in range(dimension[0]):
                                for j in range(dimension[1]):
                                    initAssignStmt = AssignStmt(
                                        ArrayCell(
                                            ctx.name, [IntegerLit(i), IntegerLit(j)]),
                                        initList[indexOfInit]
                                    )
                                    self.visit(initAssignStmt, o)
                                    indexOfInit += 1
                        # If array is 3D
                        # Ehe
                        if len(dimension) == 3:
                            for i in range(dimension[0]):
                                for j in range(dimension[1]):
                                    for k in range(dimension[2]):
                                        initAssignStmt = AssignStmt(
                                            ArrayCell(ctx.name, [IntegerLit(
                                                i), IntegerLit(j), IntegerLit(k)]),
                                            initList[indexOfInit]
                                        )
                                        self.visit(initAssignStmt, o)
                                        indexOfInit += 1

                        # If array is 4D

                        if len(dimension) == 4:
                            for i in range(dimension[0]):
                                for j in range(dimension[1]):
                                    for k in range(dimension[2]):
                                        for m in range(dimension[3]):
                                            initAssignStmt = AssignStmt(
                                                ArrayCell(
                                                    ctx.name,
                                                    [IntegerLit(i), IntegerLit(j), IntegerLit(k), IntegerLit(m)]),
                                                initList[indexOfInit]
                                            )
                                            self.visit(initAssignStmt, o)
                                            indexOfInit += 1

                        # If array is 5D, i think there is no guy use more dimension
                        if len(dimension) == 5:
                            for i in range(dimension[0]):
                                for j in range(dimension[1]):
                                    for k in range(dimension[2]):
                                        for m in range(dimension[3]):
                                            for n in range(dimension[4]):
                                                initAssignStmt = AssignStmt(
                                                    ArrayCell(
                                                        ctx.name,
                                                        [IntegerLit(i), IntegerLit(j),
                                                         IntegerLit(k), IntegerLit(m), IntegerLit(n)]),
                                                    initList[indexOfInit]
                                                )
                                                self.visit(initAssignStmt, o)
                                                indexOfInit += 1
                else:
                    self.emit.printout(initCode)
                    self.emit.printout(self.emit.emitWRITEVAR(
                        ctx.name, ctx.typ, idx, o.frame))
            else:
                if type(ctx.typ) in [IntegerType, BooleanType]:
                    self.emit.printout(self.emit.emitPUSHICONST(0, o.frame))
                elif type(ctx.typ) is FloatType:
                    self.emit.printout(self.emit.emitPUSHFCONST(0.0, o.frame))
                elif type(ctx.typ) is StringType:
                    self.emit.printout(self.emit.emitPUSHCONST(
                        "", StringType(), o.frame))
                self.emit.printout(self.emit.emitWRITEVAR(
                    ctx.name, ctx.typ, idx, o.frame))
            return o.sym[-1]

    def visitAssignStmt(self, ctx: AssignStmt, o):
        rcode, rtype = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
        lcode, ltype = self.visit(ctx.lhs, Access(o.frame, o.sym, True))

        if type(ctx.lhs) in [Id, FuncCall]:
            leftSym = list(filter(lambda x: x.name == ctx.lhs.name, o.sym))[-1]
            leftSym.mtype = rtype if type(ltype) is AutoType else ltype
        if type(ctx.rhs) in [Id, FuncCall]:
            rightSym = list(
                filter(lambda x: x.name == ctx.rhs.name, o.sym))[-1]
            rightSym.mtype = ltype if type(rtype) is AutoType else rtype

        # rcode = ''.join(rcode) if type(rcode) is list else rcode
        # lcode = ''.join(lcode) if type(lcode) is list else lcode
        if type(ctx.lhs) is ArrayCell:
            self.emit.printout(lcode)
            self.emit.printout(rcode)
            self.emit.printout(self.emit.emitASTORE(rtype, o.frame))
        elif type(ctx.rhs) is ArrayCell:
            self.emit.printout(lcode)
            self.emit.printout(rcode)
        else:
            self.emit.printout(rcode)
            self.emit.printout(lcode)

    def visitBlockStmt(self, ctx: BlockStmt, o):
        o.frame.enterScope(False)
        for decl in ctx.body:
            self.visit(decl, o)
        o.frame.exitScope()

    def visitIfStmt(self, ctx: IfStmt, o):
        if ctx.fstmt is None:
            ecode, etype = self.visit(ctx.cond, Access(o.frame, o.sym, False))
            self.emit.printout(ecode)
            # Xin frame cap FLABEL
            FLABEL = o.frame.getNewLabel()
            # Nhay den FLABEL neu dinh stack la false
            code = self.emit.emitIFFALSE(FLABEL, o.frame)
            self.emit.printout(code)
            # Sinh ma cho TrueStmt
            self.visit(ctx.tstmt, o)
            # Sinh ma de dat FLABEL tai day
            code = self.emit.emitLABEL(FLABEL, o.frame)
            self.emit.printout(code)
        else:
            ecode, etype = self.visit(ctx.cond, Access(o.frame, o.sym, False))
            self.emit.printout(ecode)
            # Xin frame cap FLABEL
            FLABEL = o.frame.getNewLabel()
            EXITLABEL = o.frame.getNewLabel()
            # Nhay den FLABEL neu dinh stack la false
            code = self.emit.emitIFFALSE(FLABEL, o.frame)
            self.emit.printout(code)
            # Sinh ma trueStmt
            self.visit(ctx.tstmt, o)
            # Nhay toi EXITLABEL
            code = self.emit.emitGOTO(EXITLABEL, o.frame)
            self.emit.printout(code)
            # Sinh ma de dat FLABEL tai day
            code = self.emit.emitLABEL(FLABEL, o.frame)
            self.emit.printout(code)
            # Sinh ma cho ElseStmt
            self.visit(ctx.fstmt, o)
            # Sinh ma de dat EXITLABEL tai day
            code = self.emit.emitLABEL(EXITLABEL, o.frame)
            self.emit.printout(code)

    def visitForStmt(self, ctx: ForStmt, o):
        o.frame.enterLoop()
        # Sinh ma cho CONTINUELABEL, BREAKLABEL
        CONTINUELABEL = o.frame.getContinueLabel()
        BREAKLABEL = o.frame.getBreakLabel()
        STARTLABEL = o.frame.getNewLabel()
        # Visit init AssignStmt dau vong lap
        self.visit(ctx.init, o)
        # Tinh toan condition
        self.emit.printout(self.emit.emitLABEL(STARTLABEL, o.frame))
        self.emit.printout(self.visit(ctx.cond, Access(o.frame, o.sym))[0])
        # If condition is false, go to break label
        self.emit.printout(self.emit.emitIFFALSE(BREAKLABEL, o.frame))
        # Else, continue to visit stmt
        self.visit(ctx.stmt, o)
        # Dat ma cho CONTINUELABEL sau khi visit Init
        self.emit.printout(self.emit.emitLABEL(CONTINUELABEL, o.frame))
        # Treat update expresstion as an AssignStmt
        updateExpr = AssignStmt(
            ctx.init.lhs, BinExpr("+", ctx.init.lhs, ctx.upd))
        self.visit(updateExpr, o)
        # Quay lai STARTLABEL
        self.emit.printout(self.emit.emitGOTO(STARTLABEL, o.frame))
        # Dat ma cho BREAKLABEL ket thuc vong lap
        self.emit.printout(self.emit.emitLABEL(BREAKLABEL, o.frame))

        o.frame.exitLoop()

    def visitWhileStmt(self, ctx: WhileStmt, o):
        # Bat dau sinh ma cho vong lap
        o.frame.enterLoop()
        # Set STARTLABEL = CONTINUELABEL, EXITLABEL = BREAKLABEL
        CONTINUELABEL = o.frame.getContinueLabel()
        BREAKLABEL = o.frame.getBreakLabel()
        # Dat ma CONTINUELABEL dau vong lap
        self.emit.printout(self.emit.emitLABEL(CONTINUELABEL, o.frame))
        # Tinh expr
        ecode = self.visit(ctx.cond, Access(o.frame, o.sym, False))[0]
        self.emit.printout(ecode)
        # If expr is false then goto EXITLABEL
        self.emit.printout(self.emit.emitIFFALSE(BREAKLABEL, o.frame))
        # Sinh ma cho stmt
        self.visit(ctx.stmt, o)
        # Quay tro lai dau vong lap
        self.emit.printout(self.emit.emitGOTO(CONTINUELABEL, o.frame))
        # Dat ma BREAKLABEL tai day
        self.emit.printout(self.emit.emitLABEL(BREAKLABEL, o.frame))
        # Ket thuc sinh ma cho vong lap
        o.frame.exitLoop()

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o):
        o.frame.enterLoop()
        CONTINUELABEL = o.frame.getContinueLabel()
        BREAKLABEL = o.frame.getBreakLabel()
        # Visit stmt lan dau
        self.visit(ctx.stmt, Access(o.frame, o.sym, False))
        # Dat ma cho CONTINUELABEL
        self.emit.printout(self.emit.emitLABEL(CONTINUELABEL, o.frame))
        # Tinh expr
        ecode = self.visit(ctx.cond, Access(o.frame, o.sym, False))[0]
        self.emit.printout(ecode)
        # If expr is false then goto EXITLABEL
        self.emit.printout(self.emit.emitIFFALSE(BREAKLABEL, o.frame))
        # Sinh ma cho blockstmt
        self.visit(ctx.stmt, Access(o.frame, o.sym, False))
        # Quay tro lai dau vong lap
        self.emit.printout(self.emit.emitGOTO(CONTINUELABEL, o.frame))
        # Dat ma cho BREAKLABEL
        self.emit.printout(self.emit.emitLABEL(BREAKLABEL, o.frame))
        o.frame.exitLoop()

    def visitBreakStmt(self, ctx: BreakStmt, o):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getBreakLabel(), o.frame))

    def visitContinueStmt(self, ctx: ContinueStmt, o):
        self.emit.printout(self.emit.emitGOTO(
            o.frame.getContinueLabel(), o.frame))

    def visitReturnStmt(self, ctx: ReturnStmt, o):
        if type(o.frame.returnType) is not VoidType:
            ecode, etype = self.visit(
                ctx.expr, Access(o.frame, o.sym, False, False))
            if type(o.frame.returnType) is FloatType and type(etype) is IntegerType:
                ecode = ecode + self.emit.emitI2F(o.frame)
            self.emit.printout(ecode)
        # self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(o.frame.returnType, o.frame))

    def visitCallStmt(self, ctx: CallStmt, o):
        if ctx.name in ['super', 'preventDefault']:
            return
        sym = next(filter(lambda x: ctx.name == x.name, o.sym), None)
        cname = sym.value.value
        f_info = sym.mtype
        if type(f_info.rettype) is AutoType:
            f_info.rettype = VoidType()
        code = ""
        i = 0
        for x in ctx.args:
            acode, atype = self.visit(x, Access(o.frame, o.sym, False, False))
            code += acode
            if type(f_info.partype[i]) is FloatType and type(atype) is IntegerType:
                code += self.emit.emitI2F(o.frame)
            i += 1
        self.emit.printout(code)

        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ctx.name, f_info, o.frame))

    def visitFuncCall(self, ctx: FuncCall, o):
        for defaultFunction in self.env:
            if ctx.name == defaultFunction.name:
                code = self.emit.emitINVOKESTATIC(
                    defaultFunction.value.value + "/" + defaultFunction.name,
                    defaultFunction.mtype, o.frame
                )
                return code, defaultFunction.mtype.rettype
        sym = next(filter(lambda x: ctx.name == x.name, o.sym), None)
        cname = sym.value.value
        f_info = sym.mtype
        pair = ["", list()]
        for arg in ctx.args:
            str1, typ1 = self.visit(arg, Access(o.frame, o.sym, False, True))
            pair = [pair[0] + str1, pair[1].append(typ1)]
            if type(f_info.rettype) is FloatType and type(typ1) is IntegerType:
                pair[0] += self.emit.emitI2F(o.frame)

        pair[0] = pair[0] + \
            self.emit.emitINVOKESTATIC(cname + "/" + ctx.name, f_info, o.frame)
        return pair[0], f_info.rettype

    def visitBinExpr(self, ctx: BinExpr, o):
        e1c, e1t = self.visit(ctx.left, o)
        e2c, e2t = self.visit(ctx.right, o)

        if type(e1t) is AutoType:
            leftSym = list(filter(lambda x: x.name ==
                           ctx.left.name, o.sym))[-1]
            if type(ctx.left) is Id:
                leftSym.mtype = e2t
            else:
                leftSym.mtype.rettype = e2t
        if type(e2t) is AutoType:
            rightSym = list(filter(lambda x: x.name ==
                            ctx.right.name, o.sym))[-1]
            if type(ctx.right) is Id:
                rightSym.mtype = e1t
            else:
                rightSym.mtype.rettype = e1t

        if type(e1t) is type(e2t):
            rt = e1t
        elif type(e1t) is IntegerType and type(e2t) is FloatType:
            e1c = e1c + self.emit.emitI2F(o.frame)
            rt = FloatType()
        else:
            e2c = e2c + self.emit.emitI2F(o.frame)
            rt = FloatType()

        if ctx.op == '*':
            op = self.emit.emitMULOP(ctx.op, rt, o.frame)
        elif ctx.op in ['+', '-']:
            op = self.emit.emitADDOP(ctx.op, rt, o.frame)
        elif ctx.op == '/':
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                e1c = e1c + self.emit.emitI2F(o.frame)
                e2c = e2c + self.emit.emitI2F(o.frame)
                rt = FloatType()
            op = self.emit.emitMULOP(ctx.op, rt, o.frame)
        elif ctx.op == '%':
            rt = IntegerType()
            op = self.emit.emitMOD(o.frame)
        elif ctx.op == '::':
            rt = StringType()
            op = self.emit.emitINVOKEVIRTUAL(
                'java/lang/String/concat', MType([StringType()], StringType()), o.frame)
        elif ctx.op == '&&':
            rt = BooleanType()
            op = self.emit.emitANDOP(o.frame)
        elif ctx.op == '||':
            rt = BooleanType()
            op = self.emit.emitOROP(o.frame)
        else:
            op = self.emit.emitREOP(ctx.op, rt, o.frame)
            rt = BooleanType()

        return e1c + e2c + op, rt

    def visitUnExpr(self, ctx: UnExpr, o):
        ec, et = self.visit(ctx.val, o)

        if type(et) is AutoType:
            sym = list(filter(lambda x: x.name == ctx.val.name, o.sym))[-1]
            if type(ctx.val) is Id:
                sym.mtype = IntegerType() if ctx.op == '-' else BooleanType()
            else:
                sym.mtype.rettype = IntegerType() if ctx.op == '-' else BooleanType()

        if ctx.op == '-':
            rt = et
            op = self.emit.emitNEGOP(et, o.frame)
        elif ctx.op == '!':
            rt = BooleanType()
            op = self.emit.emitNOT(0, o.frame)

        return ec + op, rt

    def visitId(self, ctx: Id, o):
        # Get the most local variable
        sym = list(filter(lambda x: x.name == ctx.name, o.sym))[-1]
        if o.isLeft == False:
            if type(sym.value) is Index:
                code = self.emit.emitREADVAR(
                    sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitGETSTATIC(
                    sym.value.value + "." + sym.name, sym.mtype, o.frame)
        else:
            if type(sym.value) is Index:
                o.frame.push()
                code = self.emit.emitWRITEVAR(
                    sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitPUTSTATIC(
                    sym.value.value + "." + sym.name, sym.mtype, o.frame)
        return code, sym.mtype

    def visitArrayCell(self, ctx: ArrayCell, o):
        # Tim declare cua Id array
        # Chung ta can them gia tri cua ve phai, trong AssignStmt can goi ASTORE de luu gia tri
        code = []
        sym = list(filter(lambda x: x.name == ctx.name, o.sym))[0]
        if o.isLeft:
            if sym.isGlobal:
                code += [self.emit.emitGETSTATIC(self.className +
                                                 "/" + sym.name, sym.mtype, o.frame)]
            else:
                code += [self.emit.emitREADVAR(sym.name,
                                               sym.mtype, sym.value.value, o.frame)]
            while len(ctx.cell) > 1:
                cellcode, celltype = self.visit(
                    ctx.cell.pop(0), Access(o.frame, o.sym))
                code += [cellcode]
                code += [self.emit.emitALOAD(sym.mtype, o.frame)]
            cellcode, celltype = self.visit(
                ctx.cell.pop(0), Access(o.frame, o.sym))
            code += [cellcode]
        else:
            if sym.isGlobal:
                code += [self.emit.emitGETSTATIC(self.className +
                                                 "/" + sym.name, sym.mtype, o.frame)]
            else:
                code += [self.emit.emitREADVAR(sym.name,
                                               sym.mtype, sym.value.value, o.frame)]
            while len(ctx.cell) > 1:
                cellcode, celltype = self.visit(
                    ctx.cell.pop(0), Access(o.frame, o.sym))
                code += [cellcode]
                code += [self.emit.emitALOAD(sym.mtype, o.frame)]
            cellcode, celltype = self.visit(
                ctx.cell.pop(0), Access(o.frame, o.sym))
            code += [cellcode]
            code += self.emit.emitALOAD(sym.mtype.typ, o.frame)

        return ''.join(code), sym.mtype.typ

    def visitIntegerLit(self, ctx: IntegerLit, o):
        return self.emit.emitPUSHICONST(ctx.val, o.frame), IntegerType()

    def visitFloatLit(self, ctx: FloatLit, o):
        return self.emit.emitPUSHFCONST(ctx.val, o.frame), FloatType()

    def visitStringLit(self, ctx: StringLit, o):
        return self.emit.emitPUSHCONST(ctx.val, StringType(), o.frame), StringType()

    def visitBooleanLit(self, ctx: BooleanLit, o):
        return self.emit.emitPUSHICONST(ctx.val, o.frame), BooleanType()

    def visitArrayLit(self, ctx: ArrayLit, o):
        code = []
        for exp in ctx.explist:
            ecode, etype = self.visit(exp, Access(o.frame, o.sym))
            if type(exp) is not ArrayType:
                code += [ecode]
            else:
                self.visit(exp, Access(o.frame, o.sym))
        return code, ArrayType(len(ctx.explist), etype)
