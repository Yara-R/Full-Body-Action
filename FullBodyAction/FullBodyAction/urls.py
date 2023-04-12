from django.urls import path
from app_FullBA import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]

urlpatterns = [
    path('', views.treino, name= 'treino'),
    path('', views.exercicios_do_musculos, name='variedade de treinos'),
    path('', views.avaliacao, name = 'avaliação dos treinos'),

]