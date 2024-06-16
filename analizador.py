#Inicio aporte Carlos Cabanilla
import ply.lex as lex
#Aporte de Kevin Ibarra
reserved = {
    'def' : 'DEF',
    'end':'END',
    'true':'TRUE',
    'false':'FALSE'
}
#

# List of token names.   This is always required
tokens = (
   'INTEGER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'FLOAT',
   'IP',
   #Kevin Ibarra
   'LIST',
   'BOOLEAN',
   'LPAREN',
   'RPAREN',
   'POINT',
   'VARIABLE',
   'STRING'
   #
) + tuple(reserved.values()) #agregar la coma y dos puntos 

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
#Kevin Ibarra
t_POINT    = r','
#

def t_VARIABLE(t):
    r'[_a-zA-Z]\w*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t

#Expresión regular para reconocer números flotantes
def t_FLOAT(t):
    r'-?[0-9]*\.[0-9]*'
    t.value = float(t.value)
    return t

#Expresión regular para reconocer números enteros y flotantes
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

#Expresión regular para reconocer direcciones IP
def t_IP(t):
    r'(?:\d{1,3}\.){3}\d{1,3}'
    return t

#Kevin Ibarra
def t_LIST(t):
    r'\[\s*([a-zA-Z_][a-zA-Z0-9_]*|\d+)\s*(,\s*([a-zA-Z_][a-zA-Z0-9_]*|\d+)\s*)*\]'
    t.type = reserved.get(t.value, 'LIST')
    return t

def t_STRING(t):
  r'[\"\'](\\.|[^\"\'])*[\"\']' #Acepta comillas simples o dobles
  t.value = t.value[1:-1]  # Eliminar comillas
  return t
#

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#Informacion a verificar
data = "La direccion IP del pc involucrado es 194.111.10.3"
#Kevin Ibarra
data_Kevin = '[manzana, naranja, platano] [1,2,3] "Hola mundo"'
#
lexer.input(data_Kevin)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)