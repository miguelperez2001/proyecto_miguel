from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    fecha_lanzamiento=models.DateField()
    id_ocio=models.IntegerField()

    class Meta:
        db_table='videojuego'

class Cocina(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    pais_origen=models.CharField(max_length=50)
    id_ocio=models.IntegerField()

    class Meta:
        db_table='cocina'

class Serie(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    fecha_lanzamiento=models.DateField()
    id_ocio=models.IntegerField()

    class Meta:
        db_table='serie'

class Ocio(models.Model):
    nombre=models.CharField(max_length=50)

    class Meta:
        db_table='ocio'