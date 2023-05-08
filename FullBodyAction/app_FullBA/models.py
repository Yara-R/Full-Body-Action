from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
class Registro_Agua(models.Model):
    data = models.DateField()
    hora = models.DateTimeField()
    quantidade_ml = models.IntegerField()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

class medidas(models.Model):
    peito = models.DecimalField(max_digits = 3, decimal_places = 2)
    costas = models.DecimalField(max_digits = 3, decimal_places = 2)
    ombro = models.DecimalField(max_digits = 3, decimal_places = 2)
    pescoco = models.DecimalField(max_digits = 3, decimal_places = 2)
    braco = models.DecimalField(max_digits = 3, decimal_places = 2)
    antebraco = models.DecimalField(max_digits = 3, decimal_places = 2)
    quadril = models.DecimalField(max_digits = 3, decimal_places = 2)
    cintura = models.DecimalField(max_digits = 3, decimal_places = 2)
    coxa = models.DecimalField(max_digits = 3, decimal_places = 2)
    panturrilha = models.DecimalField(max_digits = 3, decimal_places = 2)
    