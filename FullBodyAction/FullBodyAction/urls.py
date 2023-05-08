from django.urls import path
from app_FullBA import views
from django.urls import path
from app_FullBA.views import rate_view

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    # path('login/', user_login, name='login'),
    path('perfil/', views.perfil, name='perfil'),

    path('consumo_agua/', views.registro, name='registro_agua'),
    path('medidas/', views.medidas, name= 'medidas'),
    
    path('academias/', views.academias, name='academias'),

    path('treino/', views.treino, name='treino'),
    path('musculo/', views.smash, name='smash'),
    path('rate/', rate_view, name='rate'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),


    #Exercicios Biceps---
    path('rosca_com_barra/', views.rosca_com_barra, name='rosca_com_barra'),
    path('rosca_martelo/', views.rosca_martelo, name= 'rosca_martelo'),
    path('rosca_unilateral/', views.rosca_unilateral, name ='rosca_unilateral'),
    path('rosca_apoiada/', views.rosca_apoiada, name ='rosca_apoiada')

]
