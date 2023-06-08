import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_0(self):
        input = "main:function void(){}"
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 400))

    def test_1(self):
        input = "mai:function void(){}"
        output = "No entry point"
        self.assertTrue(TestChecker.test(input, output, 401))

    def test_2(self):
        input = """foo:function array[1] of integer (out a: integer) inherit goo {}
goo:function integer(a:integer, b:float){}"""
        output = "Invalid statement in function: foo"
        self.assertTrue(TestChecker.test(input, output, 402))

    def test_3(self):
        input = """foo:function array[1] of integer (out c: integer) inherit goo {super(1,2.0);}
goo:function integer(a:integer, b:float){}
main:function void() {}"""
        output = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, output, 403))

    def test_4(self):
        input = """a,b,c: integer = 1,2,3;"""
        output = "No entry point"
        self.assertTrue(TestChecker.test(input, output, 404))

    def test_5(self):
        input = """a,b,c:auto = 3, 4.0, {5};
        d:auto;
        main: function void(a:integer, b:float, c: array[1] of integer) {}"""
        output = "Invalid Variable: d"
        self.assertTrue(TestChecker.test(input, output, 405))

    def test_6(self):
        input = """a,b,c:auto = 3, 4.0, {5,6.0};
        d:auto = 2;
        main: function void() {}"""
        output = "Illegal array literal: ArrayLit([IntegerLit(5), FloatLit(6.0)])"
        self.assertTrue(TestChecker.test(input, output, 406))

    def test_7(self):
        input = """a,b,c:auto = 3, 4.0, {5};
        d:auto = 1;
        main: function void(a:integer, b:float, c: array[1] of integer) {}"""
        output = "No entry point"
        self.assertTrue(TestChecker.test(input, output, 407))

    def test_8(self):
        input = """foo:function integer() inherit goo {}
        main: function void() {}"""
        output = "Undeclared Function: goo"
        self.assertTrue(TestChecker.test(input, output, 408))

    def test_9(self):
        input = """foo:function integer() inherit goo {super(1);}
        goo: function void(inherit a:integer){}
        main: function void() {}"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 409))

    def test_10(self):
        input = """main: function void() {
            if (1+1 == 2) break;
            continue;
        }"""
        output = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, output, 410))

    def test_11(self):
        input = """main: function void() {
            if (1 == 1) if (2 == 2) if (3 == 3) if (4 == 4) if (5 == 5) continue;
        }"""
        output = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, output, 411))

    def test_12(self):
        input = """main: function void() {
            x:integer = 1;
            if (x == 1) {
                i:integer;
                for (i = 1, i < 10, 1) {
                    printInteger(i);
                    y:integer = 2;
                    continue;
                }
            }
            break;
        }"""
        output = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, output, 412))

    def test_13(self):
        input = """main: function void() {
            x:integer = "A";
        }"""
        output = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, StringLit(A))"
        self.assertTrue(TestChecker.test(input, output, 413))

    def test_14(self):
        input = """
        foo: function void(inherit a:integer){}
        goo: function void(a:integer) inherit foo{}
        main: function void() {
        }"""
        output = "Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, output, 414))

    def test_15(self):
        input = """
        foo: function void(inherit d:integer){}
        goo: function void (c:integer,b:float) inherit foo{

            super(1);
        }
        main: function void() {
        }"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 415))

    def test_16(self):
        input = """
        foo: function void(){}
        goo: function void (c:integer,b:float) inherit foo{
            super(d);
        }
        main: function void() {
        }"""
        output = "Type mismatch in expression: Id(d)"
        self.assertTrue(TestChecker.test(input, output, 416))

    def test_17(self):
        input = """
        a:integer = 1;
        b:integer = 2;
        foo:function integer(a: integer, b: float){}
        main: function void() {
            foo(a);
        }"""
        output = "Type mismatch in statement: CallStmt(foo, Id(a))"
        self.assertTrue(TestChecker.test(input, output, 417))

    def test_18(self):
        input = """
        a,c:integer = 1,3;
        b:float = 2;
        
        foo:function integer(a: integer, b: float){}
        main: function void() {
            foo(a,b,c);
        }"""
        output = "Type mismatch in statement: CallStmt(foo, Id(a), Id(b), Id(c))"
        self.assertTrue(TestChecker.test(input, output, 418))

    def test_19(self):
        input = """
        a:integer = 1;
        b:integer = 2;
        c:integer = 3;
        foo:function float(a: integer, b: float){}
        main: function void() {
            a = foo(a,b);
        }"""
        output = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [Id(a), Id(b)]))"
        self.assertTrue(TestChecker.test(input, output, 419))

    def test_20(self):
        input = """
        a:integer = 1;
        b:integer = 2;
        c:integer = 3;
        foo:function integer(a: integer, b: float){}
        main: function void() {
            a = i + 1;
        }"""
        output = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, output, 420))

    def test_21(self):
        input = """
        a:integer = 1;
        b:string = "a";
        foo:function integer(a: integer, b: boolean){}
        main: function void() {
            foo(a, b);
        }"""
        output = "Type mismatch in statement: CallStmt(foo, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, output, 421))

    def test_22(self):
        input = """
        main: function void() {
            a,b:integer = 1,2;
            a = b + 1;
        }"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 422))

    def test_23(self):
        input = """
        main: function void() {
            a,b:integer = 1,2;
            c: float = 1;
            a = c + 1;
        }"""
        output = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, Id(c), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, output, 423))

    def test_24(self):
        input = """
        main: function void() {
            a,b:integer = 1,2;
            c: float = 1;
            d:string = "aa";
            a = c == d;
        }"""
        output = "Type mismatch in expression: BinExpr(==, Id(c), Id(d))"
        self.assertTrue(TestChecker.test(input, output, 424))

    def test_25(self):
        input = """
        main: function void() {
            arr:array [2] of integer = {1,2};
            printInteger(arr[2]);
        }"""
        output = "Type mismatch in expression: ArrayCell(arr, [IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, output, 425))

    def test_26(self):
        input = """
        main: function void() {
            x:integer;
            if (1+1) x = 2;
        }"""
        output = "Type mismatch in statement: IfStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)), AssignStmt(Id(x), IntegerLit(2)))"
        self.assertTrue(TestChecker.test(input, output, 426))

    def test_27(self):
        input = """
        a:integer;
        main: function void() {
            a:integer = 1;
        }"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 427))

    def test_28(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum: integer;
            sum = a + b + c;
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 428))

    def test_29(self):
        input = """
        a, b, c: integer = 4, 5.0, 6;
        main: function void () {
            sum: integer;
            sum = a + b + c;
        }
        """
        output = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, FloatLit(5.0))"
        self.assertTrue(TestChecker.test(input, output, 429))

    def test_30(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum: integer;
            sum = a + b + c + 0.5;
        }
        """
        output = "Type mismatch in statement: AssignStmt(Id(sum), BinExpr(+, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)), FloatLit(0.5)))"
        self.assertTrue(TestChecker.test(input, output, 430))

    def test_31(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum: float;
            sum = a + b + c;
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 431))

    def test_32(self):
        input = """
        a, b, c: float = 4, 5, 6;
        main: function void () {
            sum: integer;
            sum = a + b + c + 0.5;
        }
        """
        output = "Type mismatch in statement: AssignStmt(Id(sum), BinExpr(+, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)), FloatLit(0.5)))"
        self.assertTrue(TestChecker.test(input, output, 432))

    def test_33(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum: integer;
            a = a + b + c + 0.5;
        }
        """
        output = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)), FloatLit(0.5)))"
        self.assertTrue(TestChecker.test(input, output, 433))

    def test_34(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum: integer;
            a = a + b + c + "s";
        }
        """
        output = "Type mismatch in expression: BinExpr(+, BinExpr(+, BinExpr(+, Id(a), Id(b)), Id(c)), StringLit(s))"
        self.assertTrue(TestChecker.test(input, output, 434))

    def test_35(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum : integer;
            sum : integer;
            a = a + b + c + s;
        }
        """
        output = "Redeclared Variable: sum"
        self.assertTrue(TestChecker.test(input, output, 435))

    def test_36(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum: integer;
            a : integer = 1;
            a = a + b + c ;
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 436))

    def test_37(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum: integer;
            a = a + b + c + s;
        }
        """
        output = "Undeclared Identifier: s"
        self.assertTrue(TestChecker.test(input, output, 437))

    def test_38(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum : float;
            sum = sum + a + b + c;
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 438))

    def test_39(self):
        input = """
        a, b, c: integer = 4, 5, 6;
        main: function void () {
            sum : float;
            sum = sum + a + b + c;
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 439))

    def test_40(self):
        input = """
        a: array [2, 3, 1] of integer = { { {1}, {2}, {3} }, foo() };  // 1
foo: function array[3,1] of integer () {}
main:function void () {}
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 440))

    def test_41(self):
        input = """
        foo: function auto(x:integer){
            return x;
        }
        main: function void () {
            a:string = foo(1);
        }
        """
        output = "Type mismatch in Variable Declaration: VarDecl(a, StringType, FuncCall(foo, [IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, output, 441))

    def test_42(self):
        input = """
        a, b: integer = 4, 5;
        c : float = 6.0;
        main: function void () {
            sum : float;
            sum = a + b + c;
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 442))

    def test_43(self):
        input = """
        lmao : function string (){
            haha: string = "hi hi";
            return haha;
        }
        main: function void () {
            lmao();
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 443))

    def test_44(self):
        input = """
        foo:function integer (inherit a:integer) {}
        goo: function integer (b:integer) inherit foo {
            super(1);
            x:integer =  a + b;
            return x;
        }
        main: function void () {
            x:integer = goo(1);
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 444))

    def test_45(self):
        input = """
        a : integer = 1;
        main: function void () {
            a : integer = 10;
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 445))

    def test_46(self):
        input = """
        foo:function integer (inherit a:integer, inherit b:integer) {}
        goo: function integer (b:integer) inherit foo {
            super(1, 2);
            x: integer = a + b;
        }
        main: function void () {
            x:integer = goo(1);
        }
        """
        output = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, output, 446))

    def test_47(self):
        input = """
        foo:function integer (inherit a:integer, b :integer) {}
        goo: function integer (b:integer) inherit foo {
            super(1, 2);
            x: integer = a + b;
        }
        main: function void () {
            x:integer = goo(1);
        }
        """
        output = "Type mismatch in expression: IntegerLit(2)"
        self.assertTrue(TestChecker.test(input, output, 447))

    def test_48(self):
        input = """
        foo:function integer (inherit a:integer, b :integer) {}
        goo: function integer (b:integer) inherit foo {
            super(1);
            a: integer = b;
        }
        main: function void () {
            x:integer = goo(1);
        }
        """
        output = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, output, 448))

    def test_49(self):
        input = """

        main: function void () {
            a: array[3] of string = {3, 1, 2};
            i: integer;
            for (i = 1, i + 3, i + 1) {
                
            }
        }
        """
        output = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([3], StringType), ArrayLit([IntegerLit(3), IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, output, 449))

    def test_50(self):
        input = """

        main: function void () {
            a: array[3] of float = {3, 1, 2};
            i: integer;
            for (i = 1, i <= 3, i + 1) {
                a[i] = a[i] + " ";
            }
        }
        """
        output = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([3], FloatType), ArrayLit([IntegerLit(3), IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, output, 450))

    def test_51(self):
        input = """
        main: function void () {
            a: array[3] of integer = {3, 1, 2};
            i: integer;
            for (i = 1, i <= 3, i + 1) {
                a[i] = a;
            }
        }
        """
        output = "Type mismatch in statement: AssignStmt(ArrayCell(a, [Id(i)]), Id(a))"
        self.assertTrue(TestChecker.test(input, output, 451))

    def test_52(self):
        input = """
        main: function void () {
            a: array[3] of float = {3, 1.0, 2};
            i, j: integer;
            for (i = 0, i < 3, i + 1) {
                for (j = i+1, j < 3, j + "1"){
                    a[i] = a[j];    
                }
            }
        }
        """
        output = "Illegal array literal: ArrayLit([IntegerLit(3), FloatLit(1.0), IntegerLit(2)])"
        self.assertTrue(TestChecker.test(input, output, 452))

    def test_53(self):
        input = """
        foo : function integer(inherit y: integer){}
        goo : function integer(x: integer){
            i: integer;
            for (i = 0, i < 10, i + 1) {
                super(1);
            }
        }
        main: function void () {
            a: array[3] of integer = {3, 1, 2};
            i, j: integer;
            for (i = 0, i < 3, i + 1) {
                for (j = i+1, j < 3, j + "1"){
                    a[i] = goo(a[i]);    
                }
            }
        }
        """
        output = "Type mismatch in expression: BinExpr(+, Id(j), StringLit(1))"
        self.assertTrue(TestChecker.test(input, output, 453))

    def test_54(self):
        input = """
        main: function void () {
            a: array[3] of integer = {3, 1, 2};
            b: array[1] of string = {" "};
            c: array[4] of integer = a + b;
        }
        """
        output = "Type mismatch in Variable Declaration: VarDecl(c, ArrayType([4], IntegerType), BinExpr(+, Id(a), Id(b)))"
        self.assertTrue(TestChecker.test(input, output, 454))

    def test_55(self):
        input = """
        a:array [2, 3, 2] of integer = {{{1, 2}, {1, 2}}, {{1, 2}, {1, "2"}, {1, 2}}};
        main:function void() {}
        """
        output = "Illegal array literal: ArrayLit([IntegerLit(1), StringLit(2)])"
        self.assertTrue(TestChecker.test(input, output, 455))

    def test_56(self):
        input = """
        main: function void () {
            i : auto = 1.1;
            while (i > 1){
            }
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 456))

    def test_57(self):
        input = """
        main: function void () {
            a:array [2, 3, 2] of integer = {{{1, 2}, {1, 2}, {1, 2}}, {{1, 2}, {1, 2}, {1, 2}}};
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 457))

    def test_58(self):
        input = """
        main: function void () {
            i : auto = 1.1;
            while (i == 1){
            }
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 458))

    def test_59(self):
        input = """
        main: function void () {
            i : auto = 1.1;
            while (i / 1){
            }
        }
        """
        output = "Type mismatch in statement: WhileStmt(BinExpr(/, Id(i), IntegerLit(1)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, output, 459))

    def test_60(self):
        input = """
        foo:function auto() {}
        main: function void () {
            a:float = -foo();
            b: integer = foo();
        }
        """
        output = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, FuncCall(foo, []))"
        self.assertTrue(TestChecker.test(input, output, 460))

    def test_61(self):
        input = """
        foo: function auto (x:auto) {
            return x;
        }
        main: function void () {
            i : auto = 1.1;
            
            while (foo(i) < 3.0){
            }
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 461))

    def test_62(self):
        input = """
        foo: function void() {
            foo:integer = foo();
            return foo(foo);
        }
        main: function void () {
            i : auto = 1;
            while (i < 10){
                i = i + 1;
            }
        }
        """
        output = "Type mismatch in expression: FuncCall(foo, [])"
        self.assertTrue(TestChecker.test(input, output, 462))

    def test_63(self):
        input = """
        main: function void () {
            a:array [2,2] of integer = {{1,2},{3,4}};
            B:integer;
            B = a[0,1] * a[1,0];
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 463))

    def test_64(self):
        input = """
        foo: function void (inherit a:integer) {}
        goo: function void (b:integer) inherit foo {
            super(1);
            if (b == 1){
                a:integer = 1;
            }
        }
        main: function void () {}
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 464))

    def test_65(self):
        input = """
        foo: function void (inherit a:integer) {}
        goo: function void (b:integer) inherit foo {
            preventDefault();
            if (b == 1){
                a:integer = 1;
            }
            a:integer;
        }
        main: function void () {}
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 465))

    def test_66(self):
        input = """
        a: integer = 1;
        main: function void () {
            a,b:integer = 2,3;
            printInteger(a);
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 466))

    def test_67(self):
        input = """
        a: integer = 1;
        main: function void () {
            a,b:integer = 2,3;
            printFloat(a);
        }
        """
        output = "Type mismatch in expression: CallStmt(printFloat, Id(a))"
        self.assertTrue(TestChecker.test(input, output, 467))

    def test_68(self):
        input = """
        a: integer = 1;
        main: function void () {
            a,b:integer = 2,3;
            str:string = "abc"::"123";
            printString(str);
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 468))

    def test_69(self):
        input = """
        x: function void() {}
        main: function void() inherit x {
            super(); //?
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 469))

    def test_70(self):
        input = """
        x: function void() {}
        main: function void() inherit x {
            super(1); //?
        }
        """
        output = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, output, 470))

    def test_71(self):
        input = """
        x: function void(inherit a:integer, inherit b:float, inherit c:string) {}
        main: function void() inherit x {
            super(1,1.0,"aha"); 
            c:string;
        }
        """
        output = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, output, 471))

    def test_72(self):
        input = """
        x: function void(inherit a:integer, inherit b:float, inherit c:string) {}
        main: function void() inherit x {
            super(1,1.0,"aha"); 
            x(1, 1, "a");
            return c;
        }
        
        """
        output = "Type mismatch in statement: ReturnStmt(Id(c))"
        self.assertTrue(TestChecker.test(input, output, 472))

    def test_73(self):
        input = """
        foo: function integer() {
            return 1;
        }
        main: function void(){

        }
        
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 473))

    def test_74(self):
        input = """
        a: function integer () {
            a:integer;
        }
        main: function void(){

        }
        
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 474))

    def test_75(self):
        input = """
        a: function integer () {
            a:integer;
            if (a == 1) {
                if (a + 1 == 2) return 2;
            }
            return 1;
        }
        main: function void() {}
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 475))

    def test_76(self):
        input = """
        a: function integer () {
            a:integer;
            return 1;
            if (a == 1) {
                if (a + 1 == 2) a = 2;
            }
            return 1.0;
        }
        main: function void() {}
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 476))

    def test_77(self):
        input = """
        a: function auto () {
            a:integer;
            if (a == 1) {
                if (a + 1 == 2) {
                    a = 2;
                    return a;
                }
            }
            return 1.0;
        }
        main: function void() {}
        """
        output = "Type mismatch in statement: ReturnStmt(FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, output, 477))

    def test_78(self):
        input = """
        a: function auto () {
            a:integer;
            if (a == 1) {
                if (a + 1 == 2) {
                    a = 2;
                    return a;
                }
                else {
                    return 2.0;
                }
            }
            return 1;
        }
        main: function void() {}
        """
        output = "Type mismatch in statement: ReturnStmt(FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, output, 478))

    def test_79(self):
        input = """
        factorial: function integer (a:integer) {
            if ((a == 1) || (a == 0)) return 1;
            else return a * factorial(a-1);
        }
        main: function void() {
            printInteger(factorial(10));
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 479))

    def test_80(self):
        input = """
        factorial: function integer (a:integer) {
            if (a == 1 || a == 0) return 1;
            else return a * factorial(a-1);
        }
        main: function void() {
            printInteger(factorial(10));
        }
        """
        output = "Type mismatch in expression: BinExpr(==, Id(a), BinExpr(||, IntegerLit(1), Id(a)))"
        self.assertTrue(TestChecker.test(input, output, 480))

    def test_81(self):
        input = """
        plus: function integer(a: integer, b:integer) {return a+b;}
        fplus: function float(a: float, b:float) {return a+b;}
        splus: function string(a: string, b:string) {return a::b;}
        main: function void() {
            printInteger(plus(1,1));
            printFloat(fplus(1,1+1));
            printString(splus("hello", "world"));
            
        }
        """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 481))

    def test_82(self):
        input = """
x: boolean = true;
main: function void() {}
y,z: string = "true", "1";
foo: function float(y: string) inherit main {
    preventDefault();
    i:integer;
    for (i = y, i < z, i) {
        while (i) {
            if (z) {
                do {
                    return h;
                }
                while (y != z);
            }
        }
    }
}
        """
        output = "Type mismatch in expression: BinExpr(<, Id(i), Id(z))"
        self.assertTrue(TestChecker.test(input, output, 482))

    def test_83(self):
        input = """
x: boolean = true;
main: function void() {
    a,b:integer;
    lst:float;
    a = b - a;
    b = a - b;
    lst = a + b;
    return lst/x;
}        """
        output = "Type mismatch in expression: BinExpr(/, Id(lst), Id(x))"
        self.assertTrue(TestChecker.test(input, output, 483))

    def test_84(self):
        input = """
x: integer = 100;
main: function void() {
    a,b:integer;
    lst:float;
    a = b - a;
    b = a - b;
    lst = a + b;
    return lst/x;
}        """
        output = "Type mismatch in statement: ReturnStmt(BinExpr(/, Id(lst), Id(x)))"
        self.assertTrue(TestChecker.test(input, output, 484))

    def test_85(self):
        input = """
a,b:array [2] of integer;
main: function void() {
    a[3] = b[2];
}       """
        output = "Type mismatch in expression: ArrayCell(a, [IntegerLit(3)])"
        self.assertTrue(TestChecker.test(input, output, 485))

    def test_86(self):
        input = """
x: boolean = true;
main: function void() {
    while (true) break;
}      """
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 486))

    def test_87(self):
        input = """
x: boolean = true;
main: function void() {
    if (x) if (x) if (x) if (x) if (x) if (x) if (x) break;
}     """
        output = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, output, 487))

    def test_88(self):
        input = """
x: boolean = true;
main: function void() {
    i:integer;
    for (i = 1, x, x) if (x) if (x) break;
}     """
        output = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), Id(x), Id(x), IfStmt(Id(x), IfStmt(Id(x), BreakStmt())))"
        self.assertTrue(TestChecker.test(input, output, 488))

    def test_89(self):
        input = """
isLeapYear: function boolean(year:integer) {
    return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
}     
main:function void() {
    isLeapYear:integer = 2023;
    isLeapYear(isLeapYear);
}
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 489))

    def test_90(self):
        input = """
