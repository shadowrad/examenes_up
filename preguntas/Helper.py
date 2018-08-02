import random

from preguntas.models import Pregunta


def examen_preguntas_ids(cantidad, materia_id):
    if materia_id is None:
        data_ids = list(Pregunta.objects.values_list('id', flat=True))
    else:
        data_ids = list(Pregunta.objects.filter(materia__id=materia_id).values_list('id',flat=True))

    cantidad_datos = len(data_ids)
    randoms = []
    index =0
    while index < (len(data_ids)-index):
        pos= random.randint(index, (len(data_ids)-1)-index)
        data_ids[index], data_ids[pos] = data_ids[pos], data_ids[index]
        index = index +1
    rango = range(0, cantidad)
    if cantidad == 0 or cantidad > cantidad_datos:
        rango= range(0, cantidad_datos)

    for i in rango:
        randoms.append(data_ids[i])

    return randoms
