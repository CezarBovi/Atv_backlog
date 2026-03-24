from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('estudantes', views.EstudanteViewSet)
router.register('cursos', views.CursoViewSet)
router.register('matriculas', views.MatriculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('estudantes/<int:estudante_id>/matriculas/', views.MatriculasPorEstudante.as_view()),
    path('cursos/<int:curso_id>/matriculas/', views.MatriculasPorCurso.as_view()),
]