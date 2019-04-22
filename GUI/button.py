from tkinter import *

root = Tk()
root.title("Operaciones")
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()


def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()


def resta():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()


def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()


def borrar():
    n1.set("")
    n2.set("")


Label(root, text="Número 1").pack()
Entry(root, justify="center", textvariable=n1).pack()  # Primer número
Label(root, text="Número 2").pack()
Entry(root, justify="center", textvariable=n2).pack()  # Segundo número
Label(root, text="\nResultado").pack()
Entry(root, justify="center", textvariable=r,
      state="disabled").pack()  # Resultado número
Label(root, text="\n").pack()

Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")


root.mainloop()
