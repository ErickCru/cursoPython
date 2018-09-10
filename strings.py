#Lista de caracteres o un objeto
my_string = 'Hola Mundo! "Erick" '

my_string = '''Este es un string que contiene\nsaltos de linea, como puedes ver.\nAdios'''

course = "Python 3"
name = "Erick"

final_message = "Nuevo curso de " + course + " por " + name #1

final_message = "Nuevo curso de %s por %s" %(course, name) #2

final_message = "Nuevo curso de {} por {}".format(course, name) #3

print(my_string)

print(final_message)