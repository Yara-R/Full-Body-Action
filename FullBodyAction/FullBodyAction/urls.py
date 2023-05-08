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
    path('biceps_rosca_com_barra/', views.biceps_rosca_com_barra, name='biceps_rosca_com_barra'),
    path('biceps_rosca_martelo/', views.biceps_rosca_martelo, name= 'biceps_rosca_martelo'),
    path('biceps_rosca_unilateral/', views.biceps_rosca_unilateral, name ='biceps_rosca_unilateral'),
    path('biceps_rosca_apoiada/', views.biceps_rosca_apoiada, name ='biceps_rosca_apoiada'),

    #---Exercicios Peito---
    path('peito_supino/', views.peito_supino, name='peito_supino'),
    path('peito_crucifixo/', views.peito_crucifixo, name='peito_crucifixo'),
    path('peito_cross_over/', views.peito_cross_over, name='peito_cross_over'),
    path('peito_peck_deck/', views.peito_peck_deck, name='peito_peck_deck'),



]
