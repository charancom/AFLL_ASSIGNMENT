import ply.yacc as yacc
from OBJECTS_LEX import tokens

# Define a simple JSON object grammar
def p_object(p):
    '''object : LBRACE members RBRACE'''
    p[0] = dict(p[2])

def p_members(p):
    '''members : pair
               | pair COMMA members'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[3].insert(0, p[1])
        p[0] = p[3]

def p_pair(p):
    'pair : STRING COLON value'
    p[0] = (p[1][1:-1], p[3])

def p_array(p):
    '''array : LBRACE elements RBRACE
             | LBRACE RBRACE'''
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]

def p_elements(p):
    '''elements : value
                | value COMMA elements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[3].insert(0, p[1])
        p[0] = p[3]

def p_value(p):
    '''value : STRING
             | NUMBER
             | BOOL
             | NULL
             | object
             | array'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error in input at position {p.lexpos}")

parser = yacc.yacc()
input_text = '{"name": "John", "age": 30, "isStudent": true, "address": {"city": "New York", "zipcode": 10001}}'

parsed_object = parser.parse(input_text)
print(parsed_object)