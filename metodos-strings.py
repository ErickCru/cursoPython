course = 'Curso'
my_string = 'Código Facilito!'

""" Formato """
result = '{} de {}'.format(course,my_string)

#Usando alias
result = '{a} de {b}'.format(a = course,b = my_string)

#Pasa el string a minusculas, dando otro string
result = result.lower()

#Pasa el string a mayusculas, dando otro string
#result = result.upper()

#Pasa el string como un titulo, dando otro string
#result = result.title()

""" Busqueda """
#Regresa la posicion en que empieza la palabra
pos = result.find('Código')

#Conteo
count = result.count('c')

#remplazo
new_string = result.replace('c', 'x')

#secciona en pequeños bloques, cada vez que se encuentre con el campo que se le pasa corta el string y devueve una lista
new_string = result.split(' ')

print(new_string)