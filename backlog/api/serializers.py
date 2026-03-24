from rest_framework import serializers
from .models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

    def validate_cpf(self, value):
        if len(value) != 11:
            raise serializers.ValidationError('CPF deve ter 11 dígitos.')
        return value


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class MatriculaDetalhadaSerializer(serializers.ModelSerializer):
    estudante = EstudanteSerializer(read_only=True)
    curso = CursoSerializer(read_only=True)

    class Meta:
        model = Matricula
        fields = '__all__'