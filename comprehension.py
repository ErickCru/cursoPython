"""
lista = []
for valor in range(0,101):
    list.append(valor)
"""

#Lo que se encuentra antes del for es lo que se va agregar a la lista
lista = [valor for valor in range (0, 101) if valor % 2 == 0]

"""
Reglas
1. Valor a agregar a la lista.
2. Un ciclo.
Se pueden usar condicionales o ciclos.
Aunque recordar la lectura de codigo de python.
"""

#Para las tuplas hay que usar tuple
tupla = tuple ( (valor for valor in range (0, 101) if valor % 2 != 0) )

diccionario = { indice:valor for indice, valor in enumerate(lista) if indice < 10 }

#print(lista)
#print(tupla)
print(diccionario)