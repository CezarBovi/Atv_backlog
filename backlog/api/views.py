from rest_framework import viewsets, generics, filters
from .models import Estudante, Curso, Matricula
from .serializers import (
    EstudanteSerializer, 
    CursoSerializer, 
    MatriculaSerializer,
    MatriculaDetalhadaSerializer
)


class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'cpf']
    ordering_fields = ['nome', 'id']


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['descricao', 'codigo']
    ordering_fields = ['codigo', 'descricao']


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasPorEstudante(generics.ListAPIView):
    serializer_class = MatriculaDetalhadaSerializer

    def get_queryset(self):
        estudante_id = self.kwargs['estudante_id']
        return Matricula.objects.filter(estudante_id=estudante_id)


class MatriculasPorCurso(generics.ListAPIView):
    serializer_class = MatriculaDetalhadaSerializer

    def get_queryset(self):
        curso_id = self.kwargs['curso_id']
        return Matricula.objects.filter(curso_id=curso_id)