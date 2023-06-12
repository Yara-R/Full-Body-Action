from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Medidas, Agua, Cadastro, Avaliacao, User
from .models import Comentario_Antebraco_rosca_inversa_punho_dumbell, Comentario_antebraco_rosca_punho_cross_over
from .models import Comentario_antebraco_rosca_punho, Comentario_antebraco_rosca_inversa_punho
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import models


# Página Home
def homee(request):
    if request.method =="POST":
        return render(request,'usuarios/homee.html')
    elif request.method =="GET":
        return render(request,'usuarios/homee.html')
    else:
        return HttpResponse('Deu zica')

def home(request):
    if request.method =="POST":
        return render(request,'usuarios/home.html')
    elif request.method =="GET":
        return render(request,'usuarios/home.html')
    else:
        return HttpResponse('Deu zica')
    
#-------------------------------------------------------------------------------------------------------------

# Escolha do músculo (História 1)

# @login_required

def treino(request):
    if request.method =="POST":
        return render(request, 'usuarios/treino.html')
    elif request.method =="GET":
        return render(request, 'usuarios/treino.html')
    else:
        return HttpResponse('Deu zica')

# @login_required
def smash(request):
    musculo = request.GET.get('musculo')
    if musculo == 'biceps':
        return render(request, 'usuarios/biceps.html')
    elif musculo =='costas':
        return render(request, f'usuarios/costas.html')
    elif musculo == 'peito':
        return render(request, f'usuarios/peito.html')
    elif musculo == 'quadriceps':
        return render(request, f'usuarios/quadriceps.html')
    elif musculo == 'triceps':
        return render(request, f'usuarios/triceps.html')
    elif musculo == 'panturrilhas':
        return render(request, f'usuarios/panturrilhas.html')
    elif musculo == 'gluteos':
        return render(request, f'usuarios/gluteos.html')
    elif musculo == 'posterior':
        return render(request, f'usuarios/posterior.html')
    elif musculo == 'antebraco':
        return render(request, f'usuarios/antebraco.html')
# @login_required    
def redirect_to_muscle(request):
    muscle = request.GET.get('muscle', '')
    if muscle:
        return redirect(f'/muscle/{muscle}/')
    else:
        return redirect('index')
    
#-------------------------------------------------------------------------------------------------------------

# Cadastro, login dos usuários

def cadastro(request):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get("name", "")
        email = request.POST.get("email", "")
        senha = request.POST.get("senha", "")
        peso = request.POST.get("peso", 0.0)
        altura = request.POST.get("altura", 0.0)
        idade = request.POST.get("idade", 0)

        cadastro = Cadastro(nome=nome, email=email, senha=senha, peso=peso, altura=altura, idade=idade)
        ##cadastro.save()

        return redirect('login')
     
@csrf_protect
def login_view(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    elif request.method == "POST":
        email = request.POST.get("email", "")
        senha = request.POST.get("senha", "")
        user = authenticate(request, email=email, senha=senha)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('home')
        else:
            return HttpResponse("Credenciais inválidas.")

 #------------------------------------------------------------------------------------------------------------- 

# Resgistro de água (História 2)

# @login_required 
@csrf_protect

def agua(request):
    if request.method == "GET":
        return render(request, 'usuarios/agua.html')
    
    elif request.method == "POST":
        data = float(request.POST.get("data", 0))
        hora = float(request.POST.get("hora", 0))
        quantidade = float(request.POST.get("quantidade", 0))

        Agua.objects.create(data=data, hora=hora, quantidade=quantidade)
    
        return redirect('home')  

    
#-------------------------------------------------------------------------------------------------------------

# Resgistro de Medidas corporais (História 3)


# @login_required 
@csrf_protect
def medidas(request):
    if request.method == "GET":
        # print("Funcionou")
        return render(request,'usuarios/medidas.html')

    if request.method == "POST":
        peito = float(request.POST.get("peito", 0))
        costas = float(request.POST.get("costas", 0))
        ombro = float(request.POST.get("ombro", 0))
        pescoco = float(request.POST.get("pescoco", 0))
        braco = float(request.POST.get("braco", 0))
        antebraco = float(request.POST.get("antebraco", 0))
        quadril = float(request.POST.get("quadril", 0))
        cintura = float(request.POST.get("cintura", 0))
        coxa = float(request.POST.get("coxa", 0))
        panturrilha = float(request.POST.get("panturrilha", 0))

        # print("Funcionou")
        Medidas.objects.create(peito=peito, costas=costas, ombro=ombro, pescoco=pescoco, 
                          braco=braco, antebraco=antebraco, quadril=quadril,
                          cintura=cintura, coxa=coxa, panturrilha=panturrilha)
        
        return HttpResponse("Funcionou")


#-------------------------------------------------------------------------------------------------------------

# Pagina do usuario (História 6)

# @login_required
def perfil(request):
    if request.method == "GET" or request.method == "POST":
        info = User.objects.all()
        return render(request,'usuarios/perfil.html', {'nome' : info})
    else:
        return HttpResponse('Ocorreu um erro')

#-------------------------------------------------------------------------------------------------------------    

# Mapa das academias proximas (História 7)    
def academias(request):
    # if request.method =="POST":
    #     return render(request, 'usuarios/academias.html')
    if request.method =="GET":
        return render(request, 'usuarios/academias.html')
    else:
        return HttpResponse('Deu zica')
    
def academiass(request):
    # if request.method =="POST":
    #     return render(request, 'usuarios/academias.html')
    if request.method =="GET":
        return render(request, 'usuarios/academiass.html')
    else:
        return HttpResponse('Deu zica')

def mostrar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    media_avaliacoes = avaliacoes.aggregate(models.Avg('estrelas'))
    return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes, 'media_avaliacoes': media_avaliacoes})



