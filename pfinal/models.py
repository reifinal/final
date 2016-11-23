from django.db import models
from django.contrib import admin


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre +" "+self.apellido

class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    estudiantes = models.ManyToManyField(Estudiante, through='Matricula')
    def __str__(self):
        return self.nombre

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
class MatriculaInLine(admin.TabularInline):
    model = Matricula
    extra = 1

class EstudianteAdmin(admin.ModelAdmin):
    inlines = (MatriculaInLine,)

class CursoAdmin (admin.ModelAdmin):
    inlines = (MatriculaInLine,)