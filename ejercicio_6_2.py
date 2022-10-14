#Enunciado del ejercicio:

#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga
# como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = None
    nota = None
    def __init__(self, nombre, nota):
        self.nota = nota
        self.nombre = nombre
    def imprimir (self):
        print(self.nombre,"tiene un:",self.nota,end=" ")
        if self.nota >= 5:
            print("(APROBADO)")
        else: print("(SUSPENDIDO)")


print("Nombre del alumno:")
nombre =input()
print("Nota:")
nota = input()
alumno = Alumno(nombre,int(nota))
alumno.imprimir()

