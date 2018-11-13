# Lectura y retorno de los valores del archivo.
# EL archivo a abrir debe estar junto con este código.
def lectura_archivo(nombre_archivo, permiso):
    archivo = open(nombre_archivo, permiso)
    contenido = [] 
    first_line = ""
    second_line = ""
    for indice, linea in enumerate(archivo.readlines()):
        if indice == 0:
            first_line = linea.strip('\n')
            contenido.append(first_line)
            continue
        # En caso de que el archivo tenga más de un titulo.  
        for caracter in linea.strip('\n'):
            if caracter == '>':
                first_line = linea.strip('\n')
                contenido.append(second_line)
                contenido.append(first_line)
                second_line = ""
                break
            second_line += caracter
    contenido.append(second_line)
    archivo.close()
    return contenido

# Se llama a la función de lectura_archivo() para obtener los valores del archivo 
# y guardarlos en la variable lista.
lista = lectura_archivo('demo.fasta','r')

# Valores que debe tener la secuencia DNA
valores_validos = ('A','T','C','G')


# Recorrido del contenido de la lista para obtener los caracteres válidos de la secuencia DNA.
for indice, contenido in enumerate(lista):
    # En la posiciones pares tendremos a los titulos.
    # Por lo cual se trabaja con las posiciones impares.
    if indice % 2 != 0:
        pos_inicio = 0
        pos_final = 0
        secuencia_valida = ""
        inicio = True
        cont = 1
        print ("Resultados: ")
        for indice, caracter in enumerate(contenido):
            if caracter in valores_validos:
                if inicio:
                    pos_inicio = indice
                    inicio = False
                elif indice == len(contenido) - 1:
                    pos_final = indice
                    print("String{} : {}. start: {} end: {}\n".format (cont, secuencia_valida, pos_inicio + 1, pos_final + 1))
                secuencia_valida += caracter
            elif secuencia_valida != "":
                inicio = True
                pos_final = indice - 1
                print("String{} : {}. start: {} end: {}\n".format (cont, secuencia_valida, pos_inicio + 1, pos_final + 1))
                cont+=1
                secuencia_valida = ""
