from django.urls import path
from app_cadastro import views

urlpatterns = [
    #fullbodyaction.com/cadastro/
    path('cadastro/', views.cadastro, name='cadastro'),
]
