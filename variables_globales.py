
def palindromo():
    nuevo_valor = frase.replace(' ','') #Variables locales
    return nuevo_valor == nuevo_valor[::-1]

frase = 'anita lava la tina' #Variables gloabales
result = palindromo()
print(result)


#Modificar la variable global
"""
def valor_global():
    global variable_global 
    variable_global = 'Cambiar valor'

variable_global = 'Esto es una variable global'

print (variable_global)
valor_global()
print (variable_global)
"""

#Crar la variable global a partir de una funcion

def valor_global():
    global variable_global 
    variable_global = 'Cambiar valor'

def mostrar_global():
    print(valor_global)

def crear_global():
    global nueva_variable
    nueva_variable = 'Esto es una variable global'

crear_global()
print(nueva_variable)
