from django.urls import path
from app_FullBA import views
from django.urls import path
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('perfil/', views.perfil, name='perfil'),


    path('consumo_agua/', views.agua, name='registro_agua'),

    path('admin/', admin.site.urls),
    path ('accounts/', include('django.contrib.auth.urls')),

    path('consumo_agua/', views.agua, name='registro_agua'),
    path('medidas/', views.medidas, name= 'medidas'),
    
    path('academias/', views.academias, name='academias'),

    path('registro_treinos/', views.registro_treinos, name='registro_treinos'),



    path('rosca_com_barra/', views.biceps_rosca_com_barra, name='rosca_com_barra'),
    path('rosca_martelo/', views.biceps_rosca_martelo, name= 'rosca_martelo'),
    path('rosca_unilateral/', views.biceps_rosca_unilateral, name ='rosca_unilateral'),
    path('rosca_apoiada', views.biceps_rosca_apoiada, name = 'rosca_apoiada'),

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

    #---Exercícios tríceps---

    path('triceps_banco/', views.triceps_banco, name='triceps_banco'),
    path('triceps_cross_corda/', views.triceps_cross_corda, name='triceps_cross_corda'),
    path('triceps_cross_unilateral/', views.triceps_cross_unilateral, name='triceps_cross_unilateral'),
    path('triceps_frances/', views.triceps_frances, name='triceps_frances'),

 #---Exercícios antebraço---

    path('antebraco_rosca_punho/', views.antebraco_rosca_punho, name='antebraco_rosca_punho'),
    path('antebraco_rosca_inversa_punho/', views.antebraco_rosca_inversa_punho, name='antebraco_rosca_inversa_punho'),
    path('antebraco_rosca_inversa_punho_dumbell/', views.antebraco_rosca_inversa_punho_dumbell, name='antebraco_rosca_inversa_punho_dumbell'),
    path('antebraco_rosca_punho_cross_over/', views.antebraco_rosca_punho_cross_over, name='antebraco_rosca_punho_cross_over'),


 #---Exercícios panturrilhas---

    path('panturrilha_gemeos_elevacao/', views.panturrilha_gemeos_elevacao, name= 'panturrilha_gemeos_elevacao'),
    path('panturrilha_gemeos_sentado/', views.panturrilha_gemeos_sentado, name = 'panturrilha_gemeos_sentado'),
    path('panturrilha_gemeos_maquina_em_pe/', views.panturrilha_gemeos_maquina_em_pe, name = 'panturrilha_gemeos_maquina_em_pe'),
    path('panturrilha_flexora_vertical/', views.panturrilha_flexora_vertical, name = 'panturrilha_flexora_vertical'),

#---Exercícios quadriceps---

    path('quadriceps_cadeira_extensora/', views.quadriceps_cadeira_extensora, name= 'quadriceps_cadeira_extensora'),
    path('quadriceps_cadeira_flexora/', views.quadriceps_cadeira_flexora, name = 'quadriceps_cadeira_flexora'),
    path('quadriceps_afundo/', views.quadriceps_afundo, name = 'quadriceps_afundo'),
    path('quadriceps_hack_squat/', views.quadriceps_hack_squat, name = 'quadriceps_hack_squat'),


#---Exercícios panturrilhas---

    path('gluteo_crew/', views.gluteo_crew, name= 'gluteo_crew'),
    path('gluteo_caneleira/', views.gluteo_caneleira, name = 'gluteo_caneleira'),
    path('gluteo_caneleira_extensao/', views.gluteo_caneleira_extensao, name = 'gluteo_caneleira_extensao'),
    path('gluteo_maquina/', views.gluteo_maquina, name = 'gluteo_maquina'),

    
] 
