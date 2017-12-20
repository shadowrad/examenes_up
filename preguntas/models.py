from django.db import models

# Create your models here.



class Pregunta(models.Model):
    Descripcion= models.TextField(verbose_name='Pregunta')

    def __str__(self):
        return self.Descripcion
    class Meta:
        ordering = ['Descripcion']
        unique_together = ['Descripcion']
