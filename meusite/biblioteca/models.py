from django.db import models
from django.utils import timezone

class Prateleira(models.Model):
    nomeGenero = models.CharField(max_length=30)

    def __str__(self):
        return self.nomeGenero


class Livro(models.Model):
    prateleira = models.ForeignKey(Prateleira)
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=30)
    editora = models.CharField(max_length=30)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo
