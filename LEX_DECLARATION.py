import ply.lex as lex

# List of token names
tokens = (
    'NAME',
    'ASSIGN',
    'NUMBER',
    'STRING',
    'BOOLEAN',
    'UNDEFINED',
    'NULL',
    'SEMICOLON',
)

# Regular expressions for token rules
t_ASSIGN = r'='
t_SEMICOLON = r';'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'NAME'  # Set the token type to 'NAME'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"|\'[^\']*\''
    t.value = t.value[1:-1]
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = (t.value == 'true')
    return t

def t_UNDEFINED(t):
    r'undefined'
    t.value = None
    return t

def t_NULL(t):
    r'null'
    t.value = None
    return t

# Newline handling
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore whitespace and tab characters
t_ignore = ' \t'

# Error handling function
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()


