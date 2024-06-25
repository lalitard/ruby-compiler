import ply.yacc as yacc
import logging
import datetime
from analizador_lexico import tokens

#Empieza aporte de Carlos Cabanilla 24/06
username= "carlosCabani" 
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
                | tupla
                | declaracion
                | if
                | solicitud
    '''


def p_expresion(p):
    'expresion : valor operador valor'


def p_imprimir(p):
    'imprimir : PRINT LPAREN valores RPAREN'


def p_imprimir_vacio(p):
    'imprimir : PRINT LPAREN RPAREN'


def p_valores(p):
    '''valores : valor
               | valor COMMA valores
    '''


def p_sentenciaIf(p):
    'if : IF LPAREN condicion RPAREN COLON programa ELSE programa'


def p_condicion(p):
    '''condicion : valor comparador valor
    '''

def p_comparador(p):
    '''comparador : LESS_THAN
                  | GREATER_THAN
    '''


def p_valor(p):
    '''valor : VARIABLE
             | INTEGER
             | FLOAT
             | tupla
             | expresion
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
                  | EQUAL
                  | NOT_EQUAL
                  | LESS_EQUAL
                  | GREATER_EQUAL
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
    'case : CASE valor WHEN condicion programa WHEN condicion programa ELSE programa END' 


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
    if not s: continue
    #Aporte Carlos Cabanilla 24/06
 # Configura un nuevo archivo de log para cada entrada
    setup_logging(username)
    
    result = parser.parse(s)
    print(result)
#Termina aporte Adrian Litardo