from django.urls import path
from app_FullBA import views

urlpatterns = [
    path('home/', views.home, name = 'treino'),
    path('cadastro/', views.cadastro, name='usuarios'),
    path('login/', views.login, name='login'),
    path('biceps/', views.treino, name ='biceps'),
    path('costas/', views.treino, name ='costas'),
    path('peito/', views.treino, name ='peito'),
    path('quadriceps/', views.treino, name ='quadriceps'),
    path('triceps/', views.treino, name ='triceps'), 
    path('panturrilha/', views.treino, name ='panturrilha'),
    path('gluteos/', views.treino, name ='gluteos'),
    path('posterior/', views.treino, name ='posterior'),
    path('antebraco/', views.treino, name ='antebraco'),
    path('consumo_agua/', views.registro, name='registro_agua')
]
