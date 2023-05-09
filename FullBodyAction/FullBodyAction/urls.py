from django.urls import path
from app_FullBA import views
from django.urls import path

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

   path('comentarios/', views.comentarios, name='comentarios'),


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

    #---Exercícios Costa---
    path('costa_pull_down_aberto/', views.costa_pull_down_aberto, name='costa_pull_down_aberto'),
    path('costa_pull_down_supinado/', views.costa_pull_down_supinado, name='costa_pull_down_supinado'),
    path('costa_low_row/', views.costa_low_row, name='costa_low_row'),
    path('costa_remada_curva/', views.costa_remada_curva, name='costa_remada_curva'),


    #---Exercícios Posterior---

    path('posterior_agachamento/', views.posterior_agachamento, name='posterior_agachamento'),
    path('posterior_leg_curl/', views.posterior_leg_curl, name='posterior_leg_curl'),
    path('posterior_agachamento_smith/', views.posterior_agachamento_smith, name='posterior_agachamento_smith'),
    path('posterior_hack_squat/', views.posterior_hack_squat, name='posterior_hack_squat'),

    #---Exercícios Posterior---

    path('triceps_banco/', views.triceps_banco, name='triceps_banco'),
    path('triceps_cross_corda/', views.triceps_cross_corda, name='triceps_cross_corda'),
    path('triceps_cross_unilateral/', views.triceps_cross_unilateral, name='triceps_cross_unilateral'),
    path('triceps_frances/', views.triceps_frances, name='triceps_frances'),

]
