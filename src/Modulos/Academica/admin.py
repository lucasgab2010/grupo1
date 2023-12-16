from django.contrib import admin
from Modulos.Academica.models import (
    Carrera, Estudiante, Curso, Matricula
)

# Register your models here.

admin.site.register(
    Carrera,
    Estudiante,
    Curso,
    Matricula,   
)