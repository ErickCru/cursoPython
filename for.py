lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
    pass

"""
range con 1 campo toma del 0 hasta el valor que le damos, con 2 campos nos indica de donde comienza y donde termina y
con 3 campos nos indica donde comienza, donde termina y de cuanto en cuanto irá aumentando
"""
nuevo_range = range(0, 20, 4)

for valor in nuevo_range:
    pass

#enumerate nos regresa dos valores el indice y el valor
for indice, valor in enumerate(lista):
    pass#print(valor, "tiene el indice", indice)

#len() nos regresa la longitud del objeto interable

for valor in range(0, len(lista) ):
    pass#print(valor)

diccionario = {'a': 10, 'b' : 20, 'c' : 500}

#items() es igual a enumerate() pero se usa con los diccionarios
for llave, valor in diccionario.items():
    print("La llave ", llave, "tiene el valor de" , valor)