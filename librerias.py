#Random
"""
import random

valor = random.randint(0,10)

lista = [True, "Strings", 23, False]

valor = random.choices( lista )

print(lista)

random.shuffle (lista)

print(lista)"""

#Tiempo
"""
import datetime

print(datetime.datetime.now())"""

#Sys
import sys
#import time

#for i in range(100):
#    time.sleep(0.5)
#    sys.stdout.write("\r%d %%" % i)
#    sys.stdout.flush()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Es necesario colocar por lo menos un argumento")
    else:
        if sys.argv[1] == 'help':
            print('puedes contactar a Erick si tienes alguna duda')
        #print ( sys.argv[1] )

