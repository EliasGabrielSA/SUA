from django.urls import path
from . import views

app_name = "pacientes"

urlpatterns = [
    path("", views.paciente_lista, name="lista"),
    path("novo/", views.paciente_novo, name="novo"),
    path("<int:pk>/", views.paciente_detalhe, name="detalhe"),
]
