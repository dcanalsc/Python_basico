#Enunciado del ejercicio:

#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open('archivo.txt','w')
print("Escribe un texto, cuando hayas terminado, deja en blanco la linea")
valor = None
while valor != "":
    cadena = input()
    if cadena == "":
        valor = cadena
        continue
    f.writelines(cadena)
    f.write("\n")

f.close()

