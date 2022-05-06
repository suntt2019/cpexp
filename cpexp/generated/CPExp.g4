grammar CPExp;

// Simple grammar, just for smoke test
r: TOKEN+;
TOKEN: IDN | INT16 | REAL16 | INT8 | REAL8 | INT10 | REAL10 | ADD | SUB | MUL | DIV | LT | GT | EQ | LB | RB | SEM | IF | THEN | ELSE | WHILE | DO;


IDN: [a-zA-Z]([a-zA-Z]|[0-9])*(('_'|'.')([a-zA-Z]|[0-9])+)?;
INT16: ('0x'|'0X')[0-9a-f]+;
REAL16: INT16'.'[0-9a-f]+;
INT8: '0'[1-7][0-7]*;
REAL8: INT8'.'[0-7]+;
INT10: '0'|[1-9][0-9]*;
REAL10: INT10'.'[0-9]+;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LT:  '<';
GT:  '>';
EQ:  '=';
LB:  '(';
RB:  ')';
SEM: ';';

IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
DO: 'do';

WS : [ \r\t\n]+ -> skip ;
