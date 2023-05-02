from django.urls import path
from app_FullBA import views
from django.urls import path
from app_FullBA.views import rate_view

urlpatterns = [
    path('', views.home, name = 'home'),
    path('treino/', views.treino, name='treino'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('musculo/', views.smash, name='smash'),
    path('consumo_agua/', views.registro, name='registro_agua'),
    path('medidas/', views.medidas, name= 'medidas'),
    path('usuarios/', views.usuario, name= 'usuarios'),
    path('perfil/', views.perfil, name='perfil'),
    path('academias/', views.academias, name='academias'),

    path('rosca_com_barra/', views.rosca_com_barra, name='rosca_com_barra'),
    path('rate/', rate_view, name='rate'),
]
