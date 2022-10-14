#Enunciado del ejercicio:
#   En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares
#   de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos
#   obtenidos mediante reduce.

from functools import reduce

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = list(filter (lambda n : n % 2 != 0, lista))
print("Impares:",impares)

print("Utilizando la función sum() -- Suma:",sum(impares))
print("Utilizando la función reduce() -- Suma:",reduce(lambda x, y: x +y, impares))