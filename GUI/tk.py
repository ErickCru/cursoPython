from tkinter import *

# configuracion de la raiz
root = Tk()

# Variables dinámicas
# texto = StringVar()
# texto.set("Un nuevo texto")

# root.title("Hola mundo")

# Tamaño de la ventana
# root.resizable(1, 1)

# Linux
# root.iconbitmap('@nameicon.xbm')

# Win
# root.iconbitmap('nameicon.ico')
"""
Renombrar el archivo a .pyw para esconder
la terminal de fondo.
"""

# frame = Frame(root, width=480, height=320)
# frame.pack()

# se empaquete a si mismo
# Se alinea arriba, al centro por defecto
# frame.pack(side="bottom", anchor="w")

# Rellenar el frame fill(x,y,both), expandir expand=1 (verdadero)
# frame.pack(fill='both', expand=1)

# frame.config(width=480, height=320)
# frame.config(cursor="pirate")
# frame.config(bg="lightblue")
# frame.config(bd=25)
# frame.config(relief="sunken")
# frame.config()

# root.config(cursor="arrow")
# root.config(bg="blue")
# root.config(bd=15)
# root.config(relief="ridge")

# Crear label widget
#label = Label(frame, text="¡Hola mundo!")
# label.pack()
# sino se usara más el label se puede empaquetar directo
# Label(root, text="¡Hola1 mundo!").pack(anchor="nw")
# label = Label(root, text="¡Hola2 mundo!")
# label.pack(anchor="center")
# Label(root, text="¡Hola3 mundo!").pack(anchor="se")

# #fg = color-text
# label.config(bg="green", fg="#fff", font=('Verdana', 24))
# label.config(textvariable=texto)

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

# Al final de todo
root.mainloop()
