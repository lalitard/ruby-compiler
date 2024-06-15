 #Inicio aporte Carlos Cabanilla
import ply.lex as lex


#definición de tokens
tokens = ['INTEGER', 
          'PLUS', 
          'MINUS', 
          'TIMES', 
          'DIVIDE',
          'FLOAT',
          'WORD',
          'IP'
          ]

#Expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

#Expresión regular para reconocer direcciones IP
def t_IP(t):
    r'(?:\d{1,3}\.){3}\d{1,3}'
    return t

#Expresión regular para reconocer números enteros y flotantes
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

#Expresión regular para reconocer palabras
def t_WORD(t):
    r'[a-zA-Z]+'
    return t

#Expresión regular para reconocer números flotantes
def t_FLOAT(t):
    r'\d*\.?(\d+|.)'
    t.value = float(t.value)
    return t

#Ignorar caracteres como espacios y saltos de línea
t_ignore = ' \n'

#Manejo de errores de token
def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)

#Construcción del analizador léxico
lexer = lex.lex()

#Informacion a verificar
data = "La direccion IP del pc involucrado es 194.111.10.3"
lexer.input(data)

#Obtener los tokens reconocidos
while True:
    token = lexer.token()
    if not token:
        break
    print(token)

#Fin aporte Carlos Cabanilla