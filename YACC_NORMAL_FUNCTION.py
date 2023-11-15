from ply import yacc
from LEX_NORMAL_FUNCTION import lexer, tokens

# Grammar rules

# def p_function_declaration(p):
#     '''
#     function_declaration : FUNCTION ID LPAREN parameter_list RPAREN LBRACE RBRACE
#                         | FUNCTION ID LPAREN RPAREN LBRACE RBRACE
#     '''

def p_function_declaration(p):
    '''
    function_declaration : FUNCTION ID LPAREN parameter_list RPAREN LBRACE RBRACE
                        | FUNCTION ID LPAREN RPAREN LBRACE RBRACE
    '''
    p[0] = f'Parsed function declaration: {p[2]}'


def p_parameter_list(p):
    '''
    parameter_list : parameter
                  | parameter_list COMMA parameter
    '''

def p_parameter(p):
    '''
    parameter : ID
    '''

# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error at token '{p.value}'")

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':
    # Test the parser with a modified input
    input_text = "function myFunction(param1, param2) {}"
    result = parser.parse(input_text, lexer=lexer)
    print(result)


