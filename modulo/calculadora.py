#!/usr/bin/python3
"""
Aqui colocamos lo que hace el modulo a que contexto le corresponde
"""
#Metadatos

__author__ = "Erick"
__copyright__ = "Copyright 2018"
__credits__ = "Codigo Facilito"

__license__ = "GLP"
__version__ = "1.0.0"
__maintainer = "Erick"
__email__ = "erick3ftv@gmail.com"
__status__ = "Developer"

def suma(num_uno, num_dos):
    """Regresa un número entero el cual es el resultado de una suma"""
    return num_uno + num_dos

def resta(num_uno, num_dos):
    """Regresa un número entero el cual es el resultado de una resta"""
    return num_uno - num_dos

def multiplicacion(num_uno, num_dos):
    """Regresa un número entero el cual es el resultado de una multiplicacion"""
    return num_uno * num_dos

def division(num_uno, num_dos):
    """Regresa un número entero el cual es el resultado de una division"""
    return num_uno / num_dos

def saluda():
    print("Saluda")
    
#Estructura de un modulo

if __name__ == '__main__':
    saluda()


