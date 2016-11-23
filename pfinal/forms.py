from django import forms
from .models import Estudiante, Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'apellido', 'telefono',)
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion',)