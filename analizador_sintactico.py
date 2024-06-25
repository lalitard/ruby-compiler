import ply.yacc as yacc
import logging
import datetime
import sys
from analizador_lexico import tokens
# t_BOOLEAN = r'true|false'
# t_BREAK = r'break'
# t_DEF = r'def'
# t_EXPONENT = r'\*\*'
# t_FALSE = r'false'
# t_FOR = r'for'
# t_HASH = r'\#'
# t_IN = r'in'
# t_IP = r'(?:\d{1,3}\.){3}\d{1,3}'
# t_LIST = r'\[\s*([a-zA-Z_][a-zA-Z0-9_]*|\d+)\s*(,\s*([a-zA-Z_][a-zA-Z0-9_]*|\d+)\s*)*\]'
# t_NOT = r'not'
# t_POINT = r'\.'
# t_RETURN = r'return'
# t_SEMICOLON = r';'
# t_TRUE = r'true'
# t_WHILE = r'while[^:]*:'



#Empieza aporte de Carlos Cabanilla 24/06
username= "lalitard"
# Configura el registro
def setup_logging(username):
    now = datetime.datetime.now()
    log_filename = f"logs/sintactico-{username}-{now.strftime('%d%m%Y-%Hh%M')}.txt"
    logging.basicConfig(filename=log_filename, level=logging.ERROR, format='%(message)s')

def log_error(message):
    logging.error(message)
    print(message)

setup_logging(username)

def p_programa(p):
    '''programa : expresion
                | imprimir
                | declaracion
                | sentenciaIf
                | solicitud
                | sentenciaCase
    '''


def p_expresion(p):
    '''expresion : valor operador valor
    '''

#Aporte Adrian Litardo 24/06
def p_expresion_binaria(p):
    '''expresion : expresion operador valor
    '''

def p_expresion_par(p):
    'expresion : LPAREN expresion RPAREN'
    p[0] = p[2]

def p_expresion_mul_div(p):
    '''expresion : expresion TIMES valor
                 | expresion DIVIDE valor
    '''
    p[0] = (p[2], p[1], p[3])

def p_expresion_add_sub(p):
    '''expresion : expresion PLUS valor
                 | expresion MINUS valor
    '''
    p[0] = (p[2], p[1], p[3])

#Con esta reglas manejamos las precedencias de las operaciones en la expresion
#Termina aporte Adrian Litardo
def p_imprimir(p):
    'imprimir : PRINT LPAREN valores RPAREN'


def p_imprimir_vacio(p):
    'imprimir : PRINT LPAREN RPAREN'


def p_valores(p):
    '''valores : valor
               | valor COMMA valores
    '''


def p_sentenciaIf(p):
    'sentenciaIf : IF LPAREN condicion RPAREN COLON programa ELSE programa'



def p_valor(p):
    '''valor : VARIABLE
             | INTEGER
             | FLOAT
             | tupla
    '''


def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
    '''

#Aporte Kevin Ibarra
def p_condicion(p):
    '''condicion : valor comparador valor
                 | condicion conector condicion
    '''

def p_comparador(p):
    '''comparador : LESS_THAN
                  | GREATER_THAN
                  | EQUALS
                  | NOT_EQUALS
                  | LESS_EQUAL_THAN
                  | GREATER_EQUAL_THAN
    '''

def p_conector(p):
    '''conector : AND
                | OR
    '''
def p_tupla(p):
    'tupla : LPAREN valores RPAREN'


def p_declaracion(p):
    'declaracion : VARIABLE EQUAL valor'

#Aporte de Carlos Cabanilla 24/06
def p_solicitud(p):                              
    'solicitud : INPUT LPAREN COMILLA STRING COMILLA RPAREN'

def p_sentenciaCase(p):
    'sentenciaCase : CASE valor WHEN condicion programa WHEN condicion programa ELSE programa END'


# Regla para manejar errores sintácticos
def p_error(p):
    error_message = "Syntax error in input!"
    log_error(error_message)

# Construcción del analizador
parser = yacc.yacc()

# Bucle principal para leer la entrada del usuario y analizarla
while True:
    try:
        s = input('lp > ')
    except EOFError:
        break
    if not s:
        continue
    #Aporte Carlos Cabanilla 24/06
 # Configura un nuevo archivo de log para cada entrada
    setup_logging(username)
    result = parser.parse(s)
    print(result)
#Termina aporte Adrian Litardo