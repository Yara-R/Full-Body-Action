from django.db import models

class Cadastro(models.Model):
    nome = models.TextField()
    email = models.TextField()
    senha = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    idade = models.IntegerField()

class Avaliacao(models.Model):
    estrelas = models.IntegerField(default=0, blank=True, null=True)
    
class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    # data = models.DateTimeField(auto_now_add=True)


class Medidas(models.Model):
    peito = models.DecimalField(max_digits=5, decimal_places=2)
    costas = models.DecimalField(max_digits=5, decimal_places=2)
    ombro = models.DecimalField(max_digits=5, decimal_places=2)
    pescoco = models.DecimalField(max_digits=5, decimal_places=2)
    braco = models.DecimalField(max_digits=5, decimal_places=2)
    antebraco = models.DecimalField(max_digits=5, decimal_places=2)
    quadril = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    coxa = models.DecimalField(max_digits=5, decimal_places=2)
    panturrilha = models.DecimalField(max_digits=5, decimal_places=2)

class Agua(models.Model):
    data = models.DecimalField(max_digits=8, decimal_places=2)
    hora = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)