import re

from django import forms

from .models import Aluno, Paciente, Servidor, Visitante


class BootstrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            widget = campo.widget
            if isinstance(widget, forms.CheckboxInput):
                classe = "form-check-input"
            elif isinstance(widget, forms.Select):
                classe = "form-select"
            else:
                classe = "form-control"
            widget.attrs["class"] = classe


class PacienteForm(BootstrapMixin, forms.ModelForm):
    cpf = forms.CharField(max_length=14, required=False, empty_value=None, label="CPF")

    class Meta:
        model = Paciente
        fields = ["nome", "cpf", "data_nascimento", "genero", "email", "celular"]
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if not cpf:
            return None
        digitos = re.sub(r"\D", "", cpf)
        if len(digitos) != 11:
            raise forms.ValidationError("O CPF deve ter 11 dígitos.")
        return digitos


class AlunoForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ["paciente"]


class ServidorForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Servidor
        exclude = ["paciente"]


class VisitanteForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Visitante
        exclude = ["paciente"]
