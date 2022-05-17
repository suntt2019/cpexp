grammar c4e;

program
  : declare_block function*
  ;

declare_block
  : declare_statement*  # DeclareBlock
  ;

function
  : TYPE_ IDN LP RP LB block RB
  ;

block
  : statemenet*         # StatementsBlock
  ;

statemenet
  : declare_statement
  | non_declare_statement
  ;

non_declare_statement
  : value_statement
  | control_flow_statement
  | return_statement
  | combined_statement
  ;

declare_statement
  : TYPE_ IDN SEM       # DeclareStatement
  ;

value_statement
  : IDN ASSIGN expression SEM       # AssignStatement
  | expression SEM                  # ExpressionStatement
  | SEM                             # EmptyStatement
  ;

control_flow_statement
  : declare_statement                               # ToDeclareStatement
  | IF LP condition RP statemenet                   # IfStatement
  | IF LP condition RP statemenet ELSE statemenet   # IfElseStatement
  | WHILE LP condition RP statemenet                # WhileStatement
  ;

return_statement
  : RET expression SEM      # ReturnStatement
  ;

combined_statement
  : LB block RB     # BracketedStatement
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
  | IDN LP RP               # CallExpression
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
RET: 'return';


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
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
