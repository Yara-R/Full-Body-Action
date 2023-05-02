from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(default='email@default.com')
    password = models.CharField(max_length=25, default='12345678')

class Registro_Agua(models.Model):
    data = models.DateField()
    hora = models.DateTimeField()
    quantidade_ml = models.IntegerField()

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
    


