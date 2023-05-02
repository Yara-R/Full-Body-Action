from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse

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

def cadastro(request):
    # Salvar os dados da tela para o banco de dados
    if request.method == "GET":
        return render(request,'usuarios/cadastro.html')
    if request.method == "POST":
        return render(request,'usuarios/cadastro.html')
    else:
        return HttpResponse('Erro')
    
def usuario(request):
    user = User.objects.create_user(request.POST['nome'], request.POST['email'], request.POST['password'])
    user.save()

def login(request):
    if request.method == "POST":
        return render(request,'usuarios/login.html')
    if request.method == "GET":
        return render(request,'usuarios/login.html')
    
    login_usuario = Usuario()
    login_usuario.email_login = request.POST.get('email')
    login_usuario.senha_login = request.POST.get('senha')

    user = authenticate(request, email=login_usuario.email_login, senha=login_usuario.senha_login)

    if user is not None:
        login(request, user)
        return render(request, 'usuarios/perfil.html')
    else:
        return HttpResponse('Email ou senha errados')

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
def medidas(request):
    if request.method == "GET":
        return render(request,'usuarios/medidas.html')
    else:
        return HttpResponse('Ocorreu um erro')

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
    
#-------------------------------------------------------------------------------------------------------------

#Exercícios de Bíceps:

def rosca_com_barra(request):
    if request.method =="POST":
        return render(request, 'usuarios/rosca_com_barra.html')
    elif request.method =="GET":
        return render(request, 'usuarios/rosca_com_barra.html')
    else:
        return HttpResponse('Deu zica')
    
def rate_view(request):
  rating_value = request.POST.get('rating')
  # faça algo com o valor da avaliação, como salvar no banco de dados
  return JsonResponse({'success': True})
