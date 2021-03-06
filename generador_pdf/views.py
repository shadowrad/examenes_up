from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from preguntas.Helper import examen_preguntas_ids
from preguntas.models import Pregunta, Materia

@login_required
def parcial_ean(request):
    materia = None
    materias = []
    preguntas = []
    if request.method == "POST":
        materia_id = request.POST.get('materia_id')
        materia = Materia.objects.get(pk=materia_id)
        randoms_id = examen_preguntas_ids(5, materia_id)
        preguntas = Pregunta.objects.filter(id__in=randoms_id)
    else:
        materias = Materia.objects.all()

    return render(request,'parcial_ean.html', {'preguntas':preguntas,'materias':materias, 'materia': materia})


def parcial_up(request):
    materia = None
    materias = []
    preguntas = []
    cantidad = 5
    if request.method == "POST":
        materia_id = request.POST.get('materia_id')
        cantidad = request.POST.get('cantidad')
        materia = Materia.objects.get(pk=materia_id)
        randoms_id = examen_preguntas_ids(int(cantidad), materia_id)
        preguntas = Pregunta.objects.filter(id__in=randoms_id)
    else:
        materias = Materia.objects.all()
    datos = {'preguntas': preguntas,
             'materias': materias,
             'materia': materia,
             'cantidad':cantidad}
    return render(request,'parcial_up.html', datos)