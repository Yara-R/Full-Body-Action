from django.urls import path
from app_FullBA import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('exercicios/', views.exercicios, name= 'exercicios'),
    path('treino/', views.treino, name= 'treino'),
]
