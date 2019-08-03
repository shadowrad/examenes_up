from rest_framework import serializers

from preguntas.models import Pregunta


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'
        depth = 2
