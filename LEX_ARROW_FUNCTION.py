import ply.lex as lex

# List of token names
tokens = (
    'LPAREN',
    'RPAREN',
    'IDENTIFIER',
    'ARROW',
    'COMMA',
    'NUMBER',  # Add NUMBER token
    'STRING',  # Add STRING token
)

# Regular expressions for token rules
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ARROW = r'=>'

# Define a rule for identifiers (parameter names)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

# Define a rule for the comma
def t_COMMA(t):
    r','
    return t

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert the value to an integer
    return t

# Define a rule for strings
def t_STRING(t):
    r'"[^"]*"|\'[^\']*\''
    t.value = t.value[1:-1]  # Remove quotes from the value
    return t

# Ignore whitespace and tab characters
t_ignore = ' \t'

# Error handling function
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Create the lexer
lexer = lex.lex()

# Sample input code
input_code = """(param1, param2) => "Hello, world" => 42"""

# Tokenize the input code
lexer.input(input_code)

# Print tokens
for tok in lexer:
    print(tok)
