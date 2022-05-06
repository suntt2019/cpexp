grammar CPExp;

// Simple grammar, just for smoke test
//r: TOKEN+;
//TOKEN: IDN | INT16 | REAL16 | INT8 | REAL8 | INT10 | REAL10 | ADD | SUB | MUL | DIV | LT | GT | EQ | LB | RB | SEM | IF | THEN | ELSE | WHILE | DO;

options {
    language  = Python3;
}

p
  : {print('pstart'); print('yo')} l {print('pend')}
  | l p
  ;

l
  : s
  ;

s
  : IDN EQ e SEM
  | IF c THEN s
  | IF c THEN s ELSE s
  | WHILE c DO s
  | LB p RB
  ;

c
  : e GT e
  | e LT e
  | e EQ e
  ;

e
  : e ADD e
  | e SUB e
  | t
  ;

t
  : f
  | t MUL f
  | t DIV f
  ;

f
  : LP e RP
  | IDN
  | INT8
  | INT10
  | INT16
  ;

IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE:{print('while')} 'while';
DO: 'do';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LT:  '<';
GT:  '>';
EQ:  '=';
LP:  '(';  // Parentheses
RP:  ')';
SEM: ';';

LB: '{';  // Braces
RB: '}';

IDN: [a-zA-Z]([a-zA-Z]|[0-9])*(('_'|'.')([a-zA-Z]|[0-9])+)?;
INT16: ('0x'|'0X')[0-9a-f]+;
REAL16: INT16'.'[0-9a-f]+;
INT8: '0'[1-7][0-7]*;
REAL8: INT8'.'[0-7]+;
INT10: '0'|[1-9][0-9]*;
REAL10: INT10'.'[0-9]+;

WS : [ \r\t\n]+ -> skip ;
