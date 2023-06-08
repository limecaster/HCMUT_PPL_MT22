/** Student ID: 2110813
  * Name: Do Van Bang
*/
/**
  *	Filename: MT22.g4	
*/
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declaration+ EOF;

declaration: variableDeclaration | functionDeclaration;

functionDeclaration: functionPrototype blockStatement;

functionPrototype:  Identifier Colon Function mt22Type LeftParen parameterList RightParen
                  | Identifier Colon Function mt22Type LeftParen parameterList RightParen Inherit Identifier;

parameterList: parameterListPrime | ;

parameterListPrime:  parameterDeclarion Comma parameterListPrime
              | parameterDeclarion;

parameterDeclarion: Identifier Colon mt22Type
                  | Out Identifier Colon mt22Type
                  | Inherit Identifier Colon mt22Type
                  | Inherit Out Identifier Colon mt22Type;

variableDeclaration:  varDeclShortForm Semicolon
                    | varDeclFullForm Semicolon
                    | arrayDeclaration Semicolon;

varDeclShortForm:  identifierList Colon mt22Type;

varDeclFullForm:  Identifier Comma varDeclFullForm Comma expression
                | Identifier Colon mt22Type Assign expression;

arrayDeclaration: arrayDeclShortForm | arrayDeclFullForm;

arrayDeclShortForm: identifierList Colon Array dimensionArray Of atomicType;

arrayDeclFullForm:    Identifier Comma arrayDeclFullForm Comma expression 
                   |  Identifier Colon Array dimensionArray Of atomicType Assign expression;

expression:   LeftParen expression RightParen
            | indexedExpression
            | <assoc = right> Minus expression
            | <assoc = right> Not expression
            | <assoc = left> expression multiplyOperator expression
            | <assoc = left> expression addingOperator expression
            | <assoc = left> expression booleanOperator expression
            | expression relationalOperator expression
            | expression stringOperator expression
            | operand
            ;


expressionList: expression Comma expressionList
              | expression;

indexedExpression:  Identifier indexedOperator;

functionCall: Identifier LeftParen expressionList RightParen
            | Identifier LeftParen RightParen; 

operand:  literal
        | Identifier
        | functionCall
        ;

indexedOperator:  LeftBracket expressionList RightBracket;

booleanOperator:  AndAnd | OrOr;

relationalOperator: Equal | NotEqual | Less | Greater | LessEqual | GreaterEqual;

multiplyOperator: Star | Div | Mod;

addingOperator: Plus | Minus; 

stringOperator: Doublecolon;

arrayLiteral: LeftBrace expressionList RightBrace;

mt22Type: atomicType | Void | Auto | Array dimensionArray Of atomicType;

atomicType: String | Integer | Float | Boolean;

dimensionArray: LeftBracket dimensionsArrayPrime RightBracket;

dimensionsArrayPrime: IntegerLiteral Comma dimensionsArrayPrime
                    | IntegerLiteral;


literal:  StringLiteral
        | IntegerLiteral
        | FloatLiteral
        | BooleanLiteral
        | arrayLiteral
        ;

statement:    assignStatement
            | forStatement
            | whileStatement
            | do_whileStatement
            | breakStatement
            | continueStatement
            | returnStatement
            | callStatement
            | blockStatement
            | conditionStatement
            ;

assignStatement:  scalarVariable Assign expression Semicolon;

conditionStatement: If LeftParen expression RightParen statement
                  | If LeftParen expression RightParen statement Else statement;

forStatement: For LeftParen scalarVariable Assign expression 
              Comma expression Comma expression RightParen
              statement;

scalarVariable: Identifier | indexedExpression;

whileStatement: While LeftParen expression RightParen statement;

do_whileStatement:  Do blockStatement While LeftParen expression RightParen Semicolon;

continueStatement:  Continue Semicolon;

returnStatement:  Return Semicolon
                | Return expression Semicolon;

breakStatement: Break Semicolon;

blockStatement: LeftBrace blockStatementPrime RightBrace
              | LeftBrace RightBrace;

blockStatementPrime:  statement blockStatementPrime
                    | variableDeclaration blockStatementPrime
                    | statement
                    | variableDeclaration;

callStatement:  functionCall Semicolon;

identifierList: Identifier Comma identifierList
              | Identifier;
          
        
IntegerLiteral: '0' | NONZERODIGIT ('_'? DIGIT+)*  {self.text = self.text.replace('_','')};

BooleanLiteral: True_ | False_;

FloatLiteral:   INTEGERPART DECIMALPART? EXPONENTPART   {self.text = self.text.replace('_','')}
              | INTEGERPART DECIMALPART EXPONENTPART?   {self.text = self.text.replace('_','')}
              | INTEGERPART? DECIMALPART EXPONENTPART   {self.text = self.text.replace('_','')};

StringLiteral: '"' (ESC_SEQUENCE | ~[\r\n\\"] )*? '"' 
  {
    self.text = self.text[1:-1];
    self.text = self.text.replace('\\"', '\"')
  };

// Keywords
Auto:     'auto';
Array:    'array';
Break:    'break';
Boolean:  'boolean';
Do:       'do';
Else:     'else';
False_:   'false';
Float:    'float';
For:      'for';
Function: 'function';
If:       'if';
Integer:  'integer';
Return:   'return';
String:   'string';
True_:    'true';
Void:     'void';
While:    'while';
Out:      'out';
Continue: 'continue';
Of:       'of';
Inherit:  'inherit';


// Operators
Plus:           '+';
Minus:          '-';
Star:           '*';
Div:            '/';
Mod:            '%';
Not:            '!'; 
AndAnd:         '&&';
OrOr:           '||';
Equal:          '==';
NotEqual:       '!=';
Less:           '<';
LessEqual:      '<=';
Greater:        '>';
GreaterEqual:   '>=';
Doublecolon:    '::';

// Seperators
LeftParen:      '(';
RightParen:     ')';
LeftBracket:    '[';
RightBracket:   ']';
LeftBrace:      '{';
RightBrace:     '}';
Dot:            '.';
Comma:          ',';
Semicolon:      ';';
Colon:          ':';
Assign:         '=';


Identifier: [a-zA-Z_][a-zA-Z_0-9]*;


fragment  DIGIT:  [0-9];

fragment  NONZERODIGIT: [1-9];

fragment  NONDIGIT: [a-zA-Z_];

fragment  SIGN: [+-];

fragment  INTEGERPART: DIGIT ('_'? DIGIT+)*;

fragment  DECIMALPART: '.' DIGIT*;

fragment  EXPONENTPART:  'e'  SIGN?  DIGIT+
                        |'E'  SIGN?  DIGIT+;

fragment  ESC_SEQUENCE: '\\' [bfrnt'"\\];

WhiteSpace : [ \b\f\r\n\t]+  -> skip ; 

BlockComment: '/*' .*? '*/' -> skip;

//UNCLOSE_COMMENT: '/*' .*? {raise UnterminatedComment(self.text)};

LineComment: '//' ~ [\r\n]* -> skip;

ILLEGAL_ESCAPE: '"' (ESC_SEQUENCE | ~[\r\n\\"])*? ('\\' ~[btfr"'\\])  {raise IllegalEscape(self.text[1:])};

UNCLOSED_STRING:'"' (ESC_SEQUENCE | ~[\r\n\\"] )* ('\n' | EOF)?  {raise UncloseString(self.text[1:])}; 

ERROR_CHAR: . {raise ErrorToken(self.text)};

ERROR_INTLIT: NONZERODIGIT DIGIT* ('__'+'_'* DIGIT+)* {raise ErrorToken(self.text)};