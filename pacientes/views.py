import re

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.db import transaction

from .forms import AlunoForm, PacienteForm, ServidorForm, VisitanteForm
from .models import Paciente

# Create your views here.

VINCULOS = {
    "aluno": AlunoForm,
    "servidor": ServidorForm,
    "visitante": VisitanteForm,
}


def paciente_novo(request):
    vinculo = request.POST.get("vinculo", "")
    erro_vinculo = None

    if request.method == "POST":
        form = PacienteForm(request.POST)
        # só o form do vínculo escolhido recebe os dados do POST
        forms_vinculo = {
            nome: cls(request.POST if nome == vinculo else None, prefix=nome)
            for nome, cls in VINCULOS.items()
        }

        if vinculo not in VINCULOS:
            erro_vinculo = "Escolha o vínculo do paciente."
            form.is_valid()  # para mostrar também os erros do paciente
        elif form.is_valid() & forms_vinculo[vinculo].is_valid():
            with transaction.atomic():
                paciente = form.save()
                dados_vinculo = forms_vinculo[vinculo].save(commit=False)
                dados_vinculo.paciente = paciente
                dados_vinculo.save()
            messages.success(request, "Paciente cadastrado com sucesso.")
            return redirect("pacientes:detalhe", pk=paciente.pk)
    else:
        form = PacienteForm()
        forms_vinculo = {nome: cls(prefix=nome) for nome, cls in VINCULOS.items()}

    return render(request, "pacientes/paciente_form.html", {
        "form": form,
        "forms_vinculo": forms_vinculo,
        "vinculo": vinculo,
        "erro_vinculo": erro_vinculo,
    })

def paciente_detalhe(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    atendimentos = paciente.atendimentos.all()
    return render(
        request,
        "pacientes/paciente_detalhe.html",
        {"paciente": paciente, "atendimentos": atendimentos},
    )

def paciente_lista(request):
    busca = request.GET.get("q", "").strip()
    pacientes = Paciente.objects.select_related("aluno", "servidor", "visitante").order_by("nome")

    if busca:
        filtro = Q(nome__icontains=busca)
        digitos = re.sub(r"\D", "", busca)
        if digitos:
            filtro |= Q(cpf__contains=digitos)
        pacientes = pacientes.filter(filtro)

    return render(request, "pacientes/paciente_lista.html", {
        "pacientes": pacientes,
        "busca": busca,
    })
