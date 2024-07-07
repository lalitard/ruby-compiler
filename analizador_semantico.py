import ply.yacc as yacc
import logging
import datetime
import sys
from analizador_lexico import tokens


username= "lalitard"
# Configura el registro
def setup_logging(username):
    now = datetime.datetime.now()
    log_filename = f"logs/semantico-{username}-{now.strftime('%d%m%Y-%Hh%M')}.txt"
    logging.basicConfig(filename=log_filename, level=logging.ERROR, format='%(message)s')

def log_error(message):
    logging.error(message)
    print(message)

setup_logging(username)


#Agregar todas las variables declaradas
variables = {}


def p_programa(p):
    '''programa : expresion
                | imprimir
                | sentenciaIf
                | solicitud
                | sentenciaCase
                | sentenciaWhile
                | list
                | length_list
                | declaracion
    '''


def p_expresion(p):
    '''expresion : valor operador valor
                | expresion_binaria
                | expresion_par
                | expresion_mul_div
                | expresion_add_sub
    '''

    #Aporte semantico Kevin Ibarra
    if not isinstance(p[1], str) or p[1] in variables:
        pass
    else:
        print(f"Error semántico: La variable {p[1]} no ha sido inicializada.")
        return
    if not isinstance(p[3], str) or p[3] in variables:
        pass
    else:
        print(f"Error semántico: La variable {p[3]} no ha sido inicializada.")
        return
    #Fin aporte semantico Kevin Ibarra
    #Aporte semantico Adrian Litardo
    # Validación de mismos tipos de datos para realizar operaciones
    # Se obtienen los valores reales de p[1] y p[3] para la comparación de tipos
    valor1 = variables[p[1]] if isinstance(p[1], str) else p[1]
    valor3 = variables[p[3]] if isinstance(p[3], str) else p[3]

    if type(valor1) != type(valor3):
        print(f"Error semántico: Los tipos de {p[1]} y {p[3]} son incompatibles para la operación.")
        return
    #Fin aporte semantico Adrian Litardo
def p_expresion_binaria(p):
    '''expresion : expresion operador valor'''

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

def p_imprimir(p):
    'imprimir : PRINT LPAREN valores RPAREN'


def p_imprimir_vacio(p):
    'imprimir : PRINT LPAREN RPAREN'

def p_declaracion(p):
    '''declaracion : VARIABLE EQUAL valor
                  | VARIABLE EQUAL LIST'''
    variables[p[1]] = p[3]

def p_list(p):
    'list : LCOR valores RCOR'
    p[0] = list(p[2])


def p_valores(p):
    '''valores : valor
              | valor COMMA valores'''
    if len(p)==2:
        p[0]=[p[1]]
    else:
        p[0] = [p[1]]+p[3]

#Aporte semantico Adrian Litardo
def p_condicion(p):
    '''condicion : valor comparador valor
                 | condicion conector condicion
    '''
    # Solo se realiza la validación de tipos para comparaciones directas entre valores
    if len(p) == 4:  # Esto indica que la producción es del tipo 'valor comparador valor'
        # Se obtienen los valores reales de p[1] y p[3] para la comparación de tipos
        valor1 = variables[p[1]] if isinstance(p[1], str) and p[1] in variables else p[1]
        valor3 = variables[p[3]] if isinstance(p[3], str) and p[3] in variables else p[3]

        # Se verifica si ambos son instancias de la misma clase (tipo)
        if not isinstance(valor1, type(valor3)):
            print(f"Error semántico: Los tipos de {p[1]} y {p[3]} son incompatibles para la comparación.")
            return
#Fin aporte semantico Adrian Litardo

def p_valor(p):
    '''valor : VARIABLE
             | INTEGER
             | FLOAT
             | expresion
    '''
    if isinstance(p[1], str) and p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0] = p[1]


def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
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
def p_solicitud(p):
    'solicitud : INPUT LPAREN COMILLA STRING COMILLA RPAREN'

def p_sentenciaCase(p):
    'sentenciaCase : CASE valor WHEN condicion programa WHEN condicion programa ELSE programa END'

def p_sentenciaIf(p):
    '''sentenciaIf : IF condicion programa ELSE programa END'''

def p_sentenciaWhile(p):
    '''sentenciaWhile : WHILE condicion programa END'''

#Aporte semantico Kevin Ibarra 
# Regla semántica para el tamaño de una lista
def p_length_list(p):
    'length_list : valor POINT LENGTH'
    if not isinstance(p[1], str) or p[1] in variables:
        if isinstance(p[1], list):
            pass
        else:
            print(f"Error semántico: {p[1]} no es una lista o una variable que contenga una lista.")

    else:
        print(f"Error semántico: La variable {p[1]} no ha sido inicializada.")
#Fin aporte semantico Kevin Ibarra

# Regla para manejar errores sintácticos
def p_error(p):
    error_message = "Syntax error in input!"

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
    result = parser.parse(s)
    print(result)
    print(variables)
#Termina aporte Adrian Litardo