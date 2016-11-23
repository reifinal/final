from django.shortcuts import render

def lista_estudiantes(request):
    return render(request, 'pfinal/lista_estudiantes.html', {})
#
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login
## Create your views here.
#
#def authentication(request):
#    if request.method == 'POST':
#        action = request.POST.get('action',None)
#        
