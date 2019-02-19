from datetime import datetime
from django.contrib import admin

# Register your models here.
import random

from django.contrib import admin

# Register your models here.
from django.contrib.admin import ListFilter

import preguntas
from preguntas.Helper import examen_preguntas_ids, examen_preguntas_ids_frecuencia
from preguntas.models import Pregunta, Materia
from django.contrib.admin import SimpleListFilter

class ResetFilter(SimpleListFilter):
    title = 'para resetear frecuencias'
    parameter_name = 'frecuencias'

    def lookups(self, request, model_admin):
        return [(1, 'reset')]

    def queryset(self, request, queryset):
        if self.value() is not None:
            for p in Pregunta.objects.all():
                p.posibilidad = 20
                p.save()

            return queryset



class Cantidad_filter(SimpleListFilter):
    title = 'Cantidad de preguntas'
    parameter_name = 'Cantidad Preguntas'

    def lookups(self, request, model_admin):
        numeros=[]
        for i in range(5,55,5):
            numeros.append((i,i))
        return numeros

    def queryset(self, request, queryset):
        if self.value() is not None:
            randoms_id = examen_preguntas_ids_frecuencia(int(self.value()),request.GET.get('materia__id__exact'))
            return queryset.filter(id__in=randoms_id)





class PreguntaExamen(Pregunta):
    class Meta:
        proxy = True
        verbose_name_plural = u"Examen"


class ExamenAdmin(admin.ModelAdmin):
    list_display = ['posibilidad', 'Descripcion']
    model= PreguntaExamen
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    actions = None
    list_display_links=None

    list_filter=('materia',Cantidad_filter,ResetFilter)

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['Descripcion','materia']
    list_filter = ('materia',)

admin.site.register(PreguntaExamen,ExamenAdmin)
admin.site.register(Pregunta,PreguntaAdmin)
admin.site.register(Materia)
