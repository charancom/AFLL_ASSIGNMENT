from ply import lex

# List of token names
tokens = (
    'ID',       # Identifier
    'LPAREN',   # (
    'RPAREN',   # )
    'LBRACE',   # {
    'RBRACE',   # }
    'FUNCTION', # function keyword
    'COMMA',    # ,
)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','

# Recognize 'function' as a keyword
def t_FUNCTION(t):
    r'function'
    return t

# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == '__main__':
    # Test the lexer
    lexer.input("function hello(param1, param2) {")
    for token in lexer:
        print(token)
