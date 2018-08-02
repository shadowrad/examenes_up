from django.contrib import admin

# Register your models here.
import random

from django.contrib import admin

# Register your models here.
from django.contrib.admin import ListFilter

import preguntas
from preguntas.Helper import examen_preguntas_ids
from preguntas.models import Pregunta, Materia
from django.contrib.admin import SimpleListFilter

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
            randoms_id = examen_preguntas_ids(int(self.value()),request.GET.get('materia__id__exact'))
            return queryset.filter(id__in=randoms_id)





class PreguntaExamen(Pregunta):
    class Meta:
        proxy = True
        verbose_name_plural = u"Examen"


class ExamenAdmin(admin.ModelAdmin):
    model= PreguntaExamen
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    actions = None
    list_display_links=None

    list_filter=('materia',Cantidad_filter)

admin.site.register(PreguntaExamen,ExamenAdmin)
admin.site.register(Pregunta)
admin.site.register(Materia)
