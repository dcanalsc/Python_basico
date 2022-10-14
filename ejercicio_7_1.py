import calculadora as c

#   Enunciado del ejercicio:
#   En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora:
#   sumar, restar, multiplicar y dividir.
#   Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
#   Los resultados tenéis que mostrarlos por consola.

print("Introduce dos números:")
a = int(input())
b = int(input())

print("Suma", c.sumar(a,b))
print("Resta", c.restar(a,b))
print("Multiplicación", c.multiplicar(a,b))
print("División", c.dividir(a,b))


