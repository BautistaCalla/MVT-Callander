from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre = models. CharField(max_length=30)  # Texto
    apellido = models.CharField(max_length=30)  # Texto
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    class Meta:
       verbose_name_plural = "Familiares"

    def __str__(self) -> str: #MOdificar como se visualiza  
      return f'{self.nombre} {self.apellido}'