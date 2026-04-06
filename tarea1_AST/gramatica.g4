grammar gramatica;

prog: expr EOF ;

expr: expr ('+'|'-') term   # AddSub
    | term                  # TermAlt
    ;

term: term ('*'|'/') factor # MulDiv
    | factor                # FactorAlt
    ;

factor: NUMBER              # Number
      | IDENT               # Identifier
      | '(' expr ')'        # Parens
      ;

NUMBER : [0-9]+ ;
IDENT  : [a-zA-Z_][a-zA-Z0-9_]* ;
WS     : [ \t\r\n]+ -> skip ;
