from django.db import models

# Create your models here.

class Paciente(models.Model):
    class Genero(models.TextChoices):
        FEMININO = "F", "Feminino"
        MASCULINO = "M", "Masculino"

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=1, choices=Genero.choices, blank=True)
    email = models.EmailField(blank=True)
    celular = models.CharField(max_length=20, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="aluno",
    )
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.paciente} (aluno)"


class Servidor(models.Model):
    class EstadoCivil(models.TextChoices):
        SOLTEIRO = "SOL", "Solteiro"
        CASADO = "CAS", "Casado"
        VIUVO = "VIU", "Viúvo"
        DIVORCIADO = "DIV", "Divorciado"
        OUTROS = "OUT", "Outros"

    class Escolaridade(models.TextChoices):
        FUNDAMENTAL = "FUN", "Ensino fundamental"
        MEDIO = "MED", "Ensino médio completo"
        SUPERIOR_INCOMPLETO = "SUI", "Ensino superior incompleto"
        SUPERIOR_COMPLETO = "SUC", "Ensino superior completo"

    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="servidor",
    )
    siape = models.CharField(max_length=20, unique=True)
    campus_lotacao = models.CharField(max_length=100, blank=True)
    cargo = models.CharField(max_length=100, blank=True)
    ativo = models.BooleanField(default=True)

    mae = models.CharField(max_length=150, blank=True)
    pai = models.CharField(max_length=150, blank=True)
    estado_civil = models.CharField(max_length=3, choices=EstadoCivil.choices, blank=True)
    escolaridade = models.CharField(max_length=3, choices=Escolaridade.choices, blank=True)
    curso = models.CharField(max_length=100, blank=True)

    endereco = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)

    tem_plano_saude = models.BooleanField(default=False)
    plano_saude = models.CharField(max_length=100, blank=True)  # "Qual?"

    def __str__(self):
        return f"{self.paciente} (servidor)"


class Visitante(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="visitante",
    )
    observacao = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.paciente} (visitante)"
