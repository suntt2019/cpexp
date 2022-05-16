grammar c4e;


p           // Program
  : s       # SingleProgram
  | s p     # AppendedProgram
  ;

s                           // Statement
  : IDN ASSIGN e SEM        # AssignStatement
  | IF c THEN s             # IfStatement
  | IF c THEN s ELSE s      # IfElseStatement
  | WHILE c DO s            # WhileStatement
  | LB p RB                 # BracketedStatement
  ;

c               // Condition
  : e GT e      # GreaterCondition
  | e LT e      # LessCondition
  | e EQ e      # EqualCondition
  ;

e               // Expression
  : e ADD t     # AddExpression
  | e SUB t     # SubExpression
  | t           # TermExpression
  ;

t               // Term
  : f           # FactorTerm
  | t MUL f     # MultipleTerm
  | t DIV f     # DivitionTerm
  ;

f               // Factor
  : LP e RP     # BracketedFactor
  | IDN         # IdentifierFactor
  | INT8        # Int8Factor
  | INT10       # Int10Factor
  | INT16       # Int16Factor
  ;

IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
DO: 'do';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LT:  '<';
GT:  '>';
EQ:  '==';
LP:  '(';  // Parentheses
RP:  ')';
ASSIGN: '=';
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
