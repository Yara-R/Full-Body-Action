from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('cadastro/',views.cadastro, name='cadastro'),
    path('usuarios/', views.usuarios, name="listagem_usuarios"),
]
