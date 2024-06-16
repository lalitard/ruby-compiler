#Inicio aporte Carlos Cabanilla
import ply.lex as lex
import re
#Aporte de Kevin Ibarra
reserved = {
    'def' : 'DEF',
    'end':'END',
    'true':'TRUE',
    'false':'FALSE',
    #Empieza aporte Adrian Litardo
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE',
    'for':'FOR',
    'in':'IN',
    'print':'PRINT',
    'input':'INPUT',
    'return':'RETURN',
    'break':'BREAK',
    #Termina aporte Adrian Litardo

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
   'STRING',
    #Empieza aporte Adrian Litardo
    'COMMA',
    'COLON',
    'SEMICOLON',
    'EQUALS',
    'NOT_EQUALS',
    'EXPONENT',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL_THAN',
    'GREATER_EQUAL_THAN',
    'AND',
    'OR',
    'NOT',
    'HASH'
    #Termina aporte Adrian Litardo

) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
#Empieza aporte Adrian Litardo
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_EXPONENT = r'\^'
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_EQUAL_THAN = r'<='
t_GREATER_EQUAL_THAN = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
#Termina aporte Adrian Litardo
#Kevin Ibarra
t_POINT = r'.'

#Empieza aporte Adrian Litardo
#Expresion regular para hash
def t_HASH(t):
    r'[a-fA-F0-9]{32}' #Solo acepta hash de 32 caracteres
    t.value = reserved.get(t.value, 'HASH')
    return t
#Termina aporte Adrian Litardo
def t_VARIABLE(t):
    r'[_a-zA-Z]\w{0,14}'#Acepta nombres de variables de hasta 14 caracteres, modificacion de Adrian Litardo
    t.type = reserved.get(t.value,'VARIABLE')
    return t

#Expresión regular para reconocer números flotantes
def t_FLOAT(t):
    #Aporte de Adrian Litardo modificando la expresion regular
    r'-?[0-9]+\.[0-9]+' #Ahora acepta números flotantes negativos
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

#Empieza aporte Adrian Litardo
#Expresion regular para booleanos
def t_BOOLEAN(t):
    r'true|false'
    t.value = reserved.get(t.value, 'BOOLEAN')
    return t
#Expresion regular para while
def t_WHILE(t):
    r'while[^:]*:'
    t.value = reserved.get(t.value, 'WHILE')
    return t
#Termina aporte Adrian Litardo

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
#Adrian Litardo
data_Adrian = 'while x < 5: -3.45 == 3e25960a79dbc69b674cd4ec67a72c62; true != false'
#
lexer.input(data_Adrian)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)