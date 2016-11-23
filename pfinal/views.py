from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Estudiante, Curso, Matricula
from .forms import EstudianteForm, CursoForm, MatriculaForm
from django.http.response import HttpResponseRedirect

def lista_estudiantes(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        estudiantes = Estudiante.objects.all().order_by('apellido')
        return render(request, 'pfinal/lista_estudiantes.html', {'estudiantes':estudiantes, 'user':request.user})

def detalle_estudiante(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        estudiantes = get_object_or_404(Estudiante, pk=pk)
        return render(request, 'pfinal/detalle_estudiante.html', {'estudiantes': estudiantes, 'user':request.user})
    
def nuevo_estudiante(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        if request.method == "POST":
            form = EstudianteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pfinal.views.lista_estudiantes')#, pk=post.pk)
        else:
            form = EstudianteForm()
        return render(request, 'pfinal/editar_estudiante.html', {'form': form, 'user':request.user})

def editar_estudiante(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        estudiantes = get_object_or_404(Estudiante, pk=pk)
        if request.method == "POST":
            form = EstudianteForm(request.POST, instance=estudiantes)
            if form.is_valid():
                estudiantes.save()
                return redirect('pfinal.views.lista_estudiantes')#, pk=post.pk)
        else:
            form = EstudianteForm(instance=estudiantes)
        return render(request, 'pfinal/editar_estudiante.html', {'form': form, 'user':request.user})

def lista_cursos(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        cursos = Curso.objects.all().order_by('nombre')
        return render(request, 'pfinal/lista_cursos.html', {'cursos':cursos, 'user':request.user})

def detalle_curso(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        cursos = get_object_or_404(Curso, pk=pk)
        return render(request, 'pfinal/detalle_curso.html', {'cursos': cursos, 'user':request.user})

def nuevo_curso(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        if request.method == "POST":
            form = CursoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('pfinal.views.lista_cursos')#, pk=post.pk)
        else:
            form = CursoForm()
        return render(request, 'pfinal/editar_curso.html', {'form': form, 'user':request.user})

def editar_curso(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        cursos = get_object_or_404(Curso, pk=pk)
        if request.method == "POST":
            form = CursoForm(request.POST, instance=cursos)
            if form.is_valid():
                cursos.save()
                return redirect('pfinal.views.lista_cursos')#, pk=post.pk)
        else:
            form = CursoForm(instance=cursos)
        return render(request, 'pfinal/editar_curso.html', {'form': form, 'user':request.user})

#Vista para insertar tabla relacionada
def nuevo_matricula(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        if request.method == "POST":
            form = MatriculaForm(request.POST)
            if form.is_valid():
                cursos = request.POST.get('curso')
                for estudiantes in request.POST.getlist('estudiante'):
                    matriculas = Matricula(estudiante_id = estudiantes, curso_id = cursos)
                    matriculas.save()
                    return redirect('pfinal.views.lista_estudiantes')
        else:
            form = MatriculaForm()
        return render(request, 'pfinal/nuevo_matricula.html', {'form': form, 'user':request.user})

def borrar_curso(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        cursos = Curso.objects.filter(pk=pk)
        cursos.delete()
        return HttpResponseRedirect('/curso/')

def authentication(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.method == 'POST':
            username=request.POST.get('username',None)
            password=request.POST.get('password',None)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/login")
        return render(request,'pfinal/login.html',{})
        