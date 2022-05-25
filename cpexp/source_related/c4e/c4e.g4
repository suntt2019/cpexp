grammar c4e;

program
  : (declare_statement|function_declaration|asm_statement|function_definition)*
  ;

function_declaration
  : function_prototype SEM      # FunctionDeclaration
  ;

function_definition
  :  function_prototype function_body       # FunctionDefinition
  ;

function_prototype
  : (VOID|TYPE_) IDN LP ((TYPE_ IDN COMMA)* (TYPE_ IDN|DOTS))? RP     # FunctionPrototype
  ;

function_body
  : LB block RB     # FunctionBody
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
  | asm_statement
  ;

declare_statement
  : TYPE_ IDN SEM
  | TYPE_ IDN ASSIGN expression SEM
  ;

value_statement
  : IDN ASSIGN expression SEM       # AssignStatement
  | expression SEM                  # ExpressionStatement
  | SEM                             # EmptyStatement
  ;

control_flow_statement
  : IF LP condition RP non_declare_statement                    # IfStatement
  | IF LP condition RP statemenet ELSE non_declare_statement    # IfElseStatement
  | WHILE LP condition RP non_declare_statement                 # WhileStatement
  ;

return_statement
  : RET expression SEM      # ReturnValueStatement
  | RET SEM                 # ReturnVoidStatement
  ;

combined_statement
  : LB block RB     # BracketedStatement
  ;

asm_statement
  : ASM LP STR RP SEM   # AsmStatement
  ;

condition
  : expression GT expression      # GreaterCondition
  | expression LT expression      # LessCondition
  | expression EQ expression      # EqualCondition
  ;

expression
  : expression ADD term                             # AddExpression
  | expression NEG term                             # SubExpression
  | term                                            # TermExpression
  | IDN LP ((expression COMMA)* expression)? RP     # CallExpression
  ;

term
  : unary              # UnaryTerm
  | term MUL unary     # MultipleTerm
  | term DIV unary     # DivitionTerm
  ;

unary
  : NEG factor          # NegUnary
  | factor              # FactorUnary
  ;

factor
  : LP expression RP    # BracketedFactor
  | IDN                 # IdentifierFactor
  | INT8                # Int8Factor
  | INT10               # Int10Factor
  | INT16               # Int16Factor
  | REAL8               # Real8Factor
  | REAL10              # Real10Factor
  | REAL16              # Real16Factor
  | STR                 # StringFactor
  ;


IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
DO: 'do';
RET: 'return';
ASM: 'asm';


ADD: '+';
NEG: '-';
MUL: '*';
DIV: '/';
LT:  '<';
GT:  '>';
EQ:  '==';
LP:  '(';  // Parentheses
RP:  ')';
ASSIGN: '=';
COMMA: ',';
SEM: ';';
LB: '{';  // Braces
RB: '}';

DOTS: '...';
VOID: 'void';

TYPE_: 'string' | 'long' | 'float';
IDN: [a-zA-Z]([a-zA-Z]|[0-9])*(('_'|'.')([a-zA-Z]|[0-9])+)?;
INT16: ('0x'|'0X')[0-9a-f]+;
REAL16: INT16'.'[0-9a-f]+;
INT8: '0'[1-7][0-7]*;
REAL8: INT8'.'[0-7]+;
INT10: '0'|[1-9][0-9]*;
REAL10: INT10'.'[0-9]+;
STR: '"'.*?'"';

WS : [ \r\t\n]+ -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
