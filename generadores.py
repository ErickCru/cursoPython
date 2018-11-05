#Crear objetos sin almacenarlos en memoria RAM
#def return_valores():
 #   print("Hola mundo 1")
  #  return True #Termina la funcion

#print(return_valores())

#Generalmente se trabajan con un loop (for-while)
def generador(*args):
    for valor in args:
        yield valor * 10, True #en vez de return, regresa el valor e intera de nuevo


for valor_uno, valor_dos in generador(1,2,3,4,5,6,7,8,9):
    print(valor_uno,valor_dos)
