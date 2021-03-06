from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from examenes_up import settings


Niveles = (
        ('FACIL', 'Facil'),
        ('INTERMEDIO', 'Intermedio'),
        ('DIFICIL', 'Dificil'),
    )
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
    nivel = models.CharField(max_length=20, choices=Niveles)
    Descripcion= RichTextField(verbose_name='Pregunta')
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
    posibilidad = models.IntegerField(default=settings.MAX)
    tags = models.ManyToManyField(Tag, blank=True)


    def __str__(self):
        return mark_safe(self.Descripcion)

    def descripcion(self):
        return mark_safe(self.Descripcion)

    class Meta:
        ordering = ['Descripcion']
        unique_together = ['Descripcion']



