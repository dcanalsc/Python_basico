from pprint import pprint

#Enunciado del ejercicio:

#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#   Color
#   Ruedas
#   Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#   Velocidad
#   Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = None
    ruedas = None
    puertas = None

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

miCoche = Coche()
miCoche.ruedas = 4
miCoche.color = "Rojo"
miCoche.puertas = 3
miCoche.velocidad = 50
miCoche.cilindrada = 1600

pprint(vars(miCoche))
