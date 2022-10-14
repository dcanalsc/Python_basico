#Enunciado del ejercicio:

#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    marca = None
    color = None

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    def __str__(self):
        return "Marca {} y color {}".format(self.marca,self.color)

#creamos el objeto y lo guardamos en un fichero

f = open ('coche.bin', 'wb')
coche = Vehiculo("honda","rojo")
pickle.dump(coche, f)
f.close()
print("Este es el coche que he escrito:", coche)

#leemos el objeto del fichero

read = open ('coche.bin','rb')
coche2 = pickle.load(read)
read.close()
print("Este es el coche que he leido:", coche2)