# Ejemplo 1
def crear_funcion(num_uno, num_dos):  # Closure

    def validacion():
        print("Se ejecuta validacion")
        return num_uno > 0 and num_dos > 0

    return validacion

# Ejemplo 2


def aplicar_funcion(func):
    resultado = func()
    print(resultado)

# closures, son funciones que crean funciones (cuando returnamos la funcion anidada) primer ejemplo

# Una funcion como argumento a otra funcion, ejemplo 2


nueva_funcion = crear_funcion(10, 2)
# Algoritmo
#print( nueva_funcion() )
aplicar_funcion(nueva_funcion)
