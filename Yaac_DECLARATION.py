import ply.yacc as yacc
from LEX_DECLARATION import tokens

def p_program(p):
    '''
    program : statement
           | program statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement_var_declare(p):
    'statement : NAME NAME ASSIGN expression SEMICOLON'
    p[0] = ("var_declare", p[2], p[4])

def p_expression(p):
    '''expression : NUMBER
                  | STRING
                  | BOOLEAN
                  | NULL
                  | UNDEFINED'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} with value '{p.value}'")
    else:
        print("Syntax error at EOF")

# Create the parser
parser = yacc.yacc()

# Sample input code
input_code = """var x = 42;
                var y = 90;
var hello = 90;
"""

# Parse the input code
result = parser.parse(input_code)

print(result)
