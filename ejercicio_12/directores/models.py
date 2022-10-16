from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_defuncion = models.DateField(null= True, blank = True)
    biografia = models.TextField()

    def __str__(self):
        return self.nombre + " " + self.apellidos

class Pelicula(models.Model):
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=25)
    sinopsis = models.TextField()
    lenght = models.PositiveIntegerField()
    imagen = models.URLField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
