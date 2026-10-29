from django import forms

from pacientes.forms import BootstrapMixin

from .models import Atendimento


class AtendimentoForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ["data_hora", "observacao"]
        labels = {"data_hora": "Data / horário", "observacao": "Anotações"}
        widgets = {
            "data_hora": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "observacao": forms.Textarea(attrs={"rows": 6}),
        }
