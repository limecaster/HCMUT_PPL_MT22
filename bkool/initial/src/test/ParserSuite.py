import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program:"""
        input = """abc = 1 + 2 ?? 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_simple_program_2(self):
        """Simple program:"""
        input = """abc = 1 + 2 ?? 3;
u = array(a1 => 3 . 4, a2 => 3 + (u2 % 5));"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    