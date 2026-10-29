from django.db import models
from django.utils import timezone

# Create your models here.

class Atendimento(models.Model):
    paciente = models.ForeignKey(
        "pacientes.Paciente",
        on_delete=models.PROTECT,
        related_name="atendimentos",
    )
    data_hora = models.DateTimeField(default=timezone.now)
    observacao = models.TextField()

    class Meta:
        ordering = ["-data_hora"]

    def __str__(self):
        return f"{self.paciente} em {self.data_hora:%d/%m/%Y %H:%M}"
