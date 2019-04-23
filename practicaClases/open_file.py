# archivo = open("CRE_Acetobacteraceae.txt")
# for i, línea in enumerate(archivo):
#     línea = línea.rstrip("\\n")
#     print (" %4d: %s" % (i, línea))
# archivo.close()

#La llamada a rstrip es necesaria ya que cada línea que se lee del archivo contiene un fin
#de línea y con la llamada a rstrip("\\n") se remueve.

# Funcion para la lectura de los ficheros

def readinputdata(filename,modo):

    def ordenar(lista):
        lista.sort()
        return lista

    # def limpiar(lista):

    #     return ordenar(lista)            

    lista = []
    
    # archivo = open(filename,modo)
    
    # for line in archivo.readlines():
    #     lista.append(line)
    
    # archivo.close()



    with open(filename,modo) as lineas:
        for linea in lineas:
            lista.append(linea)

    return ordenar(lista)

# Entrada de Datos

 

data = readinputdata("CRE_Acetobacteraceae.txt","r") # Aqui pones el nombre del fichero de entrada

print(data)
