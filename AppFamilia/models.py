from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Familia (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField ()
    fechaNacimiento = models.DateField ()
    email= models.EmailField()

class Amigos (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField ()

class Asistencia (models.Model):
    estado =(models.CharField(max_length=30))    


    

