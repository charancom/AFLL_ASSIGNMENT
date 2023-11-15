import ply.yacc as yacc
from LEX_ARROW_FUNCTION import tokens

def p_arrow_function(p):
    '''arrow_function : LPAREN param_list RPAREN ARROW expression'''
    p[0] = ('arrow_function', p[2], p[5])

def p_param_list(p):
    '''param_list : IDENTIFIER
                 | IDENTIFIER COMMA param_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | STRING
                  | arrow_function'''
    p[0] = p[1]

# Error handling function
def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}, unexpected token: {p.value}")

# Create the parser
parser = yacc.yacc()

# Sample input code
input_code = """(param1, param2) => expression"""

# Parse the input code
result = parser.parse(input_code)
print(result)
