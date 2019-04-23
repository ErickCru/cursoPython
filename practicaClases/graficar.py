import matplotlib.pyplot as plt

valores = []

archivo = open("CRE_Acetobacteraceae.txt")
for linea in archivo:
    if linea.rstrip("\\n"):
        valores.append(',')
    
    valores.append(linea)
archivo.close()

print(valores)