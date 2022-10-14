#Enunciado del ejercicio:

#   En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista
#   de elementos seleccionables, también debe de tener un label con el texto que queráis.

from tkinter import *

root = Tk()
root.config(bd=15)

leche = IntVar()      # 1 si, 0 no
azucar = IntVar()    # 1 si, 0 no
descafeinado = IntVar()     # 1 si, 0 no

Label(root,text="¿Cómo quieres el café?").grid(column=0,row=0)
Label(root,text="").grid(column=0,row=1)
Checkbutton(root, text="Con leche", variable=leche,
            onvalue=1, offvalue=0).grid(column=0,row=2)
Checkbutton(root, text="Con azúcar",variable=azucar,
            onvalue=1, offvalue=0).grid(column=1,row=2)
Checkbutton(root, text="Descafeinado", variable=descafeinado,
            onvalue=1, offvalue=0).grid(column=2,row=2)

root.mainloop()