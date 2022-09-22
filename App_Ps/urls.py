from django.urls import path
from App_Ps.views import *




urlpatterns = [
   
    path('', inicio, name="Inicio"),
    path('cursos/', cursos, name="Cursos"),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('formu1/',formulario1),
    path('formu2/',formulario2),
    path('buscarCursos/',busquedaCursos),
    path('buscar/',buscar),
]

