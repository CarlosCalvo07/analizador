import ply.yacc as yacc
from Examen import tokens, lexico  # Importa los tokens desde tu analizador léxico

# Reglas de la gramática
def p_for_loop_correct(p):
    '''statement : PR'''
    print("Estructura correcta: bucle for")
    p[0] = ('for_loop', p[1], 'correcta')

def p_for_loop_incorrect(p):
    '''statement : ID'''
    print("Estructura incorrecta")
    p[0] = ('identifier', p[1], 'incorrecta')

# Manejo de errores sintácticos
def p_error(p):
    print("Error de sintaxis en '%s'" % p.value)

# Construir el analizador sintáctico
parser = yacc.yacc()

def sintactico(text):
    tokens = lexico(text)  # Primero, analizamos léxicamente
    result = parser.parse(text)
    return result

if __name__ == '__main__':
    # Ejemplo para probar el analizador sintáctico
    while True:
        try:
            s = input('Ingresa el código: ')  # Recibe el código como entrada
        except EOFError:
            break
        if not s:
            continue
        result = sintactico(s)
        print(result)