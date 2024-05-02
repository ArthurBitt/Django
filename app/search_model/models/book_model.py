from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):

    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

    # autores = models.CharField(max_length=255, default="Unknown")
    # publicado = models.DateField(default=datetime.now)
    # isbn = models.CharField(max_length=13, unique=True)  # ISBN como identificador único
    # capa = models.ImageField(upload_to='search_model/covers/%Y/%m/%d/', default='')  # URL para a capa do livro
    # descricao = models.TextField(null=True, blank=True)
    # categoria = models.CharField(max_length=60)
    # alugado = models.BooleanField(default=False)
    #
    #
    # def media_avaliacao(self):
    #     avaliacoes = Avaliacao.objects.filter(livro=self)
    #
    # def __str__(self):
    #     return self.titulo

# class Avaliacao(models.Model):
#     livro = models.ForeignKey(Livro, on_delete=models.CASCADE,  related_name='avaliacoes')
#     usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
#     avaliacao = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])