#-------------------------------------------------------------------------------------------------------------

#Exercícios de Bíceps:

def biceps_rosca_martelo(request):
    if request.method == "POST":
        return render(request, 'usuarios/biceps_rosca_martelo.html')
    elif request.method == "GET":
        return render(request, 'usuarios/biceps_rosca_martelo.html')
    else:
        return HttpResponse('Deu zica')

def biceps_rosca_unilateral(request):
    if request.method == "POST":
        return render(request, 'usuarios/biceps_rosca_unilateral.html')
    elif request.method == "GET":
        return render(request, 'usuarios/biceps_rosca_unilateral.html')
    else:
        return HttpResponse('Deu zica')


def rosca_apoiada(request):
    if request.method =='POST':
        return render(request, 'usuarios/rosca_apoiada.html')
    elif request.method =='GET':
        return render(request, 'usuario/rosca_apoiada.html')
    else:
        return HttpResponse('Deu zica')
         

def biceps_rosca_apoiada(request):
    if request.method == "POST":
        return render(request, 'usuarios/biceps_rosca_apoiada.html')
    elif request.method == "GET":
        return render(request, 'usuarios/biceps_rosca_apoiada.html')
    else:
        return HttpResponse('Deu zica')

def biceps_rosca_com_barra(request):
    if request.method =="POST":
        return render(request, 'usuarios/biceps_rosca_com_barra.html')
    elif request.method =="GET":
        return render(request, 'usuarios/biceps_rosca_com_barra.html')
    else:
        return HttpResponse('Deu zica')
    

#-------------------------------------------------------------------------------------------------------------

#Exericicos de Peito

def peito_supino(request):
    if request.method =="POST":
        return render(request, 'usuarios/peito_supino.html')
    elif request.method =="GET":
        return render(request, 'usuarios/peito_supino.html')
    else:
        return HttpResponse('Deu zica')
    
def peito_crucifixo(request):
    if request.method =="POST":
        return render(request, 'usuarios/peito_crucifixo.html')
    elif request.method =="GET":
        return render(request, 'usuarios/peito_crucifixo.html')
    else:
        return HttpResponse('Deu zica')
    
def peito_cross_over(request):
    if request.method =="POST":
        return render(request, 'usuarios/peito_cross_over.html')
    elif request.method =="GET":
        return render(request, 'usuarios/peito_cross_over.html')
    else:
        return HttpResponse('Deu zica')
    
def peito_peck_deck(request):
    if request.method =="POST":
        return render(request, 'usuarios/peito_peck_deck.html')
    elif request.method =="GET":
        return render(request, 'usuarios/peito_peck_deck.html')
    else:
        return HttpResponse('Deu zica')
    

#-------------------------------------------------------------------------------------------------------------

#Exericicos de Costas

def costa_pull_down_aberto(request):
    if request.method =="POST":
        return render(request, 'usuarios/costa_pull_down_aberto.html')
    elif request.method =="GET":
        return render(request, 'usuarios/costa_pull_down_aberto.html')
    else:
        return HttpResponse('Deu zica')
    
def costa_pull_down_supinado(request):
    if request.method =="POST":
        return render(request, 'usuarios/costa_pull_down_supinado.html')
    elif request.method =="GET":
        return render(request, 'usuarios/costa_pull_down_supinado.html')
    else:
        return HttpResponse('Deu zica')
    
def costa_low_row(request):
    if request.method =="POST":
        return render(request, 'usuarios/costa_low_row.html')
    elif request.method =="GET":
        return render(request, 'usuarios/costa_low_row.html')
    else:
        return HttpResponse('Deu zica')
    
