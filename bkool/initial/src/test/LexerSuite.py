import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_single_string(self):
        self.assertTrue(TestLexer.test("12", "12,<EOF>",101))
    def test_complex_string(self):
        self.assertTrue(TestLexer.test("13", "Error Token 1", 102))
    def test_complex_string_2(self):
        self.assertTrue(TestLexer.test("21A", "21A,<EOF>", 103))
    def test_complex_string_3(self):
        self.assertTrue(TestLexer.test("1B", "Error Token 1", 104))
 