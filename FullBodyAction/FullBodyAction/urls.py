from django.urls import path
from app_FullBA import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.usuarios, name='usuarios'),
    path('login/', views.login, name='login'),
    path('exercicios/', views.exercicios, name= 'exercicios'),
    path('treino/', views.treino, name= 'treino'),
    path('consumo_agua/', views.registro, name='registro_agua'),
    path('biceps/', views.biceps, name ='biceps'),
    path('costas/', views.costas, name ='costas'),
    path('peito/', views.peito, name ='peito'),
    path('quadriceps/', views.quadriceps, name ='quadriceps'),
    path('triceps/', views.triceps, name ='triceps'), 
    path('panturrilha/', views.panturrilha, name ='panturrilha'),
    path('gluteos/', views.gluteos, name ='gluteos'),
    path('posterior/', views.posterior, name ='posterior'),
    path('antebraco/', views.antebraco, name ='antebraco'),
]
