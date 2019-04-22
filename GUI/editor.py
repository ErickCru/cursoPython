from tkinter import *
from tkinter import filedialog as F
from io import open

# funciones del editor

ruta = ""  # Guardaremos la ruta de un fichero


def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title("Mi editor")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = F.askopenfilename(initialdir="./", filetypes=(
        ("Archivos de texto", "*.txt"),), title="Abrir archivo")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")


def guardar():
    global ruta
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El archivo se ha guardo correctamente")
    else:
        guardar_como()


def guardar_como():
    global ruta
    mensaje.set("Guardar fichero como...")
    fichero = F.asksaveasfile(title="Guardar archivo",
                              mode="w", defaultextension=".txt")

    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El archivo se ha guardado correctamente")
    else:
        mensaje.set("Se ha cancelado el guardado")
        ruta = ""


# Configuración de la raíz
root = Tk()
root.title("Mi editor")

# Menú superior
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Cajar de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

# Agregamos el menú a la pantalla
root.config(menu=menubar)

# Bucle de la aplicación
root.mainloop()
