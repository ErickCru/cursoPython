from tkinter import *

root = Tk()
opcion = IntVar()


def selecionar():
    monitor.config(text=f"{opcion.get()}")


def reset():
    opcion.set(None)
    monitor.config(text="")


Radiobutton(root, text="Opción 1", variable=opcion,
            value=1, command=selecionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion,
            value=2, command=selecionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion,
            value=3, command=selecionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()
