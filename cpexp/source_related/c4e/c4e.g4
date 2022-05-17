grammar c4e;


block
  : statemenet*     # StatementsBlock
  ;

statemenet
  : IDN ASSIGN expression SEM                       # AssignStatement
  | TYPE_ IDN SEM                                   # DeclareStatement
  | IF LP condition RP statemenet                   # IfStatement
  | IF LP condition RP statemenet ELSE statemenet   # IfElseStatement
  | WHILE LP condition RP statemenet                # WhileStatement
  | SEM                                             # EmptyStatement
  | LB block RB                                     # BracketedStatement
  ;

condition
  : expression GT expression      # GreaterCondition
  | expression LT expression      # LessCondition
  | expression EQ expression      # EqualCondition
  ;

expression
  : expression ADD term     # AddExpression
  | expression SUB term     # SubExpression
  | term                    # TermExpression
  ;

term
  : factor              # FactorTerm
  | term MUL factor     # MultipleTerm
  | term DIV factor     # DivitionTerm
  ;

factor
  : LP expression RP    # BracketedFactor
  | IDN                 # IdentifierFactor
  | INT8                # Int8Factor
  | INT10               # Int10Factor
  | INT16               # Int16Factor
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

TYPE_: 'int' | 'float';
IDN: [a-zA-Z]([a-zA-Z]|[0-9])*(('_'|'.')([a-zA-Z]|[0-9])+)?;
INT16: ('0x'|'0X')[0-9a-f]+;
REAL16: INT16'.'[0-9a-f]+;
INT8: '0'[1-7][0-7]*;
REAL8: INT8'.'[0-7]+;
INT10: '0'|[1-9][0-9]*;
REAL10: INT10'.'[0-9]+;

WS : [ \r\t\n]+ -> skip ;
