#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
#Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100,
# y también si es divisible entre 400.

def bisiesto(year):
    if (((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
        return True
    else:
        return False

print("Introduce el año:")
if bisiesto(int(input())):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")


