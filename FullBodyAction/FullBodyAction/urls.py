from django.urls import path
from app_FullBA import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]

urlpatterns = [
    path('', views.exercicios, name= 'exercicios')
    path('')

]