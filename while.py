contador = 0
bandera = True

while bandera:
    print(contador)
    contador +=1

    if contador == 5:
        continue

    if contador == 6:
        bandera = False

else:
    print('El while a terminado')