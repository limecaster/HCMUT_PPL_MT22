# Generated from d:\PPL\bkool\initial\src\main\bkool\parser\MiniPHP.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("s\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\6\23Y\n\23\r\23\16\23Z\3\24\6\24^\n\24\r\24\16\24_\3")
        buf.write("\24\3\24\6\24d\n\24\r\24\16\24e\3\25\6\25i\n\25\r\25\16")
        buf.write("\25j\3\26\3\26\3\26\3\26\3\27\3\27\3\27\2\2\30\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30\3\2\5\3\2\62")
        buf.write(";\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2v\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\3/\3\2\2\2\5\65")
        buf.write("\3\2\2\2\7\67\3\2\2\2\t9\3\2\2\2\13;\3\2\2\2\r=\3\2\2")
        buf.write("\2\17?\3\2\2\2\21B\3\2\2\2\23E\3\2\2\2\25G\3\2\2\2\27")
        buf.write("I\3\2\2\2\31K\3\2\2\2\33M\3\2\2\2\35O\3\2\2\2\37Q\3\2")
        buf.write("\2\2!S\3\2\2\2#U\3\2\2\2%X\3\2\2\2\']\3\2\2\2)h\3\2\2")
        buf.write("\2+l\3\2\2\2-p\3\2\2\2/\60\7c\2\2\60\61\7t\2\2\61\62\7")
        buf.write("t\2\2\62\63\7c\2\2\63\64\7{\2\2\64\4\3\2\2\2\65\66\7?")
        buf.write("\2\2\66\6\3\2\2\2\678\7=\2\28\b\3\2\2\29:\7*\2\2:\n\3")
        buf.write("\2\2\2;<\7+\2\2<\f\3\2\2\2=>\7.\2\2>\16\3\2\2\2?@\7?\2")
        buf.write("\2@A\7@\2\2A\20\3\2\2\2BC\7,\2\2CD\7,\2\2D\22\3\2\2\2")
        buf.write("EF\7\60\2\2F\24\3\2\2\2GH\7,\2\2H\26\3\2\2\2IJ\7\61\2")
        buf.write("\2J\30\3\2\2\2KL\7\'\2\2L\32\3\2\2\2MN\7-\2\2N\34\3\2")
        buf.write("\2\2OP\7/\2\2P\36\3\2\2\2QR\7A\2\2R \3\2\2\2ST\5)\25\2")
        buf.write("T\"\3\2\2\2UV\5)\25\2V$\3\2\2\2WY\t\2\2\2XW\3\2\2\2YZ")
        buf.write("\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[&\3\2\2\2\\^\t\2\2\2]\\\3")
        buf.write("\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ac\7\60")
        buf.write("\2\2bd\t\2\2\2cb\3\2\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2")
        buf.write("f(\3\2\2\2gi\t\3\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3")
        buf.write("\2\2\2k*\3\2\2\2lm\t\4\2\2mn\3\2\2\2no\b\26\2\2o,\3\2")
        buf.write("\2\2pq\13\2\2\2qr\b\27\3\2r.\3\2\2\2\7\2Z_ej\4\b\2\2\3")
        buf.write("\27\2")
        return buf.getvalue()


class MiniPHPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY = 1
    EQ = 2
    SEMI = 3
    LP = 4
    RP = 5
    COMMA = 6
    ARROW = 7
    DSTAR = 8
    DOT = 9
    MUL = 10
    DIV = 11
    MOD = 12
    ADD = 13
    SUB = 14
    DQUES = 15
    PAIRNAME = 16
    VARNAME = 17
    INTLIT = 18
    FLOATLIT = 19
    STRINGLIT = 20
    WS = 21
    ERROR_CHAR = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'='", "';'", "'('", "')'", "','", "'=>'", "'**'", 
            "'.'", "'*'", "'/'", "'%'", "'+'", "'-'", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAY", "EQ", "SEMI", "LP", "RP", "COMMA", "ARROW", "DSTAR", 
            "DOT", "MUL", "DIV", "MOD", "ADD", "SUB", "DQUES", "PAIRNAME", 
            "VARNAME", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "ARRAY", "EQ", "SEMI", "LP", "RP", "COMMA", "ARROW", "DSTAR", 
                  "DOT", "MUL", "DIV", "MOD", "ADD", "SUB", "DQUES", "PAIRNAME", 
                  "VARNAME", "INTLIT", "FLOATLIT", "STRINGLIT", "WS", "ERROR_CHAR" ]

    grammarFileName = "MiniPHP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[21] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


