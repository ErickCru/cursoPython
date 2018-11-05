# Lectura y returno de los valores del archivo.
# EL archivo a abrir debe estar junto con este código.
def lectura_archivo(nombre_archivo, permiso):
    archivo = open(nombre_archivo, permiso)
    contenido = [] 
    for linea in archivo.readlines():
        contenido.append(linea.strip('\n'))
    archivo.close()
    return contenido

# Valores que debe tener la secuencia DNA
secuencia_valores_validos = ('A', 'T', 'C', 'G')

# Se llama a la función de lectura_archivo() para obtener los valores del archivo 
# y guardarlos en la variable lista.
lista = lectura_archivo('demo.fasta','r')

# Lista para almacenar el/los carater/es que no pertece/n a la secuencia DNA.
lista_secuencia_no_valida = []

# Recorrido del contenido de la lista para obtener los caracteres no válidos de la secuencia DNA.
for indice_linea, linea in enumerate(lista):   
    # El archivo en su primera linea tendrá la cabecera, por lo cual lo saltamos.
    if indice_linea == 0:
        continue
    
    # Variables de control para determinar los caracteres no válidos en la secuencia DNA
    num_linea = indice_linea
    inicio = 0
    fin = 0
    secuencia_no_valido = ""


    for indice_elemento, elemento in enumerate(linea):
        # El archivo puede tener más de un caracter '>' lo que indica que inicia una cabecera,
        # por lo cual se salta y se busca en la siguiente linea.
        if elemento == '>':
            break
       
        # Se realiza la comparación de la secuencia DNA    
        if not elemento in secuencia_valores_validos:

            if inicio < indice_elemento:
                fin = indice_elemento
                secuencia_no_valido += elemento
            else if inicio < indice_elemento + 2:
                inicio = indice_elemento
                fin = indice_elemento
                secuencia_no_valido += elemento

            # Se almacena el caracter no válida junto con su posicion.
            

# Mostrar los caracteres no válidos en la secuencia, asi como su posición.

print(lista_secuencia_no_valida)






        