def costa_remada_curva(request):
    if request.method =="POST":
        return render(request, 'usuarios/costa_remada_curva.html')
    elif request.method =="GET":
        return render(request, 'usuarios/costa_remada_curva.html')
    else:
        return HttpResponse('Deu zica')

#-------------------------------------------------------------------------------------------------------------

#Exericicos de Posterior

def posterior_agachamento(request):
    if request.method =="POST":
        return render(request, 'usuarios/posterior_agachamento.html')
    elif request.method =="GET":
        return render(request, 'usuarios/posterior_agachamento.html')
    else:
        return HttpResponse('Deu zica')
    
def posterior_leg_curl(request):
    if request.method =="POST":
        return render(request, 'usuarios/posterior_leg_curl.html')
    elif request.method =="GET":
        return render(request, 'usuarios/posterior_leg_curl.html')
    else:
        return HttpResponse('Deu zica')
    
def posterior_agachamento_smith(request):
    if request.method =="POST":
        return render(request, 'usuarios/posterior_agachamento_smith.html')
    elif request.method =="GET":
        return render(request, 'usuarios/posterior_agachamento_smith.html')
    else:
        return HttpResponse('Deu zica')
    
def posterior_hack_squat(request):
    if request.method =="POST":
        return render(request, 'usuarios/posterior_hack_squat.html')
    elif request.method =="GET":
        return render(request, 'usuarios/posterior_hack_squat.html')
    else:
        return HttpResponse('Deu zica')

#-------------------------------------------------------------------------------------------------------------

#Exericicos de Posterior

def triceps_banco(request):
    if request.method =="POST":
        return render(request, 'usuarios/triceps_banco.html')
    elif request.method =="GET":
        return render(request, 'usuarios/triceps_banco.html')
    else:
        return HttpResponse('Deu zica')
    
def triceps_cross_corda(request):
    if request.method =="POST":
        return render(request, 'usuarios/triceps_cross_corda.html')
    elif request.method =="GET":
        return render(request, 'usuarios/triceps_cross_corda.html')
    else:
        return HttpResponse('Deu zica')
    
def triceps_cross_unilateral(request):
    if request.method =="POST":
        return render(request, 'usuarios/triceps_cross_unilateral.html')
    elif request.method =="GET":
        return render(request, 'usuarios/triceps_cross_unilateral.html')
    else:
        return HttpResponse('Deu zica')
    
def triceps_frances(request):
    if request.method =="POST":
        return render(request, 'usuarios/triceps_frances.html')
    elif request.method =="GET":
        return render(request, 'usuarios/triceps_frances.html')
    else:
        return HttpResponse('Deu zica')

#-------------------------------------------------------------------------------------------------------------

#Exericicos antebraço

def antebraco_rosca_punho(request):
    if request.method =="POST":
        return render(request, 'usuarios/antebraco_rosca_punho.html')
    elif request.method == "POST":
        autor = request.POST.get("autor", "")
        texto = request.POST.get("texto", "")
        Comentario_antebraco_rosca_punho.objects.create(autor=autor, texto=texto)
    
    comentarios = Comentario_antebraco_rosca_punho.objects.all()
    return render(request, 'usuarios/antebraco_rosca_punho.html', {'comentarios': comentarios})
    
def antebraco_rosca_inversa_punho(request):
    if request.method =="POST":
        return render(request, 'usuarios/antebraco_rosca_inversa_punho.html')
    elif request.method =="POST":
        autor = request.POST.get("autor", "")
        texto = request.POST.get("texto", "")
        Comentario_antebraco_rosca_inversa_punho.objects.create(autor=autor, texto=texto)
    
    comentarios = Comentario_antebraco_rosca_inversa_punho.objects.all()
    return render(request, 'usuarios/antebraco_rosca_inversa_punho.html', {'comentarios': comentarios})
    
def antebraco_rosca_inversa_punho_dumbell(request):
    if request.method =="POST":
        return render(request, 'usuarios/antebraco_rosca_inversa_punho_dumbell.html')
    elif request.method == "POST":
        autor = request.POST.get("autor", "")
        texto = request.POST.get("texto", "")
        Comentario_Antebraco_rosca_inversa_punho_dumbell.objects.create(autor=autor, texto=texto)
    
    comentarios = Comentario_Antebraco_rosca_inversa_punho_dumbell.objects.all()
    return render(request, 'usuarios/antebraco_rosca_inversa_punho_dumbell.html', {'comentarios': comentarios})
    
    
def antebraco_rosca_punho_cross_over(request):
    if request.method =="POST":
        return render(request, 'usuarios/antebraco_rosca_punho_cross_over.html')
    elif request.method =="POST":
        autor = request.POST.get("autor", "")
        texto = request.POST.get("texto", "")
        Comentario_antebraco_rosca_punho_cross_over.objects.create(autor=autor, texto=texto)
    
    comentarios = Comentario_antebraco_rosca_punho_cross_over.objects.all()
    return render(request, 'usuarios/antebraco_rosca_punho_cross_over.html', {'comentarios': comentarios})
    
