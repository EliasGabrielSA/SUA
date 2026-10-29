from django.urls import path

from . import views

app_name = "atendimentos"

urlpatterns = [
    path("novo/<int:paciente_pk>/", views.atendimento_novo, name="novo"),
]
