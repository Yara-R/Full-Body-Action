from django.urls import path
from app_FullBA import views

urlpatterns = [
    path('home/', views.home, name= 'treino'),
    path('cadastro/', views.cadastro, name='usuarios'),
    path('login/', views.login, name='login'),
    path('consumo_agua/', views.registro, name='registro_agua'),
    path('biceps/', views.musculo, name ='biceps'),
    path('costas/', views.musculo, name ='costas'),
    path('peito/', views.musculo, name ='peito'),
    path('quadriceps/', views.musculo, name ='quadriceps'),
    path('triceps/', views.musculo, name ='triceps'), 
    path('panturrilha/', views.musculo, name ='panturrilha'),
    path('gluteos/', views.musculo, name ='gluteos'),
    path('posterior/', views.musculo, name ='posterior'),
    path('antebraco/', views.musculo, name ='antebraco'),
]
