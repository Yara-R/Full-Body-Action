from django.urls import path
from app_cadastro import views

urlpatterns = [
    #fullbodyaction.com/cadastro/
    path('cadastro/', views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
