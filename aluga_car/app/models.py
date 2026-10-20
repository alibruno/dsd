from django.db import models
from django.contrib.auth.models import User # Usando o usuário padrão do Django para simplificar

class Carro(models.Model):
    class Status(models.TextChoices):
        DISPONIVEL = "Disponível", "Disponível"
        ALUGADO = "Alugado", "Alugado"
        EM_MANUTENCAO = "Em manutenção", "Em Manutenção"
        INDISPONIVEL = "Indisponível", "Indisponível"

    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50) # Adicionei o modelo que faltava
    ano = models.SmallIntegerField()
    placa = models.CharField(max_length=10, unique=True)
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.DISPONIVEL
    )
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

class Locacao(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.PROTECT) # PROTECT evita apagar carro com histórico
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Locação de {self.carro} por {self.cliente.username}"