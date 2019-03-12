from django.db import models

# Create your models here.
from examenes_up import settings


class Tag(models.Model):
    Descripcion = models.CharField(verbose_name='Tag', max_length=100)

    def __str__(self):
        return self.Descripcion

    class Meta:
        ordering = ['Descripcion']
        unique_together = ['Descripcion']

class Materia(models.Model):
    Descripcion= models.TextField(verbose_name='Materia')

    def __str__(self):
        return self.Descripcion
    class Meta:
        ordering = ['Descripcion']
        unique_together = ['Descripcion']



class Pregunta(models.Model):
    Descripcion= models.TextField(verbose_name='Pregunta')
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
    posibilidad = models.IntegerField(default=settings.MAX)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.Descripcion
    class Meta:
        ordering = ['Descripcion']
        unique_together = ['Descripcion']

