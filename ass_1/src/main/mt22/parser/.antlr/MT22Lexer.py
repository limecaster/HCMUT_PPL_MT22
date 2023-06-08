# Generated from d:\PPL\ass_1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\u01f1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\5\3\u0092\n\3")
        buf.write("\3\3\6\3\u0095\n\3\r\3\16\3\u0096\7\3\u0099\n\3\f\3\16")
        buf.write("\3\u009c\13\3\3\3\3\3\5\3\u00a0\n\3\3\4\3\4\5\4\u00a4")
        buf.write("\n\4\3\5\3\5\5\5\u00a8\n\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u00b0\n\5\3\5\3\5\5\5\u00b4\n\5\3\6\3\6\3\6\3\6\7\6\u00ba")
        buf.write("\n\6\f\6\16\6\u00bd\13\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\7\66\u017a\n\66\f\66")
        buf.write("\16\66\u017d\13\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\5")
        buf.write(";\u0189\n;\3;\7;\u018c\n;\f;\16;\u018f\13;\7;\u0191\n")
        buf.write(";\f;\16;\u0194\13;\3<\3<\7<\u0198\n<\f<\16<\u019b\13<")
        buf.write("\3=\3=\5=\u019f\n=\3=\6=\u01a2\n=\r=\16=\u01a3\3=\3=\5")
        buf.write("=\u01a8\n=\3=\6=\u01ab\n=\r=\16=\u01ac\5=\u01af\n=\3>")
        buf.write("\3>\3>\3?\6?\u01b5\n?\r?\16?\u01b6\3?\3?\3@\3@\3@\3@\7")
        buf.write("@\u01bf\n@\f@\16@\u01c2\13@\3@\3@\3@\3@\3@\3A\3A\3A\3")
        buf.write("A\7A\u01cd\nA\fA\16A\u01d0\13A\3A\3A\3B\3B\3B\3B\7B\u01d8")
        buf.write("\nB\fB\16B\u01db\13B\3B\3B\3B\5B\u01e0\nB\3B\3B\3C\3C")
        buf.write("\3C\3C\7C\u01e8\nC\fC\16C\u01eb\13C\3C\3C\3D\3D\3D\6\u00bb")
        buf.write("\u01c0\u01d9\u01e9\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m\2o\2q\2s\2u\2w\2y\2{\2}8\1779\u0081:\u0083")
        buf.write(";\u0085<\u0087=\3\2\13\n\2$$))^^ddhhppttvv\4\2\f\f\17")
        buf.write("\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2--//")
        buf.write("\5\2\n\f\16\17\"\"\6\2\13\f\17\17$$^^\2\u0204\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\3\u0089\3\2\2\2\5\u009f\3\2\2\2\7\u00a3\3\2\2\2\t\u00b3")
        buf.write("\3\2\2\2\13\u00b5\3\2\2\2\r\u00c1\3\2\2\2\17\u00c6\3\2")
        buf.write("\2\2\21\u00cc\3\2\2\2\23\u00d2\3\2\2\2\25\u00da\3\2\2")
        buf.write("\2\27\u00dd\3\2\2\2\31\u00e2\3\2\2\2\33\u00e8\3\2\2\2")
        buf.write("\35\u00ee\3\2\2\2\37\u00f2\3\2\2\2!\u00fb\3\2\2\2#\u00fe")
        buf.write("\3\2\2\2%\u0106\3\2\2\2\'\u010d\3\2\2\2)\u0114\3\2\2\2")
        buf.write("+\u0119\3\2\2\2-\u011e\3\2\2\2/\u0124\3\2\2\2\61\u0128")
        buf.write("\3\2\2\2\63\u0131\3\2\2\2\65\u0134\3\2\2\2\67\u013c\3")
        buf.write("\2\2\29\u013e\3\2\2\2;\u0140\3\2\2\2=\u0142\3\2\2\2?\u0144")
        buf.write("\3\2\2\2A\u0146\3\2\2\2C\u0148\3\2\2\2E\u014b\3\2\2\2")
        buf.write("G\u014e\3\2\2\2I\u0151\3\2\2\2K\u0154\3\2\2\2M\u0156\3")
        buf.write("\2\2\2O\u0159\3\2\2\2Q\u015b\3\2\2\2S\u015e\3\2\2\2U\u0161")
        buf.write("\3\2\2\2W\u0163\3\2\2\2Y\u0165\3\2\2\2[\u0167\3\2\2\2")
        buf.write("]\u0169\3\2\2\2_\u016b\3\2\2\2a\u016d\3\2\2\2c\u016f\3")
        buf.write("\2\2\2e\u0171\3\2\2\2g\u0173\3\2\2\2i\u0175\3\2\2\2k\u0177")
        buf.write("\3\2\2\2m\u017e\3\2\2\2o\u0180\3\2\2\2q\u0182\3\2\2\2")
        buf.write("s\u0184\3\2\2\2u\u0186\3\2\2\2w\u0195\3\2\2\2y\u01ae\3")
        buf.write("\2\2\2{\u01b0\3\2\2\2}\u01b4\3\2\2\2\177\u01ba\3\2\2\2")
        buf.write("\u0081\u01c8\3\2\2\2\u0083\u01d3\3\2\2\2\u0085\u01e3\3")
        buf.write("\2\2\2\u0087\u01ee\3\2\2\2\u0089\u008a\7o\2\2\u008a\u008b")
        buf.write("\7c\2\2\u008b\u008c\7k\2\2\u008c\u008d\7p\2\2\u008d\4")
        buf.write("\3\2\2\2\u008e\u00a0\7\62\2\2\u008f\u009a\5o8\2\u0090")
        buf.write("\u0092\7a\2\2\u0091\u0090\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\u0094\3\2\2\2\u0093\u0095\5m\67\2\u0094\u0093\3")
        buf.write("\2\2\2\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u0091\3\2\2\2\u0099")
        buf.write("\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\b")
        buf.write("\3\2\2\u009e\u00a0\3\2\2\2\u009f\u008e\3\2\2\2\u009f\u008f")
        buf.write("\3\2\2\2\u00a0\6\3\2\2\2\u00a1\u00a4\5)\25\2\u00a2\u00a4")
        buf.write("\5\31\r\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\b\3\2\2\2\u00a5\u00a7\5u;\2\u00a6\u00a8\5w<\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00aa\5y=\2\u00aa\u00ab\b\5\3\2\u00ab\u00b4\3\2\2\2\u00ac")
        buf.write("\u00ad\5u;\2\u00ad\u00af\5w<\2\u00ae\u00b0\5y=\2\u00af")
        buf.write("\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1\u00b2\b\5\4\2\u00b2\u00b4\3\2\2\2\u00b3\u00a5\3")
        buf.write("\2\2\2\u00b3\u00ac\3\2\2\2\u00b4\n\3\2\2\2\u00b5\u00bb")
        buf.write("\7$\2\2\u00b6\u00b7\7^\2\2\u00b7\u00ba\t\2\2\2\u00b8\u00ba")
        buf.write("\n\3\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bd\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2")
        buf.write("\u00bc\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\7")
        buf.write("$\2\2\u00bf\u00c0\b\6\5\2\u00c0\f\3\2\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7v\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\16\3\2\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7{\2\2\u00cb\20\3\2\2\2\u00cc\u00cd\7d\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7m\2\2\u00d1\22\3\2\2\2\u00d2\u00d3\7d\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7p\2\2\u00d9\24")
        buf.write("\3\2\2\2\u00da\u00db\7f\2\2\u00db\u00dc\7q\2\2\u00dc\26")
        buf.write("\3\2\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7n\2\2\u00df\u00e0")
        buf.write("\7u\2\2\u00e0\u00e1\7g\2\2\u00e1\30\3\2\2\2\u00e2\u00e3")
        buf.write("\7h\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6")
        buf.write("\7u\2\2\u00e6\u00e7\7g\2\2\u00e7\32\3\2\2\2\u00e8\u00e9")
        buf.write("\7h\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7c\2\2\u00ec\u00ed\7v\2\2\u00ed\34\3\2\2\2\u00ee\u00ef")
        buf.write("\7h\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7t\2\2\u00f1\36")
        buf.write("\3\2\2\2\u00f2\u00f3\7h\2\2\u00f3\u00f4\7w\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7p\2\2\u00fa \3")
        buf.write("\2\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7h\2\2\u00fd\"\3")
        buf.write("\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7g\2\2\u0102\u0103\7i\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104\u0105\7t\2\2\u0105$\3\2\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\u0108\7g\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7t\2\2\u010b\u010c\7p\2\2\u010c&\3")
        buf.write("\2\2\2\u010d\u010e\7u\2\2\u010e\u010f\7v\2\2\u010f\u0110")
        buf.write("\7t\2\2\u0110\u0111\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7i\2\2\u0113(\3\2\2\2\u0114\u0115\7v\2\2\u0115\u0116")
        buf.write("\7t\2\2\u0116\u0117\7w\2\2\u0117\u0118\7g\2\2\u0118*\3")
        buf.write("\2\2\2\u0119\u011a\7x\2\2\u011a\u011b\7q\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7f\2\2\u011d,\3\2\2\2\u011e\u011f")
        buf.write("\7y\2\2\u011f\u0120\7j\2\2\u0120\u0121\7k\2\2\u0121\u0122")
        buf.write("\7n\2\2\u0122\u0123\7g\2\2\u0123.\3\2\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7w\2\2\u0126\u0127\7v\2\2\u0127\60")
        buf.write("\3\2\2\2\u0128\u0129\7e\2\2\u0129\u012a\7q\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7v\2\2\u012c\u012d\7k\2\2\u012d\u012e")
        buf.write("\7p\2\2\u012e\u012f\7w\2\2\u012f\u0130\7g\2\2\u0130\62")
        buf.write("\3\2\2\2\u0131\u0132\7q\2\2\u0132\u0133\7h\2\2\u0133\64")
        buf.write("\3\2\2\2\u0134\u0135\7k\2\2\u0135\u0136\7p\2\2\u0136\u0137")
        buf.write("\7j\2\2\u0137\u0138\7g\2\2\u0138\u0139\7t\2\2\u0139\u013a")
        buf.write("\7k\2\2\u013a\u013b\7v\2\2\u013b\66\3\2\2\2\u013c\u013d")
        buf.write("\7-\2\2\u013d8\3\2\2\2\u013e\u013f\7/\2\2\u013f:\3\2\2")
        buf.write("\2\u0140\u0141\7,\2\2\u0141<\3\2\2\2\u0142\u0143\7\61")
        buf.write("\2\2\u0143>\3\2\2\2\u0144\u0145\7\'\2\2\u0145@\3\2\2\2")
        buf.write("\u0146\u0147\7#\2\2\u0147B\3\2\2\2\u0148\u0149\7(\2\2")
        buf.write("\u0149\u014a\7(\2\2\u014aD\3\2\2\2\u014b\u014c\7~\2\2")
        buf.write("\u014c\u014d\7~\2\2\u014dF\3\2\2\2\u014e\u014f\7?\2\2")
        buf.write("\u014f\u0150\7?\2\2\u0150H\3\2\2\2\u0151\u0152\7#\2\2")
        buf.write("\u0152\u0153\7?\2\2\u0153J\3\2\2\2\u0154\u0155\7>\2\2")
        buf.write("\u0155L\3\2\2\2\u0156\u0157\7>\2\2\u0157\u0158\7?\2\2")
        buf.write("\u0158N\3\2\2\2\u0159\u015a\7@\2\2\u015aP\3\2\2\2\u015b")
        buf.write("\u015c\7@\2\2\u015c\u015d\7?\2\2\u015dR\3\2\2\2\u015e")
        buf.write("\u015f\7<\2\2\u015f\u0160\7<\2\2\u0160T\3\2\2\2\u0161")
        buf.write("\u0162\7*\2\2\u0162V\3\2\2\2\u0163\u0164\7+\2\2\u0164")
        buf.write("X\3\2\2\2\u0165\u0166\7]\2\2\u0166Z\3\2\2\2\u0167\u0168")
        buf.write("\7_\2\2\u0168\\\3\2\2\2\u0169\u016a\7}\2\2\u016a^\3\2")
        buf.write("\2\2\u016b\u016c\7\177\2\2\u016c`\3\2\2\2\u016d\u016e")
        buf.write("\7\60\2\2\u016eb\3\2\2\2\u016f\u0170\7.\2\2\u0170d\3\2")
        buf.write("\2\2\u0171\u0172\7=\2\2\u0172f\3\2\2\2\u0173\u0174\7<")
        buf.write("\2\2\u0174h\3\2\2\2\u0175\u0176\7?\2\2\u0176j\3\2\2\2")
        buf.write("\u0177\u017b\t\4\2\2\u0178\u017a\t\5\2\2\u0179\u0178\3")
        buf.write("\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c")
        buf.write("\3\2\2\2\u017cl\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u017f")
        buf.write("\t\6\2\2\u017fn\3\2\2\2\u0180\u0181\t\7\2\2\u0181p\3\2")
        buf.write("\2\2\u0182\u0183\t\4\2\2\u0183r\3\2\2\2\u0184\u0185\t")
        buf.write("\b\2\2\u0185t\3\2\2\2\u0186\u0192\5o8\2\u0187\u0189\7")
        buf.write("a\2\2\u0188\u0187\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018d")
        buf.write("\3\2\2\2\u018a\u018c\5m\67\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0188\3")
        buf.write("\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193")
        buf.write("\3\2\2\2\u0193v\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0199")
        buf.write("\7\60\2\2\u0196\u0198\5m\67\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019ax\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019e\7g\2\2")
        buf.write("\u019d\u019f\5s:\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2")
        buf.write("\2\2\u019f\u01a1\3\2\2\2\u01a0\u01a2\5m\67\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01af\3\2\2\2\u01a5\u01a7\7G\2\2")
        buf.write("\u01a6\u01a8\5s:\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3\2")
        buf.write("\2\2\u01a8\u01aa\3\2\2\2\u01a9\u01ab\5m\67\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u019c\3\2\2\2")
        buf.write("\u01ae\u01a5\3\2\2\2\u01afz\3\2\2\2\u01b0\u01b1\7^\2\2")
        buf.write("\u01b1\u01b2\t\2\2\2\u01b2|\3\2\2\2\u01b3\u01b5\t\t\2")
        buf.write("\2\u01b4\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\b?\6\2\u01b9~\3\2\2\2\u01ba\u01bb\7\61\2\2\u01bb")
        buf.write("\u01bc\7,\2\2\u01bc\u01c0\3\2\2\2\u01bd\u01bf\13\2\2\2")
        buf.write("\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01c1\3")
        buf.write("\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c3\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c3\u01c4\7,\2\2\u01c4\u01c5\7\61\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c7\b@\6\2\u01c7\u0080\3\2\2\2")
        buf.write("\u01c8\u01c9\7\61\2\2\u01c9\u01ca\7\61\2\2\u01ca\u01ce")
        buf.write("\3\2\2\2\u01cb\u01cd\n\3\2\2\u01cc\u01cb\3\2\2\2\u01cd")
        buf.write("\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d2\b")
        buf.write("A\6\2\u01d2\u0082\3\2\2\2\u01d3\u01d9\7$\2\2\u01d4\u01d5")
        buf.write("\7^\2\2\u01d5\u01d8\t\2\2\2\u01d6\u01d8\n\3\2\2\u01d7")
        buf.write("\u01d4\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01df\3")
        buf.write("\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01dd\7^\2\2\u01dd\u01e0")
        buf.write("\n\2\2\2\u01de\u01e0\7\f\2\2\u01df\u01dc\3\2\2\2\u01df")
        buf.write("\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\bB\7\2")
        buf.write("\u01e2\u0084\3\2\2\2\u01e3\u01e9\7$\2\2\u01e4\u01e5\7")
        buf.write("^\2\2\u01e5\u01e8\t\2\2\2\u01e6\u01e8\n\n\2\2\u01e7\u01e4")
        buf.write("\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01ec\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01ec\u01ed\bC\b\2\u01ed\u0086\3")
        buf.write("\2\2\2\u01ee\u01ef\13\2\2\2\u01ef\u01f0\bD\t\2\u01f0\u0088")
        buf.write("\3\2\2\2\37\2\u0091\u0096\u009a\u009f\u00a3\u00a7\u00af")
        buf.write("\u00b3\u00b9\u00bb\u017b\u0188\u018d\u0192\u0199\u019e")
        buf.write("\u01a3\u01a7\u01ac\u01ae\u01b6\u01c0\u01ce\u01d7\u01d9")
        buf.write("\u01df\u01e7\u01e9\n\3\3\2\3\5\3\3\5\4\3\6\5\b\2\2\3B")
        buf.write("\6\3C\7\3D\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IntegerLiteral = 2
    BooleanLiteral = 3
    FloatLiteral = 4
    StringLiteral = 5
    Auto = 6
    Array = 7
    Break = 8
    Boolean = 9
    Do = 10
    Else = 11
    False_ = 12
    Float = 13
    For = 14
    Function = 15
    If = 16
    Integer = 17
    Return = 18
    String = 19
    True_ = 20
    Void = 21
    While = 22
    Out = 23
    Continue = 24
    Of = 25
    Inherit = 26
    Plus = 27
    Minus = 28
    Star = 29
    Div = 30
    Mod = 31
    Not = 32
    AndAnd = 33
    OrOr = 34
    Equal = 35
    NotEqual = 36
    Less = 37
    LessEqual = 38
    Greater = 39
    GreaterEqual = 40
    Doublecolon = 41
    LeftParen = 42
    RightParen = 43
    LeftBracket = 44
    RightBracket = 45
    LeftBrace = 46
    RightBrace = 47
    Dot = 48
    Comma = 49
    Semicolon = 50
    Colon = 51
    Assign = 52
    Identifier = 53
    WhiteSpace = 54
    BlockComment = 55
    LineComment = 56
    ILLEGAL_ESCAPE = 57
    UNCLOSED_STRING = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'auto'", "'array'", "'break'", "'boolean'", "'do'", 
            "'else'", "'false'", "'float'", "'for'", "'function'", "'if'", 
            "'integer'", "'return'", "'string'", "'true'", "'void'", "'while'", 
            "'out'", "'continue'", "'of'", "'inherit'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'.'", "','", "';'", "':'", "'='" ]

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
            "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IntegerLiteral", "BooleanLiteral", "FloatLiteral", 
                  "StringLiteral", "Auto", "Array", "Break", "Boolean", 
                  "Do", "Else", "False_", "Float", "For", "Function", "If", 
                  "Integer", "Return", "String", "True_", "Void", "While", 
                  "Out", "Continue", "Of", "Inherit", "Plus", "Minus", "Star", 
                  "Div", "Mod", "Not", "AndAnd", "OrOr", "Equal", "NotEqual", 
                  "Less", "LessEqual", "Greater", "GreaterEqual", "Doublecolon", 
                  "LeftParen", "RightParen", "LeftBracket", "RightBracket", 
                  "LeftBrace", "RightBrace", "Dot", "Comma", "Semicolon", 
                  "Colon", "Assign", "Identifier", "DIGIT", "NONZERODIGIT", 
                  "NONDIGIT", "SIGN", "INTEGERPART", "DECIMALPART", "EXPONENTPART", 
                  "STRING_ESC_SEQUENCE", "WhiteSpace", "BlockComment", "LineComment", 
                  "ILLEGAL_ESCAPE", "UNCLOSED_STRING", "ERROR_CHAR" ]

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
            actions[1] = self.IntegerLiteral_action 
            actions[3] = self.FloatLiteral_action 
            actions[4] = self.StringLiteral_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.UNCLOSED_STRING_action 
            actions[66] = self.ERROR_CHAR_action 
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
     

    def StringLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:]; raise IllegalEscape(self.text)
     

    def UNCLOSED_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text[1:]; raise UncloseString(self.text)
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise ErrorToken(self.text)
     