#-------------------------------------------------------------------------------------------------------------

#Exercícios de Panturrilhas:


def panturrilha_gemeos_elevacao(request):
    if request.method =="POST":
        return render(request, 'usuarios/panturrilha_gemeos_elevacao.html')
    elif request.method =="GET":
        return render(request, 'usuarios/panturrilha_gemeos_elevacao.html')
    else:
        return HttpResponse('Deu zica')
    
def panturrilha_gemeos_sentado(request):
    if request.method =="POST":
        return render(request, 'usuarios/panturrilha_gemeos_sentado.html')
    elif request.method =="GET":
        return render(request, 'usuarios/panturrilha_gemeos_sentado.html')
    else:
        return HttpResponse('Deu zica')
    
def panturrilha_gemeos_maquina_em_pe(request):
    if request.method =="POST":
        return render(request, 'usuarios/panturrilha_gemeos_maquina_em_pe.html')
    elif request.method =="GET":
        return render(request, 'usuarios/panturrilha_gemeos_maquina_em_pe.html')
    else:
        return HttpResponse('Deu zica')
    
def panturrilha_flexora_vertical(request):
    if request.method =="POST":
        return render(request, 'usuarios/panturrilha_flexora_vertical.html')
    elif request.method =="GET":
        return render(request, 'usuarios/panturrilha_flexora_vertical.html')
    else:
        return HttpResponse('Deu zica')
    
#-------------------------------------------------------------------------------------------------------------

#Exercícios de Quadriceps:

def quadriceps_cadeira_extensora(request):
    if request.method =="POST":
        return render(request, 'usuarios/quadriceps_cadeira_extensora.html')
    elif request.method =="GET":
        return render(request, 'usuarios/quadriceps_cadeira_extensora.html')
    else:
        return HttpResponse('Deu zica')
    
def quadriceps_cadeira_flexora(request):
    if request.method =="POST":
        return render(request, 'usuarios/quadriceps_cadeira_flexora.html')
    elif request.method =="GET":
        return render(request, 'usuarios/quadriceps_cadeira_flexora.html')
    else:
        return HttpResponse('Deu zica')
    
def quadriceps_afundo(request):
    if request.method =="POST":
        return render(request, 'usuarios/quadriceps_afundo.html')
    elif request.method =="GET":
        return render(request, 'usuarios/quadriceps_afundo.html')
    else:
        return HttpResponse('Deu zica')
    
def quadriceps_hack_squat(request):
    if request.method =="POST":
        return render(request, 'usuarios/quadriceps_hack_squat.html')
    elif request.method =="GET":
        return render(request, 'usuarios/quadriceps_hack_squat.html')
    else:
        return HttpResponse('Deu zica')

#-------------------------------------------------------------------------------------------------------------

#Exercícios de Gluteos:


def gluteo_crew(request):
    if request.method =="POST":
        return render(request, 'usuarios/gluteo_crew.html')
    elif request.method =="GET":
        return render(request, 'usuarios/gluteo_crew.html')
    else:
        return HttpResponse('Deu zica')
    
def gluteo_caneleira(request):
    if request.method =="POST":
        return render(request, 'usuarios/gluteo_caneleira.html')
    elif request.method =="GET":
        return render(request, 'usuarios/gluteo_caneleira.html')
    else:
        return HttpResponse('Deu zica')
    
def gluteo_caneleira_extensao(request):
    if request.method =="POST":
        return render(request, 'usuarios/gluteo_caneleira_extensao.html')
    elif request.method =="GET":
        return render(request, 'usuarios/gluteo_caneleira_extensao.html')
    else:
        return HttpResponse('Deu zica')
    
def gluteo_maquina(request):
    if request.method =="POST":
        return render(request, 'usuarios/gluteo_maquina.html')
    elif request.method =="GET":
        return render(request, 'usuarios/gluteo_maquina.html')
    else:
        return HttpResponse('Deu zica')
    
#---------------------------------------------------------------------------------------------

def registro_treinos(request):
    if request.method =="POST":
        return render(request, 'usuarios/registro_treinos.html')
    elif request.method =="GET":
        return render(request, 'usuarios/registro_treinos.html')
    else:
        return HttpResponse('Deu zica')
    
     #------------------------------------------------------------------------------------------------------------- 

# Resgistro de água (História 2)

# @login_required 
@csrf_protect

def montar_treino(request):
    if request.method == "GET":
        return render(request, 'Usuarios/MontarTreino.html')
    
    elif request.method == "POST":    
        return redirect('home')
    
