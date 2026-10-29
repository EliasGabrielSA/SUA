from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from pacientes.models import Paciente

from .forms import AtendimentoForm

# Create your views here.

def atendimento_novo(request, paciente_pk):
    paciente = get_object_or_404(Paciente, pk=paciente_pk)

    if request.method == "POST":
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            atendimento = form.save(commit=False)
            atendimento.paciente = paciente
            atendimento.save()
            messages.success(request, "Atendimento registrado.")
            return redirect("pacientes:detalhe", pk=paciente.pk)
    else:
        form = AtendimentoForm()

    return render(request, "atendimentos/atendimento_form.html", {
        "form": form,
        "paciente": paciente,
    })
