from django.urls import path
from app_FullBA import views

urlpatterns = [
    path('home/', views.home, name= 'treino'),
    path('cadastro/', views.cadastro, name='usuarios'),
    path('login/', views.login, name='login'),
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