isLeapYear: function boolean(year:integer) {
    return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
}     
main:function void() {
    year:integer = readInteger();
    if (isLeapYear(year)) printString("Leap year"); else printString("Not a leap year");
}
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 490))

    def test_91(self):
        input = """
month: integer = readInteger();
DayOfWeek: function string(month:integer) {
    a: array[12] of string = {"Jan", "Feb", "Mar", "Apr", "May","Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
    return a[month];
}
"""
        output = "No entry point"
        self.assertTrue(TestChecker.test(input, output, 491))

    def test_92(self):
        input = """
day: integer = readInteger();
DayOfWeek: function string(inherit day:integer) {
    if (day == 0) return "Sunday";
    else if (day == 1) return "Monday";
    else if (day == 1) return "Tuesday";
    else if (day == 1) return "Wednesday";
    else if (day == 1) return "Thursday";
    else if (day == 1) return "Friday";
    else if (day == 1) return "Saturday";
}
"""
        output = "No entry point"
        self.assertTrue(TestChecker.test(input, output, 492))

    def test_93(self):
        input = """
a:array[100] of integer;
min: function integer(a: array[1] of integer) {
    min,i: integer = a[0],0;
    
    for (i = 0, i < 100, 1) {
        if (a[i] < min) min = a[i];
    }
    return a[i];
}
"""
        output = "No entry point"
        self.assertTrue(TestChecker.test(input, output, 493))

    def test_94(self):
        input = """
a:array[100] of integer;
min: function integer(as: array[100] of integer) {
    min,i: integer = as[0],0;
    
    for (i = 0, i < 100, 1) {
        if (as[i] < min) min = as[i];
    }
    return as[i];
}
main: function void() {
    printInteger(min(a));
}
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 494))

    def test_95(self):
        input = """
