import ply.yacc as yacc
from ARROW_DECLARATIONLEX import tokens


def p_array_declaration(p):
    'array_declaration : LBRACKET array_items RBRACKET'
    p[0] = p[2]  # The result is the list of array items

def p_array_items(p):
    'array_items : array_item'
    p[0] = [p[1]]  # Initialize a list with the first item

def p_array_items_multiple(p):
    'array_items : array_item COMMA array_items'
    p[0] = [p[1]] + p[3]  # Combine the current item with the rest

def p_array_item(p):
    '''array_item : NUMBER
                  | STRING
                  | BOOL
                  | NULL'''
    p[0] = p[1]  # The result is the value of the array item


def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}, unexpected token: {p.value}")

parser = yacc.yacc()

input_text = '[1, "two", true, null]'
result = parser.parse(input_text)
print(result)
