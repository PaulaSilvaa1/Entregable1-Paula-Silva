from django.urls import path
from App_Ps.views import *




urlpatterns = [
   
    path('', inicio, name="Inicio"),
    path('cursos/', cursos ),
    path('profesores/', profesores, name="Profesores"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('entregables/', entregables, name="Entregables"),
    path('formu1/',formulario1,name="Cursos"),
    path('formu2/',formulario2,name= "Registrarse"),
    path('buscarCursos/',busquedaCursos),
    path('buscar/',buscar),
]

