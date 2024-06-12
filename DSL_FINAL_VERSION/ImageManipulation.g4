grammar ImageManipulation;

prog: (command | funcDef | funcCall)+ ;

command: assignment
       | action
       | saveCommand ;

assignment: ID '=' ('open' '(' STRING ')' | 'openFolder' '(' STRING ')') ;
action: ID '.' actionType ;

actionType: 'flipX'
          | 'flipY'
          | resizeCommand
          | cropCommand
          | rotateCommand
          | 'saturation' '(' NUMBER ')'
          | 'brightness' '(' NUMBER ')'
          | 'contrast' '(' NUMBER ')'
          | 'polynomial' ;

resizeCommand: 'resize' '(' NUMBER ',' NUMBER ')' ;
cropCommand: 'crop' '(' NUMBER ',' NUMBER ',' NUMBER ',' NUMBER ')' ;
rotateCommand: 'rotate' '(' NUMBER ')' ;

saveCommand: ID '.' 'save' '(' STRING ')' ;

funcDef: 'def' ID '(' ID ')' '{' (action | saveCommand)+ '}' ;
funcCall: ID '(' STRING ')' ;

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER  : [0-9]+ ;
STRING  : '"' (~["\r\n])* '"' ; // Match any character except double quotes, line feeds, or carriage returns

// Comment handling
LINE_COMMENT  : '//' ~[\r\n]* -> skip; // Skips anything after '//' until the end of the line
BLOCK_COMMENT : '/*' .*? '*/' -> skip; // Skips block comments delimited by /* and */

WS      : [ \t\r\n]+ -> skip ;