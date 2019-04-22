from tkinter import *
from tkinter import messagebox as M
from tkinter import colorchooser as C
from tkinter import filedialog as F

root = Tk()


def test():
    #Title, content
    M.showinfo("Hola", "Hola mundo")
    # M.showwarning("Alerta", "Sección solo para administradores")
    # M.showerror("Error", "Ha ocurrido un error inesperado.")
    # resultado = M.askquestion("Salir", "¿Está seguro de salir sin guardar?")
    # if resultado == 'yes':
    #     root.destroy()
    #resultado = M.askokcancel("Salir", "¿Sobreescribir el fichero actual?")
    # resultado = M.askyesno("Salir", "¿Sobreescribir el fichero actual?")
    # if resultado:
    #     root.destroy()

    # resultado = M.askretrycancel("Reintentar", "No se puede conectar.")
    # if resultado:
    #     root.destroy()

    # color = C.askcolor(title="Elige un color.")
    # print(color)

    # initialdir="directorio_inicial"
    # ruta = F.askopenfilename(title="Abrir un fichero",
    #                          filetypes=(("Fichero de texto", "*.txt"), ("Fichero avanzados", "*.pdf"), ("Todos los ficheros", "*.*")))
    # print(ruta)
    # Equivale a open('ruta', 'w')
    # fichero = F.asksaveasfile(
    #     title="Guardar un fichero", mode="w", defaultextension=".txt")
    # if fichero is not None:
    #     fichero.write("Hola!")
    #     fichero.close()


Button(root, text="Click", command=test).pack()

root.mainloop()
