from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == "GET":
        return render(request,'usuarios/cadastro.html')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('password')
    novo_usuario.save()

def login(request):
    if request.method == "POST":
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

def treino(request):
    if request.method =="POST":
        return render(request,'usuarios/treino.html')
    else:
        return HttpResponse('Deu zica')
    

@login_required    
def exercicios(request):
    return HttpResponse('Você precisa está logado')

    return render(request,'treino.html', treino)
