from django.db import models
from .classe_viagem import ClasseViagem

class Passagem(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField()
    tipo_classes_voo = models.CharField(max_length=4,choices=ClasseViagem.choices, default=0)
