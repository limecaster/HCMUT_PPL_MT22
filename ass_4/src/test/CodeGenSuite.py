import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_0(self):
        input = """main:function void() {
            printString(\"101haha\");
        }"""
        output = """101haha
"""
        self.assertTrue(TestCodeGen.test(input, output, 500))

    def test_1(self):
        input = """main:function void() {
            printInteger(10101);
        }"""
        output = """10101
"""
        self.assertTrue(TestCodeGen.test(input, output, 501))
    
    def test_2(self):
        input = """main:function void() {
            printString(\"He asked me: \\"Where is John?\\"\");
        }"""
        output = """He asked me: \"Where is John?\"
"""
        self.assertTrue(TestCodeGen.test(input, output, 502))
        
    def test_3(self):
        input = """main:function void() {
            printInteger(100000000);
        }"""
        output = """100000000
"""
        self.assertTrue(TestCodeGen.test(input, output, 503))
    
    def test_4(self):
        input = """
        x:integer;
        y:string = "abc";
        main:function void() {
            x:integer = 10;
            printInteger(x);
        }"""
        output = """10
"""
        self.assertTrue(TestCodeGen.test(input, output, 504))
        
    def test_5(self):
        input = """
        //x:integer = 1;
        x:array [4] of integer = {10,20,30,40};
        main:function void() {
            i:integer;
            for (i = 0, i < 4, 1) {
                printInteger(x[i]);
            }
        }"""
        output = """10\n20\n30\n40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 505))
    
    def test_6(self):
        input = """
        //str:string = "abc" :: "123";
        
        main:function void() {
            str:string;
            str = "abc" :: "123" :: "ehe";
            printString(str);
        }"""
        output = """abc123ehe
"""
        self.assertTrue(TestCodeGen.test(input, output, 506))
        
    def test_7(self):
        input = """
        main:function void() {
            printInteger(12301%162);
        }"""
        output = """151
"""
        self.assertTrue(TestCodeGen.test(input, output, 507))
    
    def test_8(self):
        input = """
        main:function void() {
            printFloat(12412/523);
        }"""
        output = """23.732313
"""
        self.assertTrue(TestCodeGen.test(input, output, 508))
        
    def test_9(self):
        input = """
        main:function void() {
            
            printBoolean(!false);
        }"""
        output = """true
"""
        self.assertTrue(TestCodeGen.test(input, output, 509))
    
    def test_10(self):
        input = """
        main:function void() {
            x:integer = 1;
            while (true) {
                x = x + 1;
                if (x == 10) break;
            }
            printInteger(x);
        }"""
        output = """10
"""
        self.assertTrue(TestCodeGen.test(input, output, 510))
        
    def test_11(self):
        input = """
        main:function void() {
            x:integer = 1;
            do {
                x = x + 1;
            } while(x < 10);
            printInteger(x);
        }"""
        output = """10
"""
        self.assertTrue(TestCodeGen.test(input, output, 511))
    
    def test_12(self):
        input = """
        main:function void() {
            x,i:integer = 1, 0;
            for (i = 1, i < 100, 1) x = x + 1;
            printInteger(x);
        }"""
        output = """100
"""
        self.assertTrue(TestCodeGen.test(input, output, 512))
    
    def test_13(self):
        input = """
        x:integer;
        main:function void() {
            x = 123;
            printInteger(x);
        }"""
        output = """123
