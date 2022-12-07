from django.db import models

# Create your models here.
 
class Familiar(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    nacimiento=models.DateField()

class FamiliarMayor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    nacimiento=models.DateField()
    profesion=models.CharField(max_length=50)