a:array[100] of integer;
min: function integer(a: array[100] of integer) {
    min,i: integer = a[0],0;
    
    for (i = 0, i < 100, 1) {
        if (a[i] < min) min = a[i];
    }
    return a[i];
}
main: function void() {
    printInteger(min(a));
}
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 495))

    def test_96(self):
        input = """
x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 496))

    def test_97(self):
        input = """
swap: function void (out x: integer, out y: integer) {
    temp: integer = x;
    x = y;
    y = temp;
    return;
}
bubbleSort: function void (out a: array[2] of integer, size: integer) {
    i,j: integer;
    for (i = 1, i < size-1, 1) {
        for (j = i+1, j < size, 1) {
            if (a[i] < a[j]) swap(a[i], a[j]);
        } 
    }
    return;
}
main: function void(){
    n: integer = readInteger();
    a: array[10] of integer = {1,2,3,4,5,6,7,8,9,10};
    bubbleSort(a, n);
}
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 497))

    def test_98(self):
        input = """
pascalTri: function integer(a: integer, b: integer){
            if ((a == 0) || (a == b)) return 1;
            return pascalTri(a - 1, b - 1) + pascalTri(a - 1, b);
        }
        main: function void(){
            input1, input2: integer = 5, 3;
            printInteger(pascalTri(input1, input2));
        }
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 498))

    def test_99(self):
        input = """
pascalTri: function float(a: integer, b: integer){
            if ((a == 0) || (a == b)) return 1;
            return pascalTri(a - 1, b - 1) + pascalTri(a - 1, b);
        }
        main: function void(){
            input1, input2: integer = 5, 3;
            printFloat(pascalTri(input1, input2));
        }
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 499))

    def test_100(self):
        input = """
    foo:function integer(a:auto) {
        return a + 1;
    }        
    
    main:function void () {
        x:string;
        y: integer;
        
        foo(x);
        foo(y);
    }
        
"""
        output = "None"
        self.assertTrue(TestChecker.test(input, output, 500))