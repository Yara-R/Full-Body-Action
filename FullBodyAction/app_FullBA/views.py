from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Comentario, Avaliacao
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Medidas
from django.views.decorators.csrf import csrf_protect



# Página Home

def home(request):
    if request.method =="POST":
        return render(request,'usuarios/home.html')
    elif request.method =="GET":
        return render(request,'usuarios/home.html')
    else:
        return HttpResponse('Deu zica')
    
#-------------------------------------------------------------------------------------------------------------

# Escolha do músculo (História 1)

def treino(request):
    if request.method =="POST":
        return render(request, 'usuarios/treino.html')
    elif request.method =="GET":
        return render(request, 'usuarios/treino.html')
    else:
        return HttpResponse('Deu zica')

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
    
def redirect_to_muscle(request):
    muscle = request.GET.get('muscle', '')
    if muscle:
        return redirect(f'/muscle/{muscle}/')
    else:
        return redirect('index')
    
#-------------------------------------------------------------------------------------------------------------

# Cadastro, login dos usuários
    
def login(request):
    if request.method == 'POST' or request.method == 'GET':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password')
            
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})
    
def cadastro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'usuarios/login.html')
    else:
        form = UserForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})



 #------------------------------------------------------------------------------------------------------------- 

# Resgistro de água (História 2)

#@login_required 
def registro(request):
    if request.method == "POST":
        return render(request, 'usuarios/registro_agua.html')
    if request.method =="GET":
        return render(request,'usuarios/registro_agua.html')
    else:
        return HttpResponse('Algo deu errado :/')
    
#-------------------------------------------------------------------------------------------------------------

# Resgistro de Medidas corporais (História 3)

#@login_required 
@csrf_protect
def medidas(request):
    # form = medidasForm()
    # return render(request, 'usuarios/medidas.html', {
    #     'form': form
    # })
    if request.method == "GET":
        return render(request,'usuarios/medidas.html')
    else:
        peito = request.POST["peito"]
        costas = request.POST["costas"]
        ombros = request.POST["ombros"]
        pescoco = request.POST["pescoco"]
        braco = request.POST["braco"]
        antebraco = request.POST["antebraco"]
        quadril = request.POST["quadril"]
        cintura = request.POST["cintura"]
        coxa = request.POST["coxa"]
        panturrilha = request.POST["panturrilha"]

        medidas = Medidas(peito=peito, costas=costas, ombros=ombros, pescoco=pescoco, 
                          braco=braco, antebraco=antebraco, quadril =quadril,
                          cintura=cintura, coxa=coxa, panturrilha=panturrilha)
        medidas.save()


#-------------------------------------------------------------------------------------------------------------

# Pagina do usuario (História 6) 
   
#@login_required 
def perfil(request):
    if request.method == "GET":
        info = Usuario.objects.all()
        return render(request,'usuarios/perfil.html', {'nome' : info})
    else:
        return HttpResponse('Ocorreu um erro')

#-------------------------------------------------------------------------------------------------------------    

# Mapa das academias proximas (História 7)    
def academias(request):
    if request.method =="POST":
        return render(request, 'usuarios/academias.html')
    elif request.method =="GET":
        return render(request, 'usuarios/academias.html')
    else:
        return HttpResponse('Deu zica')

def mostrar_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all()
    media_avaliacoes = avaliacoes.aggregate(models.Avg('estrelas'))
    return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes, 'media_avaliacoes': media_avaliacoes})

def comentarios(request):
    comentarios = Comentario.objects.all().order_by('-data')
    if request.method == 'POST':
        autor = request.POST['autor']
        texto = request.POST['texto']
        Comentario.objects.create(autor=autor, texto=texto)
        return redirect('comentarios')
    return render(request, 'comentarios.html', {'comentarios': comentarios})

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
    elif request.method =="GET":
        return render(request, 'usuarios/antebraco_rosca_punho.html')
    else:
        return HttpResponse('Deu zica')
    
def antebraco_rosca_inversa_punho(request):
    if request.method =="POST":
        return render(request, 'usuarios/antebraco_rosca_inversa_punho.html')
    elif request.method =="GET":
        return render(request, 'usuarios/antebraco_rosca_inversa_punho.html')
    else:
        return HttpResponse('Deu zica')
    
def antebraco_rosca_inversa_punho_dumbell(request):
    if request.method =="POST":
        return render(request, 'usuarios/antebraco_rosca_inversa_punho_dumbell.html')
    elif request.method =="GET":
        return render(request, 'usuarios/antebraco_rosca_inversa_punho_dumbell.html')
    else:
        return HttpResponse('Deu zica')
    
def antebraco_rosca_punho_cross_over(request):
    if request.method =="POST":
        return render(request, 'usuarios/antebraco_rosca_punho_cross_over.html')
    elif request.method =="GET":
        return render(request, 'usuarios/antebraco_rosca_punho_cross_over.html')
    else:
        return HttpResponse('Deu zica')