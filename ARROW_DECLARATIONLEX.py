import ply.lex as lex

tokens = (
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'NUMBER',
    'STRING',
    'BOOL',
    'NULL',
)

t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_NUMBER = r'-?\d+(\.\d+)?'
t_STRING = r'\"([^\\"]|\\.)*\"'
t_BOOL = r'true|false'
t_NULL = r'null'

t_ignore = ' \t\r\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

input_text = '[1, "two", true, null]'
lexer.input(input_text)

for token in lexer:
    print(token)

