grammar ImageManipulation;

// Define lexer rules
ID : [a-zA-Z]+;
INT_LITERAL : [0-9]+;
ALPHA : [a-zA-Z];
DIGIT : [0-9];
STRING_LITERAL : '"' (~["])* '"';
WS : [ \t\r\n]+ -> skip; // Skip whitespace

// Define parser rules
program : (declaration | action | export | COMMENT)*;

declaration : open_file | open_folder;

open_file : ID '=' 'open' '(' file_path ')' ';';

open_folder : ID '[' STRING_LITERAL ']' '=' 'open' '(' folder_path ')' ';';

action : ID action_type ';';

action_type : '=' 'open' '(' folder_path ')'
            | 'crop' '(' INT_LITERAL ',' INT_LITERAL ',' INT_LITERAL ',' INT_LITERAL ')'
            | 'rotate' '(' INT_LITERAL ')'
            | 'resize' '(' INT_LITERAL (',' INT_LITERAL)? ')'
            | 'brightness' '(' INT_LITERAL ')'
            | 'contrast' '(' INT_LITERAL ')'
            | 'saturation' '(' INT_LITERAL ')';

export : 'export' ID export_action ';';

export_action : 'save' image_type STRING_LITERAL;

file_path : STRING_LITERAL;

folder_path : ALPHA STRING_LITERAL;

image_type : 'png' | 'jpg';

COMMENT : '//' ~[\r\n]* -> skip; // Single-line comment rule
COMMENT2 : '/*' .*? '*/' -> skip; // Multi-line comment rule

// Define fragment rules if needed
fragment ALPHA_NUM : ALPHA | DIGIT;