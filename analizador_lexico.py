#Inicio aporte Carlos Cabanilla
import ply.lex as lex
import logging
import datetime
import sys

username= "lalitard"
# Configura el registro
def setup_logging(username):
    now = datetime.datetime.now()
    log_filename = f"logs/lexico-{username}-{now.strftime('%d%m%Y-%Hh%M')}.txt"
    logging.basicConfig(filename=log_filename, level=logging.ERROR, format='%(message)s')

def log_error(*args):
    message = ' '.join(str(arg) for arg in args)
    logging.error(message)
    print(message)

setup_logging(username)

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
    'return':'RETURN',
    'break':'BREAK',
    'input':'INPUT',
    'nil':'NIL',
    #Termina aporte Adrian Litardo
    #Empieza aporte Carlos Cabanilla 24/06
    'case': 'CASE',
    'when': 'WHEN',
    'length' : 'LENGTH'
}
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
   'LCOR',
   'RCOR',
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
    'HASH',
    'LPAREN',
    'RPAREN',
    #Termina aporte Adrian Litardo  
    # Aporte Carlos Cabanilla
    'EQUAL',
    'COMILLA' 

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
t_POINT = r'\.'
t_LCOR  = r'\['
t_RCOR  = r'\]'
#Aporte de Carlos Cabanilla 24/06
t_EQUAL= r'='
t_COMILLA = r'\"'
#Aporte Adrian Litardo 24/06
t_LPAREN = r'\('
t_RPAREN  = r'\)'


#Empieza aporte Adrian Litardo

#Comentarios
def t_COMMENT(t):
    r'\#.*'
    pass  # Ignorar comentarios de una sola línea

def t_MULTILINE_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignorar comentarios de múltiples líneas

#Aporte Adrian Litardo 07/07
#Expresion regular para nil
def t_NIL(t):
    r'nil'
    t.type = reserved.get(t.value, 'NIL')
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t
#Expresion regular para hash
def t_HASH(t):
    r'[a-fA-F0-9]{32}' #Solo acepta hash de 32 caracteres
    t.value = reserved.get(t.value, 'HASH')
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t
#Termina aporte Adrian Litardo
def t_VARIABLE(t):
    r'[_a-zA-Z]\w*'#Acepta nombres de variables de hasta 14 caracteres, modificacion de Adrian Litardo
    t.type = reserved.get(t.value,'VARIABLE')
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t

#Expresión regular para reconocer números flotantes
def t_FLOAT(t):
    #Aporte de Adrian Litardo modificando la expresion regular
    r'(\d+\.\d*|\d*\.\d+)' #Ahora acepta números flotantes negativos
    t.value = float(t.value)
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t

#Expresión regular para reconocer números enteros y flotantes
def t_INTEGER(t):
    r'\d+' #Acepta números enteros
    t.value = int(t.value)
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t

#Expresión regular para reconocer direcciones IP
def t_IP(t):
    r'(?:\d{1,3}\.){3}\d{1,3}'
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t

#Kevin Ibarra
def t_LIST(t):
    r'\[\s*([a-zA-Z_][a-zA-Z0-9_]*|\d+)\s*(,\s*([a-zA-Z_][a-zA-Z0-9_]*|\d+)\s*)*\]'
    t.value = eval(t.value)  # Convertir el string en una lista de Python
    t.type = 'LIST'
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t
def t_STRING(t):
  r'[\"\'](\\.|[^\"\'])*[\"\']' #Acepta comillas simples o dobles
  t.value = t.value[1:-1]  # Eliminar comillas
  # Registro del token justo antes de retornarlo
  log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
  return t

#Empieza aporte Adrian Litardo
#Expresion regular para booleanos
def t_BOOLEAN(t):
    r'true|false'
    t.value = reserved.get(t.value, 'BOOLEAN')
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t
#Expresion regular para while
def t_WHILE(t):
    r'while[^:]*:'
    t.value = reserved.get(t.value, 'WHILE')
    # Registro del token justo antes de retornarlo
    log_error(f"LexToken({t.type},'{t.value}',{t.lineno},{t.lexpos})")
    return t
#Termina aporte Adrian Litardo

# Aporte Carlos Cabanilla 24/06


# Fin aporte Carlos Cabanilla 24/06

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
#Aporte de Adrian Litardo
def t_error(t):
    log_error(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#Aporte de Adrian Litardo
#Creacion de logging automatizado para cada usuario

#Termina aporte Adrian Litardo

#Informacion a verificar
data_Carlos = "La direccion IP 194.111.10.3 es 23.2 > 50 "
#Kevin Ibarra
data_Kevin = '[1, 2, 3] [1,2,3] ="Hola mundo"'
#Adrian Litardo
data_Adrian = '''
# Esto es un comentario
def myFunction():
    x = 3 + 4.5
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")
    # Comentario de una línea
    /* Comentario
       de múltiples líneas */
    while x < 10:
        x = x + 1
    return x
'''
data_Error = 'h@l4 > ? { 7'

lexer.input(data_Error)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)