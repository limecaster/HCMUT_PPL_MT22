grammar MiniPHP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: variableDeclaration+ EOF;

variableDeclaration: VARNAME EQ expression SEMI;

array:  indexedArray | associativeArray;

indexedArray:   ARRAY LP indexedArrayPrime RP
            |   ARRAY LP RP;

indexedArrayPrime:  expression COMMA indexedArrayPrime
                |   expression;

associativeArray:   ARRAY LP associativeArrayPrime RP
                |   ARRAY LP RP;

associativeArrayPrime:  associativePair COMMA associativeArrayPrime
                    |   associativePair;

associativePair: PAIRNAME ARROW expression;

expression: operand DSTAR expression
        |   expression DOT operand
        |   expression (MUL | DIV | MOD) operand
        |   expression (ADD | SUB) operand
        |   expression DQUES operand
        |   LP expression RP
        |   operand;

operand: VARNAME | INTLIT | FLOATLIT | STRINGLIT | array;

ARRAY: 'array';
EQ: '=';
SEMI: ';';
LP: '(';
RP: ')';
COMMA: ',';
ARROW: '=>';
DSTAR: '**';
DOT: '.';
MUL: '*';
DIV: '/';
MOD: '%';
ADD: '+';
SUB: '-';
DQUES: '?';



PAIRNAME: STRINGLIT;
VARNAME: STRINGLIT;

INTLIT: [0-9]+;

FLOATLIT: [0-9]+ '.' [0-9]+;

STRINGLIT: [a-zA-Z0-9_]+;


WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};