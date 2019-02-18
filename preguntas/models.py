from django.db import models

# Create your models here.


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
    posibilidad = models.IntegerField(default=20)

    def __str__(self):
        return self.Descripcion
    class Meta:
        ordering = ['Descripcion']
        unique_together = ['Descripcion']

