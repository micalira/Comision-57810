from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.BigIntegerField()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)    
    
class Entregrable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.DateField()
    