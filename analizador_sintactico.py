import ply.yacc as yacc

from analizador_lexico import tokens

#Aporte de Adrian Litardo

def p_programa(p):
    '''programa : expresion
                | imprimir
                | tupla
                | declaracion
                | if
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
    '''comparador : LESSTHAN
                  | MORETHAN
    '''


def p_valor(p):
    '''valor : VARIABLE
             | INT
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


def p_tupla(p):
    'tupla : LPAREN valores RPAREN'


def p_declaracion(p):
    'declaracion : VARIABLE EQUAL valor'


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('lp > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

#Termina aporte Adrian Litardo