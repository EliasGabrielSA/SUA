from django.contrib import admin
from .models import Paciente, Aluno, Servidor, Visitante

# Register your models here.

admin.site.register([Paciente, Aluno, Servidor, Visitante])
