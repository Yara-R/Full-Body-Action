from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def home(request):
    if request.method =="POST":
        return render(request,'usuarios/treino.html')
    elif request.method =="GET":
        return render(request,'usuarios/treino.html')
    else:
        return HttpResponse('Deu zica')

def treino(request):
    if request.method == 'POST':
        grupo_muscular = request.POST.get('grupo_muscular')
        if grupo_muscular == 'biceps':
            return redirect('usuarios/biceps.html')
        elif grupo_muscular =='costas':
            return redirect('usuarios/costas.html')
        elif grupo_muscular == 'peito':
            return redirect('usuarios/peito.html')
        elif grupo_muscular == 'quadriceps':
            return redirect('usuarios/quadriceps.html')
        elif grupo_muscular== 'tríceps':
            return redirect('usuarios/triceps.html')
        elif grupo_muscular == 'panturrilhas':
            return redirect('usuarios/panturrilhas.html')
        elif grupo_muscular == 'gluteos':
            return redirect('usuarios/gluteos.html')
        elif grupo_muscular == 'posterior':
            return redirect('usuarios/posterior.html')
        elif grupo_muscular == 'antebraço':
            return redirect('usuarios/antebraco.html')

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