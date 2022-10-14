#Enunciado del ejercicio:

#   En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
#   y que contenga un botón de reinicio para que deje todo como al principio.
#   Al principio no tiene que haber una opción seleccionada.

from tkinter import *

def selec():
    monitor.config(text = f'{opcion.get()}')

def reset():
    opcion.set(None)          # Reiniciamos el seleccionable
    monitor.config(text='')   # Reiniciamos la etiqueta


root = Tk()
root.config(bd=10)

opcion = StringVar()
opcion.set(None)

Radiobutton(root, text="Manuela", variable=opcion,
            value="Manuela", command=selec).pack()
Radiobutton(root, text="Opción 2", variable=opcion,
            value="Opción 2", command=selec).pack()
Radiobutton(root, text="Juliana", variable=opcion,
            value="Juliana", command=selec).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()