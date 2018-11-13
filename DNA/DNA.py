# Lectura y retorno de los valores del archivo.
# EL archivo a abrir debe estar junto con este código.
def lectura_filtrado_archivo(nombre_archivo, permiso):
    archivo = open(nombre_archivo, permiso) 
    second_line = ""
    for i, linea in enumerate(archivo.readlines()):
        if i != 0:
            second_line += linea.strip('\n')
    archivo.close()
    return second_line

# Se llama a la función de lectura_filtrado_archivo() para obtener los valores del archivo 
# y guardarlos en la variable valores.
valores = lectura_filtrado_archivo('demo.fasta','r')

# Valores que debe tener la secuencia DNA
valores_validos = ('A','T','C','G')

# Recorrido del contenido de la lista para obtener los caracteres válidos de la secuencia DNA.
pos_inicio = 0
pos_final = 0
secuencia_valida = ""
# variable para detectar que ya se ha encontrado un caracter válido.
inicio = True
cont = 1
print ("Resultados: ")
for indice, caracter in enumerate(valores):
    if caracter in valores_validos:
        secuencia_valida += caracter
        if inicio:
            pos_inicio = indice
            inicio = False
        # En caso de llegar al final y haya caracteres validos
        elif indice == len(valores) - 1:
            pos_final = indice
            print("String{} : {}. start: {} end: {}\n".format (cont, secuencia_valida, pos_inicio + 1, pos_final + 1))
    elif secuencia_valida != "":
        inicio = True
        pos_final = indice - 1
        print("String{} : {}. start: {} end: {}\n".format (cont, secuencia_valida, pos_inicio + 1, pos_final + 1))
        cont += 1
        secuencia_valida = ""
        