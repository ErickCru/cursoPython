#En python las funciones son clases
def generador(*args):
    """ recibe n cantidad de números y regresa el número, además de regresar True
        o False si el número es mayor a 5
    """
    for valor in args:
        yield valor * 10, True if valor > 5 else False

nombre = generador.__name__
documentacion = generador.__doc__

print(nombre, " : ")
print(documentacion)}

#A traves del interprete

# importamos la funcion de lo que queremos documentar
#nombre archivo y luego nombre de la funcion
# from docstring import generador
# help ( generador )