from django import forms
from .models import Estudiante, Curso, Matricula

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'apellido', 'telefono',)
        
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nombre', 'descripcion',)

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ('curso', 'estudiante',)
        
#    def __init__ (self, *args, **kwargs):
#        super(MatriculaForm, self).__init__(*args, **kwargs)
#        self.fields["estudiante"].widget = forms.widgets.CheckboxSelectMultiple()
#        self.fields["estudiante"].help_text = "Seleccione los alumnos para el curso"
#        self.fields["estudiante"].queryset = Estudiante.objects.all()