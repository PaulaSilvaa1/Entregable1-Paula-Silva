from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render
from App_Ps.models import Curso,Entregable,Profesor
from App_Ps.forms import CursoFormulario, ProfesorFormulario
from django.http import HttpResponse



def inicio (request):
      return render(request, 'App_Ps/inicio.html')

def estudiantes(request):
      return render(request, 'App_Ps/estudiantes.html')

def profesores(request):
      return render(request, 'App_Ps/profesores.html')

def cursos(request):

 
      return render(request, 'App_Ps/cursos.html')

def entregables(request):
   
      return render(request, 'App_Ps/entregables.html')


def formulario1(request):

      if request.method=='POST':
            formulario1=CursoFormulario(request.POST)
            info= formulario1.cleaned_data
            Curso1 =Curso(nombre=info['curso'], camada=info['camada'])
            Curso1.save()
            return render(request,'App_Ps/formu1.html')
      
      else:
            formulario1=CursoFormulario()

      return render(request,'App_Ps/formu1.html',{'formu1':formulario1})

def formulario2(request):
      if request.method=='POST':
            formulario3=ProfesorFormulario(request.POST)
            info= formulario2.cleaned_data
            Profe =Profesor(nombre=info['nombre'],apellido=info['apellido'], email=info['email'], profesion=info['profesion'])
            Profe.save()
            return render(request,'App_Ps/formu2.html')
      else:
            formulario2=ProfesorFormulario()
      return render(request,'App_Ps/formu2.html',{'formu2':formulario2})

def busquedaCursos(request):
      return render (request, 'App_Ps/formu1.html')

def buscar(request):
      if request.method=='GET':

            camada= request.GET['camada']
            
            cursos=Curso.objects.filter(camada=camada)
           

            return render(request, "App_Ps/buscar.html",{'cursos':cursos,'camada':camada})
            

      else:
            mensaje= 'No enviaste datos.'

            
      return HttpResponse(mensaje)