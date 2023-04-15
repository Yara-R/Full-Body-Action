from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def home(request):
    if request.method =="POST":
        return render(request,'usuarios/treino.html')
    elif request.method =="GET":
        return render(request,'usuarios/treino.html')
    else:
        return HttpResponse('Deu zica')

def smash(request):
    musculo = request.GET.get('musculo')
    if musculo == 'biceps':
        return render(request, f'usuarios/biceps.html')
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

def cadastro(request):
    # Salvar os dados da tela para o banco de dados
    if request.method == "GET":
        return render(request,'usuarios/cadastro.html')
                      
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('password')
    novo_usuario.save()

def login(request):
    if request.method == "POST":
        return render(request,'usuarios/login.html')
    if request.method == "GET":
        return render(request,'usuarios/login.html')
    
    login_usuario = Usuario()
    login_usuario.email_login = request.POST.get('email')
    login_usuario.senha_login = request.POST.get('senha')

    user = authenticate(email=login_usuario.email_login, senha=login_usuario.senha_login)

    if user:
        login(request, user)
        return render(request, 'usuarios/treino.html')
    else:
        return HttpResponse('Email ou senha errados')


@login_required    
def exercicios(request):
    return render(request,'treino.html')

def registro(request):
    if request.method == "POST":
        return render(request, 'usuarios/registro_agua.html')
    if request.method =="GET":
        return render(request,'usuarios/registro_agua.html')
    else:
        return HttpResponse('Algo deu errado :/')