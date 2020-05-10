from django.shortcuts import render

# Create your views here.
from preguntas.Helper import examen_preguntas_ids
from preguntas.models import Pregunta, Materia


def parcial_ean(request):
    materias = Materia.objects.all()
    materia_id = 3
    randoms_id = examen_preguntas_ids(5, 3)
    preguntas = Pregunta.objects.filter(id__in=randoms_id)

    return render(request,'parcial_otro.html', {'preguntas':preguntas,'materias':materias})