from django.shortcuts import render, get_object_or_404
from .models import Estudiante

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all().order_by('apellido')
    return render(request, 'pfinal/lista_estudiantes.html', {'estudiantes':estudiantes})

def detalle_estudiante(request, pk):
        estudiantes = get_object_or_404(Estudiante, pk=pk)
        return render(request, 'pfinal/detalle_estudiante.html', {'estudiantes': estudiantes})
#
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
## Create your views here.
#
#def authentication(request):
#    if request.method == 'POST':
#        action = request.POST.get('action',None)
#        
