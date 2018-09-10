"""
Es igual a una lista/tupla la diferencia es que no se rige en base de indices.
Los valores que almacenan son en forma de llave-valor donde las llaves debe ser inmutables.
Si hay dos llaves iguales, toma el valor de la última llave 
"""

diccionario = { 'a' : True, 5: "esto es un string", 'a' : 100, 'a' : False }

#Añadir nuevos contenidos
diccionario['c'] = 'nuevo string'

#Para modificar valor
diccionario['a'] = False

"""
Si la llave se encuentra se modifica el valor y sino se crea el valor
"""

#Obtener los datos
#valor = diccionario['a']

#obtener datos mediante get, primer campo llave a buscar, segundo campo lo que regresará en caso de no encontrar
valor = diccionario.get('z', "No se encontró")

#Eliminar contenido
#del diccionario[5]

#print(diccionario)
#print(valor)

#Nos regresa un objeto interable donde nos regresa todas las llave
llaves = list ( diccionario.keys() )
valores = tuple( diccionario.values() )

diccionario_dos = {'z' : 23, 'w' : 88}

#Extender diccionarios
diccionario['z'] = diccionario_dos['z']
diccionario['w'] = diccionario_dos['w']

#Forma adecuada, donde primero va el diccionario que contendra al otro
diccionario.update(diccionario_dos)

#print(llaves)
#print(valores)
print(diccionario)