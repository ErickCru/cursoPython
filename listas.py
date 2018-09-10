my_list = ["strings", 15, 15.6, True]

""" Agregacion de datos """
#Recibe como parametro y lo almacena en la ultima posicion
my_list.append(6)

#Recibe dos campos, entero donde indica la posicion y luego el valor
my_list.insert(1, "insert")

""" Eliminacion de datos """
#Elimina las coincidencias
my_list.remove(15) 

print(my_list)

#Extrae y elimina el ultimo valor
last_value = my_list.pop()

print(last_value)

print(my_list)

""" Listas solo con números """

my_list_numeros = [1,9,22,6,8,65,14,99]

my_list_numeros_dos = [22,23]

#Ordenamiento ascendente
my_list_numeros.sort()

#Ordenamiento descendente
my_list_numeros.sort(reverse = True)

#combinar dos listas
my_list_numeros.extend(my_list_numeros_dos)

#añade una lista a otra
my_list_numeros.append(my_list_numeros_dos)

print(my_list_numeros)