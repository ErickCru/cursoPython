#Si la funcion no tiene return nos regresa none
def factorial_numero(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    return factorial

resultado = factorial_numero(4)
print(resultado)

def suma(valor_uno, valor_dos,valor_tres):
    return valor_uno + valor_dos + valor_tres

def division(valor_uno, valor_dos):
    return valor_uno / valor_dos

def multiplicacion(valor_uno, valor_dos = 10):
    return valor_uno * valor_dos

def multiples_valores():
    return "String", 1, True, 25.6

def mostrar_resultado( funcion ):
    print(funcion(6,8))

#Se puede definir los valores a enviar de las variables
#resultado = division(valor_dos = 10, valor_uno = 100)

#resultado = multiplicacion(valor_uno = 6, valor_dos = 15)

#resultado = multiplicacion(6)

"""
#Regreso de multiples valores
resultado = multiples_valores()

String, entero, bol, floa = multiples_valores()

print(String)
print(entero)
print(bol)
print(floa)
"""


#Asiganar una funcion a una variable
mi_variable = multiplicacion
resultado = mi_variable(8,9)

#Mandar una funcion dentro de una funcion
mi_variable = multiplicacion
mostrar_resultado ( mi_variable )
