from datetime import datetime
from django.contrib import admin

# Register your models here.
import random

from django.contrib import admin

# Register your models here.
from django.contrib.admin import ListFilter

import preguntas
from examenes_up import settings
from preguntas.Helper import examen_preguntas_ids, examen_preguntas_ids_frecuencia
from preguntas.models import Pregunta, Materia, Tag
from django.contrib.admin import SimpleListFilter

def set_dificultad(dificultad, queryset):
        rows_updated = queryset.update(nivel=dificultad)
        message = "%s preguntas modificadas" % rows_updated
        return message
class ResetFilter(SimpleListFilter):
    title = 'para resetear frecuencias'
    parameter_name = 'frecuencias'

    def lookups(self, request, model_admin):
        return [(1, 'reset')]

    def queryset(self, request, queryset):
        if self.value() is not None:
            for p in Pregunta.objects.all():
                p.posibilidad = settings.MAX
                p.save()

            return queryset


class Cantidad_filter(SimpleListFilter):
    title = 'Cantidad de preguntas'
    parameter_name = 'Cantidad Preguntas'

    def lookups(self, request, model_admin):
        numeros = []
        for i in range(5, 55, 5):
            numeros.append((i, i))
        return numeros

    def queryset(self, request, queryset):
        if self.value() is not None:
            randoms_id = examen_preguntas_ids(int(self.value()), request.GET.get('materia__id__exact'))
            return queryset.filter(id__in=randoms_id)


class PreguntaExamen(Pregunta):
    class Meta:
        proxy = True
        verbose_name_plural = u"Examen"


class ExamenAdmin(admin.ModelAdmin):
    line_numbering = 0

    model = PreguntaExamen

    def line_number(self, obj):
        self.line_numbering += 1
        return self.line_numbering

    line_number.short_description = '#'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    actions = None
    list_display_links = None
    list_display = ['line_number', 'descripcion']
    list_filter = ('materia', 'tags', 'nivel', Cantidad_filter, ResetFilter)


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'materia','nivel']
    list_filter = ('materia',)

    def marcar_dificil(self, request, queryset):
        mensaje = set_dificultad('DIFICIL', queryset)
        self.message_user(request, mensaje)

    def marcar_intemedio(self, request, queryset):
        mensaje = set_dificultad('INTERMEDIO', queryset)
        self.message_user(request, mensaje)

    def marcar_facil(self, request, queryset):
        mensaje = set_dificultad('FACIL', queryset)
        self.message_user(request, mensaje)

    actions = ['marcar_dificil','marcar_intemedio::','marcar_facil']

    def cant_seleccionada(self, obj):
        return int( (settings.MAX - obj.posibilidad)/settings.RANGO)


class PreguntasInline(admin.TabularInline):

    model = Pregunta




class MateriaAdmin(admin.ModelAdmin):
    inlines = [
        PreguntasInline,
    ]


admin.site.register(PreguntaExamen, ExamenAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Tag)