"""
        self.assertTrue(TestCodeGen.test(input, output, 513))
    
    def test_14(self):
        input = """
        x:array [4] of integer;
        main:function void() {
            x[0] = 10;
            x[1] = 20;
            x[2] = 30;
            x[3] = 40;
            i: integer;
            for (i = 0, i < 4, 1) {
                printFloat(x[i]);
            }
        }"""
        output = """10.0\n20.0\n30.0\n40.0\n"""
        self.assertTrue(TestCodeGen.test(input, output, 514))
        
    def test_15(self):
        input = """
        x:array [4] of integer;
        main:function void() {
            x[0] = 10;
            x[1] = 20;
            x[2] = 30;
            x[3] = 40;
            i: integer = x[0];
            printInteger(i);
            for (i = 0, i < 4, 1) {
                printInteger(x[i]);
            }
        }"""
        output = """10\n10\n20\n30\n40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 515))
        
    def test_16(self):
        input = """
        self:function float(x:float) {
            return x;
        }
        main:function void() {
            printFloat(self(10));
        }"""
        output = """10.0\n"""
        self.assertTrue(TestCodeGen.test(input, output, 516))
    
    def test_17(self):
        input = """
        x:auto = 10;
        main:function void() {
            printInteger(x);
        }"""
        output = """10\n"""
        self.assertTrue(TestCodeGen.test(input, output, 517))

    def test_18(self):
        input = """
        x:array[2,2] of integer;
        main:function void() {
            i,j:integer;
            for (i = 0, i < 2, 1) {
                for (j = 0, j < 2, 1) {
                    x[i,j] = 4;
                }
            }
            printInteger(x[1,1]);
        }"""
        output = """4\n"""
        self.assertTrue(TestCodeGen.test(input, output, 518))
    
    def test_19(self):
        input = """
        main:function void() {
            i,j:integer;
            x:array[2] of integer = {10,40};
            
            printInteger(x[1]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 519))
    
    def test_20(self):
        input = """
        main:function void() {
            x:integer;
            for (x = 1, x < 15, 1) continue;    
            printInteger(x);
        }"""
        output = """15\n"""
        self.assertTrue(TestCodeGen.test(input, output, 520))
    def test_21(self):
        input = """
        main:function void() {
            arr:array[1,1,1,1] of integer = {{{{40}}}};
            
            printInteger(arr[0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 521))
    
    def test_22(self):
        input = """
        main:function void() {
            arr:array[1,1,1,1,1] of integer = {{{{{40}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 522))
    
    def test_23(self):
        input = """
        main:function void() {
            arr:array[1,1,1,1,1] of integer = {{{{{40}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 523))
        
    def test_24(self):
        input = """
        main:function void() {
            arr:array[1,1,1,1,2] of integer = {{{{{40,50}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 524))
        
    def test_25(self):
        input = """
        main:function void() {
            arr:array[1,1,1,2,2] of integer = {{{{{40,50},{60,70}}}}};
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 525))
    
    def test_26(self):
        input = """
        arr:array[1,1,1,2,2] of integer = {{{{{40,50},{60,70}}}}};
        
        main:function void() {
            
            printInteger(arr[0,0,0,0,0]);
        }"""
        output = """40\n"""
        self.assertTrue(TestCodeGen.test(input, output, 526))
        
    def test_27(self):
        input = """
        FactorialRecursive:function integer(x:integer){
            if (x == 1) return 1;
            return FactorialRecursive(x-1)*x;
        }
        main:function void() {
            x:integer = 10;
            printInteger(FactorialRecursive(x));
        }"""
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 527))
        
    def test_28(self):
        input = """
        FactorialRecursive:function integer(x:integer){
            if (x == 1) return 1;
            return FactorialRecursive(x-1)*x;
        }
        main:function void() {
            x:auto = 10;
            printInteger(FactorialRecursive(x));
        }"""
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 528))\
    
    def test_29(self):
        input = """
        x:auto = 10;
        
        main:function void() {
            printInteger(FactorialRecursive(x));
        }
        FactorialRecursive:function integer(x:integer){
            if (x == 1) return 1;
            return FactorialRecursive(x-1)*x;
        }"""
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 529))
    
    def test_30(self):
        input = """
        
        FactorialRecursive:function integer(x:integer){
            if (x == 1) return 1;
            return FactorialRecursive(x-1)*x;
        }
        main:function void() {
            x:auto = 10;
            printInteger(FactorialRecursive(x));
        }
        x:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 530))
                
    def test_31(self):
        input = """
        
        FactorialRecursive:function integer(x:integer){
            if (x == 1) return 1;
            return FactorialRecursive(x-1)*x;
        }
        main:function void() {
            x:auto = 10;
            printInteger(FactorialRecursive(x));
        }
        x:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 531))
    
                        
    def test_32(self):
        input = """
        
        isLeapYear: function boolean(year:integer) {
return (year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0));
}     
main:function void() {
isLeapYear:integer = 2020;
printBoolean(isLeapYear(isLeapYear));
}          
        """
        output = """true\n"""
        self.assertTrue(TestCodeGen.test(input, output, 532))
    def test_32(self):
        input = """
//days: integer = readInteger();
days:integer = 10;
DayOfWeek: function string(day:integer) {
if (day == 0) return "Sunday";
else if (day == 1) return "Monday";
else if (day == 2) return "Tuesday";
else if (day == 3) return "Wednesday";
else if (day == 4) return "Thursday";
else if (day == 5) return "Friday";
else if (day == 6) return "Saturday";
return "Wrong day range";
}
main:function void() {
printString(DayOfWeek(days));
}         
        """
        output = """Wrong day range\n"""
        self.assertTrue(TestCodeGen.test(input, output, 532))
    
    def test_33(self):
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
        output = """71\n"""
        self.assertTrue(TestCodeGen.test(input, output, 533))
        
    def test_34(self):
        input = """
    main: function void() {
        i: integer;
        for (i = 1, i < 10, 1) {
            if (i % 2 == 0) continue;
            printInteger(i); 
        }
    }       
        """
        output = """1\n3\n5\n7\n9\n"""
        self.assertTrue(TestCodeGen.test(input, output, 534))
        
    def test_35(self):
        input = """
    main: function void() {
        i: integer = 0;
        while (i < 10) {
            i = i + 1; 
            if (i % 2 == 0) continue;
            printInteger(i);
        }
    }       
        """
        output = """1\n3\n5\n7\n9\n"""
        self.assertTrue(TestCodeGen.test(input, output, 535))
    
    def test_36(self):
        input = """
    main: function void() {
        i: integer = 0;
        do {
            i = i + 1; 
            if (i % 2 == 0) continue;
            printInteger(i);
        } while (i < 10);
    }       
        """
        output = """1\n3\n5\n7\n9\n"""
        self.assertTrue(TestCodeGen.test(input, output, 536))
    
    def test_37(self):
        input = """
    foo:function auto(a:integer){
        return a;
    }    
    main:function void() {
        printInteger(foo(10));
    }
        """
        output = """10\n"""
        self.assertTrue(TestCodeGen.test(input, output, 537))
        
    def test_38(self):
        input = """
        
        FactorialRecursive:function auto(x:integer){
            if (x == 1) return 1;
            return FactorialRecursive(x-1)*x;
        }
        main:function void() {
            x:auto = 10;
            printInteger(FactorialRecursive(x));
        }
        x:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 538))
    
    def test_39(self):
        input = """
        
        FactorialRecursive:function integer(x:auto){
            if (x == 1) return 1;
            return FactorialRecursive(x-1)*x;
        }
        main:function void() {
            x:auto = 10;
            printInteger(FactorialRecursive(x));
        }
        x:auto = 5;
        
        """
        output = """3628800\n"""
        self.assertTrue(TestCodeGen.test(input, output, 539))
            