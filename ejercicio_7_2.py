#   Enunciado del ejercicio:
#   En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
#   Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
#   En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
#   haréis una operación para calcular el tiempo que queda de trabajo.

import time


print('Fecha del sistema:', time.ctime(time.time()))
if time.localtime().tm_hour >= 19:
    print("Hora de irse a casa")
else:
    horas = 18 - time.localtime().tm_hour
    minutos =  59 - time.localtime().tm_min
    segundos = 60 - time.localtime().tm_sec
    print("Seguimos, quedan:", "{} horas {} minutos {} segundos".format(horas,minutos,segundos))