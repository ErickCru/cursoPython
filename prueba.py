""" Operadores encadenados """

numero = 35
# if numero >= 0 and numero <= 100:
#     print(f"El número {numero} está entre 0 y 100")
# else:
#     print(f"El número {numero} no está entre 0 y 100")

if 0 <= numero <= 100:
    print(f"El número {numero} está entre 0 y 100")
else:
    print(f"El número {numero} no está entre 0 y 100")

""" Compresión de listas """

lista = [letra for letra in "Casa"]
print(lista)

lista = [num**2 for num in range(0, 10)]
print(lista)

lista = [num for num in range(0, 11) if num % 2 == 0]
print(lista)

pares = [num for num in [num**2 for num in range(0, 11)] if num % 2 == 0]
print(pares)

""" Ámbitos y funciones decoradoras """


def monitorizar_args(funcion):

    def decorar(*args, **kwargs):
        print(
            f"\n\t *Se está apunto de ejecutar la función: {funcion.__name__}")

        funcion(*args, **kwargs)

        print(
            f"\t *Se ha finalizado la ejecución de la función: {funcion.__name__} \n")
    return decorar


@monitorizar_args
def hola(nombre):
    print(f"Hola {nombre}")


@monitorizar_args
def adios(nombre):
    print(f"adios {nombre}")


hola("Erick")
adios("Alonzo")

""" Funciones lambda """


def dolar(num): return num * 2


# r = lambda numero: numero*2
# impar = lambda num: num%2!=0
# revertir = lambda cadena: cadena[::-1]
# suma = lambda x,y: x+y
""" Función Filter """
numeros = [2, 5, 10, 23, 50, 33]
list(filter(lambda numero: numero % 5 == 0, numeros))


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} de {self.edad} años"


personas = [
    Persona("Erick", 23),
    Persona("Martha", 16),
    Persona("Manuel", 76),
    Persona("Luis", 12),
]

personas

menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)

""" Función map """

numeros = [2, 5, 10, 23, 50, 33]

print(list(map(lambda x: x*2, numeros)))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15]

print(list(map(lambda x, y, z: x*y*z, a, b, c)))

# Incrementar las edades de las personas.ArithmeticError
# def incrementar(persona):
#     persona.edad += 1
#     return persona
# personas = map(incrementar, personas)
# for persona in personas:
#     print(persona)

personas = map(lambda persona: Persona(
    persona.nombre, persona.edad+1), personas)

for persona in personas:
    print(persona)
