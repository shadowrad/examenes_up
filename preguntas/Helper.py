import random

import math

from preguntas.models import Pregunta


def examen_preguntas_ids(cantidad, materia_id):
    if materia_id is None:
        data_ids = list(Pregunta.objects.values_list('id', flat=True))
    else:
        data_ids = list(Pregunta.objects.filter(materia__id=materia_id).values_list('id', flat=True))

    cantidad_datos = len(data_ids)
    randoms = []
    index = 0
    while index < (len(data_ids) - index):
        pos = random.randint(index, (len(data_ids) - 1) - index)
        data_ids[index], data_ids[pos] = data_ids[pos], data_ids[index]
        index = index + 1
    rango = range(0, cantidad)
    if cantidad == 0 or cantidad > cantidad_datos:
        rango = range(0, cantidad_datos)

    for i in rango:
        randoms.append(data_ids[i])

    return randoms


def trabajar_preguntas(elegidas):
    preguntas = Pregunta.objects.filter(id__in=elegidas)
    for pregunta in preguntas:
        pregunta.posibilidad -= 2
        pregunta.save()

    return preguntas


def mezclar_todo(lista_ids):
    for i in range(len(lista_ids)):
        pos = random.randint(i, (len(lista_ids) - 1))
        temp = lista_ids[i]
        lista_ids[i] = lista_ids[pos]
        lista_ids[pos] = temp


def setear_frecuencia(cantidad, data_ids):
    total = 0
    for dato in data_ids:
        dato['fr-desde'] = total + 1
        total += dato['posibilidad']
        dato['fr-hasta'] = total

    ids_a_buscar = []

    rango_busqueda = math.floor(total / cantidad)
    rango_cantidad = math.floor(len(data_ids) / cantidad)

    desde_ids = 0
    hasta = 1
    for i in range(0, cantidad):
        desde = hasta
        hasta = desde + rango_busqueda
        nro_random = random.randrange(desde, hasta)
        for dato in data_ids[desde_ids:]:
            if dato['fr-desde'] <= nro_random <= dato['fr-hasta']:
                ids_a_buscar.append(dato['id'])
                break

        desde_ids += rango_cantidad
    return ids_a_buscar


def examen_preguntas_ids_frecuencia(cantidad, materia_id):
    if materia_id is None:
        data_ids = Pregunta.objects.values('id', 'posibilidad')
    else:
        data_ids = Pregunta.objects.filter(materia__id=materia_id).values('id', 'posibilidad')
    data_ids = list(data_ids.order_by('id'))
    mezclar_todo(data_ids)
    ids_a_buscar = setear_frecuencia(cantidad, data_ids)
    return trabajar_preguntas(ids_a_buscar)
