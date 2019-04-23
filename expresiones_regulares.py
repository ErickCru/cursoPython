import re

texto = "En esta cadena se encuentra una palabra mágica"

palabra = "mágica"

encontrado = re.search(palabra, texto)

if encontrado is not None:
    print("Se ha encontrado la palabra")
else:
    print("No se he encontrado la palabra")

encontrado.start()
encontrado.end()
encontrado.span()
encontrado.string

# Match busca al principio
texto = "Hola mundo"
print(re.match("mundo", texto))

# Split divide la cadena
texto = "Vamos a dividir la cadena"
re.split(' ', texto)

# sub de sustituir las coincidencias
texto = "Hola amigo"
re.sub('amigo', 'amiga', texto)

# findall() busca todas las coincidencias
texto = "hola adios hola hola"
re.findall('hola', texto)

texto = "hola adios hello hola hola bye"
print(re.findall("(hola|hello)", texto))

texto = "hla hola hoola hooola hoooooola"
re.findall('hola', texto)


def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))


# '*' 0 o mas veces '+' 1 o mas veces '?' una o ninguna vez
# {num} numero de veces que se repita
# {n,m} rango de veces que se repita
# [] conjunto de caracteres a buscar
# [^] exclusión - busqueda inversa
# [-] rango de conjunto
"""
Caracteres escapados \
    \d numerico
    \D no numerico
    \s espacio en blanco
    \S no espacio en blanco
    \w alfanumerico
    \W no alfanumerico
    en python anterponer r''
    [r'\d']
"""

# patrones = ['hla', 'hola', 'hoola']
# patrones = ['ho+', 'ho*', 'ho?']
# patrones = ['ho{0}la', 'ho{1}la', 'ho{2,4}la']
texto = "hola hela hila hala hula"
patrones = ['h[ou]la', 'h[aio]la']
buscar(patrones, texto)
