import ply.lex as lex

# Define a list of token names
tokens = (
    'LBRACE',
    'RBRACE',
    'COLON',
    'STRING',
    'NUMBER',
    'COMMA',
    'BOOL',
    'NULL',
)

# Define regular expressions for tokens
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_STRING = r'"[^"]*"'
t_NUMBER = r'-?\d+(\.\d+)?'
t_COMMA = r','
t_BOOL = r'true|false'
t_NULL = r'null'

# Ignore whitespace characters
t_ignore = ' \t\r\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

input_text = '{"name": "John", "age": 30, "isStudent": true, "grades": [90, 85, 95], "address": {"city": "New York", "zipcode": 10001}}'
lexer.input(input_text)

for tok in lexer :
    print(tok) ;
