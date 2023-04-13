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

