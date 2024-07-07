import ply.yacc as yacc
import logging
import datetime
import sys
from analizador_lexico import tokens

#Agregar todas las variables declaradas
variables = {}


def p_programa(p):
    '''programa : expresion
                | list
                | length_list
                | declaracion'''


def p_expresion(p):
    'expresion : valor operador valor'

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


def p_condicion(p):
    '''condicion : valor comparador valor
                 | condicion conector condicion
    '''


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