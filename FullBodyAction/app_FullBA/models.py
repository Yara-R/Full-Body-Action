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