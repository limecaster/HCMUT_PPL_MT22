# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u020f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\5\2\u008d\n\2\3\2\6\2\u0090\n\2\r")
        buf.write("\2\16\2\u0091\7\2\u0094\n\2\f\2\16\2\u0097\13\2\3\2\3")
        buf.write("\2\5\2\u009b\n\2\3\3\3\3\5\3\u009f\n\3\3\4\3\4\5\4\u00a3")
        buf.write("\n\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00ab\n\4\3\4\3\4\3\4")
        buf.write("\5\4\u00b0\n\4\3\4\3\4\3\4\3\4\5\4\u00b6\n\4\3\5\3\5\3")
        buf.write("\5\7\5\u00bb\n\5\f\5\16\5\u00be\13\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)")
        buf.write("\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\7\65\u017b")
        buf.write("\n\65\f\65\16\65\u017e\13\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\5:\u018a\n:\3:\6:\u018d\n:\r:\16:\u018e")
        buf.write("\7:\u0191\n:\f:\16:\u0194\13:\3;\3;\7;\u0198\n;\f;\16")
        buf.write(";\u019b\13;\3<\3<\5<\u019f\n<\3<\6<\u01a2\n<\r<\16<\u01a3")
        buf.write("\3<\3<\5<\u01a8\n<\3<\6<\u01ab\n<\r<\16<\u01ac\5<\u01af")
        buf.write("\n<\3=\3=\3=\3>\6>\u01b5\n>\r>\16>\u01b6\3>\3>\3?\3?\3")
        buf.write("?\3?\7?\u01bf\n?\f?\16?\u01c2\13?\3?\3?\3?\3?\3?\3@\3")
        buf.write("@\3@\3@\7@\u01cd\n@\f@\16@\u01d0\13@\3@\3@\3A\3A\3A\7")
        buf.write("A\u01d7\nA\fA\16A\u01da\13A\3A\3A\3A\3A\3A\3B\3B\3B\7")
        buf.write("B\u01e4\nB\fB\16B\u01e7\13B\3B\5B\u01ea\nB\3B\3B\3C\3")
        buf.write("C\3C\3D\3D\7D\u01f3\nD\fD\16D\u01f6\13D\3D\3D\6D\u01fa")
        buf.write("\nD\rD\16D\u01fb\3D\7D\u01ff\nD\fD\16D\u0202\13D\3D\6")
        buf.write("D\u0205\nD\rD\16D\u0206\7D\u0209\nD\fD\16D\u020c\13D\3")
        buf.write("D\3D\5\u00bc\u01c0\u01d8\2E\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\2m\2o\2q\2s\2u\2w\2y\2{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\3\2\r\6\2\f\f\17\17$$^^\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2--//\n\2$$))^^")
        buf.write("ddhhppttvv\5\2\n\f\16\17\"\"\4\2\f\f\17\17\t\2$$))^^d")
        buf.write("dhhttvv\3\3\f\f\2\u0229\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\3\u009a\3\2\2\2\5\u009e")
        buf.write("\3\2\2\2\7\u00b5\3\2\2\2\t\u00b7\3\2\2\2\13\u00c2\3\2")
        buf.write("\2\2\r\u00c7\3\2\2\2\17\u00cd\3\2\2\2\21\u00d3\3\2\2\2")
        buf.write("\23\u00db\3\2\2\2\25\u00de\3\2\2\2\27\u00e3\3\2\2\2\31")
        buf.write("\u00e9\3\2\2\2\33\u00ef\3\2\2\2\35\u00f3\3\2\2\2\37\u00fc")
        buf.write("\3\2\2\2!\u00ff\3\2\2\2#\u0107\3\2\2\2%\u010e\3\2\2\2")
        buf.write("\'\u0115\3\2\2\2)\u011a\3\2\2\2+\u011f\3\2\2\2-\u0125")
        buf.write("\3\2\2\2/\u0129\3\2\2\2\61\u0132\3\2\2\2\63\u0135\3\2")
        buf.write("\2\2\65\u013d\3\2\2\2\67\u013f\3\2\2\29\u0141\3\2\2\2")
        buf.write(";\u0143\3\2\2\2=\u0145\3\2\2\2?\u0147\3\2\2\2A\u0149\3")
        buf.write("\2\2\2C\u014c\3\2\2\2E\u014f\3\2\2\2G\u0152\3\2\2\2I\u0155")
        buf.write("\3\2\2\2K\u0157\3\2\2\2M\u015a\3\2\2\2O\u015c\3\2\2\2")
        buf.write("Q\u015f\3\2\2\2S\u0162\3\2\2\2U\u0164\3\2\2\2W\u0166\3")
        buf.write("\2\2\2Y\u0168\3\2\2\2[\u016a\3\2\2\2]\u016c\3\2\2\2_\u016e")
        buf.write("\3\2\2\2a\u0170\3\2\2\2c\u0172\3\2\2\2e\u0174\3\2\2\2")
        buf.write("g\u0176\3\2\2\2i\u0178\3\2\2\2k\u017f\3\2\2\2m\u0181\3")
        buf.write("\2\2\2o\u0183\3\2\2\2q\u0185\3\2\2\2s\u0187\3\2\2\2u\u0195")
        buf.write("\3\2\2\2w\u01ae\3\2\2\2y\u01b0\3\2\2\2{\u01b4\3\2\2\2")
        buf.write("}\u01ba\3\2\2\2\177\u01c8\3\2\2\2\u0081\u01d3\3\2\2\2")
        buf.write("\u0083\u01e0\3\2\2\2\u0085\u01ed\3\2\2\2\u0087\u01f0\3")
        buf.write("\2\2\2\u0089\u009b\7\62\2\2\u008a\u0095\5m\67\2\u008b")
        buf.write("\u008d\7a\2\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2\2")
        buf.write("\u008d\u008f\3\2\2\2\u008e\u0090\5k\66\2\u008f\u008e\3")
        buf.write("\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u008c\3\2\2\2\u0094")
        buf.write("\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\b")
        buf.write("\2\2\2\u0099\u009b\3\2\2\2\u009a\u0089\3\2\2\2\u009a\u008a")
        buf.write("\3\2\2\2\u009b\4\3\2\2\2\u009c\u009f\5\'\24\2\u009d\u009f")
        buf.write("\5\27\f\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2\2\2\u009f")
        buf.write("\6\3\2\2\2\u00a0\u00a2\5s:\2\u00a1\u00a3\5u;\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a5\5w<\2\u00a5\u00a6\b\4\3\2\u00a6\u00b6\3\2\2\2\u00a7")
        buf.write("\u00a8\5s:\2\u00a8\u00aa\5u;\2\u00a9\u00ab\5w<\2\u00aa")
        buf.write("\u00a9\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\u00ad\b\4\4\2\u00ad\u00b6\3\2\2\2\u00ae\u00b0\5")
        buf.write("s:\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1")
        buf.write("\3\2\2\2\u00b1\u00b2\5u;\2\u00b2\u00b3\5w<\2\u00b3\u00b4")
        buf.write("\b\4\5\2\u00b4\u00b6\3\2\2\2\u00b5\u00a0\3\2\2\2\u00b5")
        buf.write("\u00a7\3\2\2\2\u00b5\u00af\3\2\2\2\u00b6\b\3\2\2\2\u00b7")
        buf.write("\u00bc\7$\2\2\u00b8\u00bb\5y=\2\u00b9\u00bb\n\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00bf\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\7$\2\2\u00c0\u00c1")
        buf.write("\b\5\6\2\u00c1\n\3\2\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7w\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7q\2\2\u00c6\f")
        buf.write("\3\2\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7{\2\2\u00cc\16")
        buf.write("\3\2\2\2\u00cd\u00ce\7d\2\2\u00ce\u00cf\7t\2\2\u00cf\u00d0")
        buf.write("\7g\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7m\2\2\u00d2\20")
        buf.write("\3\2\2\2\u00d3\u00d4\7d\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9")
        buf.write("\7c\2\2\u00d9\u00da\7p\2\2\u00da\22\3\2\2\2\u00db\u00dc")
        buf.write("\7f\2\2\u00dc\u00dd\7q\2\2\u00dd\24\3\2\2\2\u00de\u00df")
        buf.write("\7g\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7u\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2\26\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5")
        buf.write("\7c\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8\30\3\2\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb")
        buf.write("\7n\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\32\3\2\2\2\u00ef\u00f0\7h\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7t\2\2\u00f2\34\3\2\2\2\u00f3\u00f4")
        buf.write("\7h\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7")
        buf.write("\7e\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7q\2\2\u00fa\u00fb\7p\2\2\u00fb\36\3\2\2\2\u00fc\u00fd")
        buf.write("\7k\2\2\u00fd\u00fe\7h\2\2\u00fe \3\2\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103\u0104\7i\2\2\u0104\u0105\7g\2\2\u0105\u0106")
        buf.write("\7t\2\2\u0106\"\3\2\2\2\u0107\u0108\7t\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7v\2\2\u010a\u010b\7w\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7p\2\2\u010d$\3\2\2\2\u010e\u010f")
        buf.write("\7u\2\2\u010f\u0110\7v\2\2\u0110\u0111\7t\2\2\u0111\u0112")
        buf.write("\7k\2\2\u0112\u0113\7p\2\2\u0113\u0114\7i\2\2\u0114&\3")
        buf.write("\2\2\2\u0115\u0116\7v\2\2\u0116\u0117\7t\2\2\u0117\u0118")
        buf.write("\7w\2\2\u0118\u0119\7g\2\2\u0119(\3\2\2\2\u011a\u011b")
        buf.write("\7x\2\2\u011b\u011c\7q\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7f\2\2\u011e*\3\2\2\2\u011f\u0120\7y\2\2\u0120\u0121")
        buf.write("\7j\2\2\u0121\u0122\7k\2\2\u0122\u0123\7n\2\2\u0123\u0124")
        buf.write("\7g\2\2\u0124,\3\2\2\2\u0125\u0126\7q\2\2\u0126\u0127")
        buf.write("\7w\2\2\u0127\u0128\7v\2\2\u0128.\3\2\2\2\u0129\u012a")
        buf.write("\7e\2\2\u012a\u012b\7q\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d\u012e\7k\2\2\u012e\u012f\7p\2\2\u012f\u0130")
        buf.write("\7w\2\2\u0130\u0131\7g\2\2\u0131\60\3\2\2\2\u0132\u0133")
        buf.write("\7q\2\2\u0133\u0134\7h\2\2\u0134\62\3\2\2\2\u0135\u0136")
        buf.write("\7k\2\2\u0136\u0137\7p\2\2\u0137\u0138\7j\2\2\u0138\u0139")
        buf.write("\7g\2\2\u0139\u013a\7t\2\2\u013a\u013b\7k\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\64\3\2\2\2\u013d\u013e\7-\2\2\u013e\66\3")
        buf.write("\2\2\2\u013f\u0140\7/\2\2\u01408\3\2\2\2\u0141\u0142\7")
        buf.write(",\2\2\u0142:\3\2\2\2\u0143\u0144\7\61\2\2\u0144<\3\2\2")
        buf.write("\2\u0145\u0146\7\'\2\2\u0146>\3\2\2\2\u0147\u0148\7#\2")
        buf.write("\2\u0148@\3\2\2\2\u0149\u014a\7(\2\2\u014a\u014b\7(\2")
        buf.write("\2\u014bB\3\2\2\2\u014c\u014d\7~\2\2\u014d\u014e\7~\2")
        buf.write("\2\u014eD\3\2\2\2\u014f\u0150\7?\2\2\u0150\u0151\7?\2")
        buf.write("\2\u0151F\3\2\2\2\u0152\u0153\7#\2\2\u0153\u0154\7?\2")
        buf.write("\2\u0154H\3\2\2\2\u0155\u0156\7>\2\2\u0156J\3\2\2\2\u0157")
        buf.write("\u0158\7>\2\2\u0158\u0159\7?\2\2\u0159L\3\2\2\2\u015a")
        buf.write("\u015b\7@\2\2\u015bN\3\2\2\2\u015c\u015d\7@\2\2\u015d")
        buf.write("\u015e\7?\2\2\u015eP\3\2\2\2\u015f\u0160\7<\2\2\u0160")
        buf.write("\u0161\7<\2\2\u0161R\3\2\2\2\u0162\u0163\7*\2\2\u0163")
        buf.write("T\3\2\2\2\u0164\u0165\7+\2\2\u0165V\3\2\2\2\u0166\u0167")
        buf.write("\7]\2\2\u0167X\3\2\2\2\u0168\u0169\7_\2\2\u0169Z\3\2\2")
        buf.write("\2\u016a\u016b\7}\2\2\u016b\\\3\2\2\2\u016c\u016d\7\177")
        buf.write("\2\2\u016d^\3\2\2\2\u016e\u016f\7\60\2\2\u016f`\3\2\2")
        buf.write("\2\u0170\u0171\7.\2\2\u0171b\3\2\2\2\u0172\u0173\7=\2")
        buf.write("\2\u0173d\3\2\2\2\u0174\u0175\7<\2\2\u0175f\3\2\2\2\u0176")
        buf.write("\u0177\7?\2\2\u0177h\3\2\2\2\u0178\u017c\t\3\2\2\u0179")
        buf.write("\u017b\t\4\2\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2")
        buf.write("\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017dj\3\2\2")
        buf.write("\2\u017e\u017c\3\2\2\2\u017f\u0180\t\5\2\2\u0180l\3\2")
        buf.write("\2\2\u0181\u0182\t\6\2\2\u0182n\3\2\2\2\u0183\u0184\t")
        buf.write("\3\2\2\u0184p\3\2\2\2\u0185\u0186\t\7\2\2\u0186r\3\2\2")
        buf.write("\2\u0187\u0192\5k\66\2\u0188\u018a\7a\2\2\u0189\u0188")
        buf.write("\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b")
        buf.write("\u018d\5k\66\2\u018c\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0191\3")
        buf.write("\2\2\2\u0190\u0189\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193t\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0195\u0199\7\60\2\2\u0196\u0198\5k\66\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019av\3\2\2\2\u019b\u0199\3\2\2")
        buf.write("\2\u019c\u019e\7g\2\2\u019d\u019f\5q9\2\u019e\u019d\3")
        buf.write("\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u01a2")
        buf.write("\5k\66\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01af\3\2\2\2")
        buf.write("\u01a5\u01a7\7G\2\2\u01a6\u01a8\5q9\2\u01a7\u01a6\3\2")
        buf.write("\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01ab")
        buf.write("\5k\66\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2")
        buf.write("\u01ae\u019c\3\2\2\2\u01ae\u01a5\3\2\2\2\u01afx\3\2\2")
        buf.write("\2\u01b0\u01b1\7^\2\2\u01b1\u01b2\t\b\2\2\u01b2z\3\2\2")
        buf.write("\2\u01b3\u01b5\t\t\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01b9\b>\7\2\u01b9|\3\2\2\2\u01ba")
        buf.write("\u01bb\7\61\2\2\u01bb\u01bc\7,\2\2\u01bc\u01c0\3\2\2\2")
        buf.write("\u01bd\u01bf\13\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c2")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1")
        buf.write("\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\7,\2\2")
        buf.write("\u01c4\u01c5\7\61\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7")
        buf.write("\b?\7\2\u01c7~\3\2\2\2\u01c8\u01c9\7\61\2\2\u01c9\u01ca")
        buf.write("\7\61\2\2\u01ca\u01ce\3\2\2\2\u01cb\u01cd\n\n\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d1\u01d2\b@\7\2\u01d2\u0080\3\2\2\2\u01d3\u01d8")
        buf.write("\7$\2\2\u01d4\u01d7\5y=\2\u01d5\u01d7\n\2\2\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01db\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01db\u01dc\7^\2\2\u01dc\u01dd\n")
        buf.write("\13\2\2\u01dd\u01de\3\2\2\2\u01de\u01df\bA\b\2\u01df\u0082")
        buf.write("\3\2\2\2\u01e0\u01e5\7$\2\2\u01e1\u01e4\5y=\2\u01e2\u01e4")
        buf.write("\n\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4")
        buf.write("\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2")
        buf.write("\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8\u01ea\t")
        buf.write("\f\2\2\u01e9\u01e8\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb")
        buf.write("\3\2\2\2\u01eb\u01ec\bB\t\2\u01ec\u0084\3\2\2\2\u01ed")
        buf.write("\u01ee\13\2\2\2\u01ee\u01ef\bC\n\2\u01ef\u0086\3\2\2\2")
        buf.write("\u01f0\u01f4\5m\67\2\u01f1\u01f3\5k\66\2\u01f2\u01f1\3")
        buf.write("\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u020a\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7")
        buf.write("\u01f8\7a\2\2\u01f8\u01fa\7a\2\2\u01f9\u01f7\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u0200\3\2\2\2\u01fd\u01ff\7a\2\2\u01fe\u01fd\3")
        buf.write("\2\2\2\u01ff\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201")
        buf.write("\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0203")
        buf.write("\u0205\5k\66\2\u0204\u0203\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0209\3")
        buf.write("\2\2\2\u0208\u01f9\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020d\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u020e\bD\13\2\u020e\u0088\3\2\2\2")
        buf.write("%\2\u008c\u0091\u0095\u009a\u009e\u00a2\u00aa\u00af\u00b5")
        buf.write("\u00ba\u00bc\u017c\u0189\u018e\u0192\u0199\u019e\u01a3")
        buf.write("\u01a7\u01ac\u01ae\u01b6\u01c0\u01ce\u01d6\u01d8\u01e3")
        buf.write("\u01e5\u01e9\u01f4\u01fb\u0200\u0206\u020a\f\3\2\2\3\4")
        buf.write("\3\3\4\4\3\4\5\3\5\6\b\2\2\3A\7\3B\b\3C\t\3D\n")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IntegerLiteral = 1
    BooleanLiteral = 2
    FloatLiteral = 3
    StringLiteral = 4
    Auto = 5
    Array = 6
    Break = 7
    Boolean = 8
    Do = 9
    Else = 10
    False_ = 11
    Float = 12
    For = 13
    Function = 14
    If = 15
    Integer = 16
    Return = 17
    String = 18
    True_ = 19
    Void = 20
    While = 21
    Out = 22
    Continue = 23
    Of = 24
    Inherit = 25
    Plus = 26
    Minus = 27
    Star = 28
    Div = 29
    Mod = 30
    Not = 31
    AndAnd = 32
    OrOr = 33
    Equal = 34
    NotEqual = 35
    Less = 36
    LessEqual = 37
    Greater = 38
    GreaterEqual = 39
    Doublecolon = 40
    LeftParen = 41
    RightParen = 42
    LeftBracket = 43
    RightBracket = 44
    LeftBrace = 45
    RightBrace = 46
    Dot = 47
    Comma = 48
    Semicolon = 49
    Colon = 50
    Assign = 51
    Identifier = 52
    WhiteSpace = 53
    BlockComment = 54
    LineComment = 55
    ILLEGAL_ESCAPE = 56
    UNCLOSED_STRING = 57
    ERROR_CHAR = 58
    ERROR_INTLIT = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'array'", "'break'", "'boolean'", "'do'", "'else'", 
            "'false'", "'float'", "'for'", "'function'", "'if'", "'integer'", 
            "'return'", "'string'", "'true'", "'void'", "'while'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'.'", "','", "';'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "IntegerLiteral", "BooleanLiteral", "FloatLiteral", "StringLiteral", 
            "Auto", "Array", "Break", "Boolean", "Do", "Else", "False_", 
            "Float", "For", "Function", "If", "Integer", "Return", "String", 
            "True_", "Void", "While", "Out", "Continue", "Of", "Inherit", 
            "Plus", "Minus", "Star", "Div", "Mod", "Not", "AndAnd", "OrOr", 
            "Equal", "NotEqual", "Less", "LessEqual", "Greater", "GreaterEqual", 
            "Doublecolon", "LeftParen", "RightParen", "LeftBracket", "RightBracket", 
            "LeftBrace", "RightBrace", "Dot", "Comma", "Semicolon", "Colon", 
            "Assign", "Identifier", "WhiteSpace", "BlockComment", "LineComment", 
            "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ERROR_CHAR", "ERROR_INTLIT" ]

    ruleNames = [ "IntegerLiteral", "BooleanLiteral", "FloatLiteral", "StringLiteral", 
                  "Auto", "Array", "Break", "Boolean", "Do", "Else", "False_", 
                  "Float", "For", "Function", "If", "Integer", "Return", 
                  "String", "True_", "Void", "While", "Out", "Continue", 
                  "Of", "Inherit", "Plus", "Minus", "Star", "Div", "Mod", 
                  "Not", "AndAnd", "OrOr", "Equal", "NotEqual", "Less", 
                  "LessEqual", "Greater", "GreaterEqual", "Doublecolon", 
                  "LeftParen", "RightParen", "LeftBracket", "RightBracket", 
                  "LeftBrace", "RightBrace", "Dot", "Comma", "Semicolon", 
                  "Colon", "Assign", "Identifier", "DIGIT", "NONZERODIGIT", 
                  "NONDIGIT", "SIGN", "INTEGERPART", "DECIMALPART", "EXPONENTPART", 
                  "ESC_SEQUENCE", "WhiteSpace", "BlockComment", "LineComment", 
                  "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ERROR_CHAR", "ERROR_INTLIT" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.IntegerLiteral_action 
            actions[2] = self.FloatLiteral_action 
            actions[3] = self.StringLiteral_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[64] = self.UNCLOSED_STRING_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.ERROR_INTLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def IntegerLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FloatLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

    def StringLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.text = self.text[1:-1];
              
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     

    def ERROR_INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise ErrorToken(self.text)
     


