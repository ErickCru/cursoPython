import matplotlib.pyplot as plt
import numpy as np

def read_file(filename,mode):
    ruta = '../material/'
    archivo = open(ruta+filename,'r')
    valores = []
    for linea in archivo.readlines():
        lista = []
        for element in linea.split(','): 
            lista.append(float(element))
        valores.append(lista)
    archivo.close()
    return valores

lista = read_file('CRE_Anaplasmataceae.txt','r')
lista2 = read_file('CRE_Brucellaceae.txt','r')
lista3 = read_file('CRE_Chlorobia.txt','r')
lista4 = read_file('CRE_Bacteroidia.txt','r')

#Rango para mostrar en el eje X del 5 al 20
rango = np.arange(5,21)

#Titulo de la ventana
plt.figure("Graficas")

#Dibujando las graficas en una sola
plt.subplot(221)
plt.plot(rango,lista)
plt.title('Anaplasmataceae')

plt.subplot(222)
plt.plot(rango,lista2)
plt.title('Brucellaceae')

plt.subplot(223)
plt.plot(rango,lista3)
plt.title('Chlorobia')

plt.subplot(224)
plt.plot(rango,lista4)
plt.title('Bacteroidia')

plt.show()

