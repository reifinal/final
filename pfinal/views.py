from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Curso
from .forms import EstudianteForm, CursoForm

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all().order_by('apellido')
    return render(request, 'pfinal/lista_estudiantes.html', {'estudiantes':estudiantes})

def detalle_estudiante(request, pk):
    estudiantes = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'pfinal/detalle_estudiante.html', {'estudiantes': estudiantes})
    
def nuevo_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pfinal.views.lista_estudiantes')#, pk=post.pk)
    else:
        form = EstudianteForm()
    return render(request, 'pfinal/editar_estudiante.html', {'form': form})

def editar_estudiante(request, pk):
    estudiantes = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = EstudianteForm(request.POST, instance=estudiantes)
        if form.is_valid():
            estudiantes.save()
            return redirect('pfinal.views.lista_estudiantes')#, pk=post.pk)
    else:
        form = EstudianteForm(instance=estudiantes)
    return render(request, 'pfinal/editar_estudiante.html', {'form': form})

def lista_cursos(request):
    cursos = Curso.objects.all().order_by('nombre')
    return render(request, 'pfinal/lista_cursos.html', {'cursos':cursos})

def detalle_curso(request, pk):
    cursos = get_object_or_404(Curso, pk=pk)
    return render(request, 'pfinal/detalle_curso.html', {'cursos': cursos})

def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pfinal.views.lista_cursos')#, pk=post.pk)
    else:
        form = CursoForm()
    return render(request, 'pfinal/editar_curso.html', {'form': form})

def editar_curso(request, pk):
    cursos = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=cursos)
        if form.is_valid():
            cursos.save()
            return redirect('pfinal.views.lista_cursos')#, pk=post.pk)
    else:
        form = CursoForm(instance=cursos)
    return render(request, 'pfinal/editar_curso.html', {'form': form})

#
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
## Create your views here.
#
#def authentication(request):
#    if request.method == 'POST':
#        action = request.POST.get('action',None)
#        
