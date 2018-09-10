#Al colocar un "*" al argumento le dice al interprete python que puede recibir n argumentos

#Es una convencion usar args como campo
"""
def suma(*args):
    resultado = 0
    for valor in varibales:
        resultado += valor 
    #print(type(varibales))
    return resultado

resultado = suma(1,2,3,4,5,6,7,8,9)
print(resultado)
"""

def suma(**kwargs):
   valor = kwargs.get('valor', 'No contiene el valor')
   print(valor)

resultado = suma(valor = 'Eduardo', x = 2, y = 2, z = True)
print(resultado)
# * -> n valores -> tuplas

# ** -> n valores -> diccionarios

