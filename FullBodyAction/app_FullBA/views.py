from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def home(request):
    if request.method =="POST":
        return render(request,'usuarios/treino.html')
    if request.method =="GET":
        return render(request,'usuarios/treino.html')
    else:
        return HttpResponse('Deu zica')

def home(request):
    if request.method == 'POST':
        grupo_muscular = request.POST.get('grupo_muscular')
        if grupo_muscular == 'Bíceps':
            return redirect('biceps.html')
        elif grupo_muscular =='Costas':
            return redirect('costas.html')
        elif grupo_muscular == 'Peito':
            return redirect('peito.html')
        elif grupo_muscular == 'Quadriceps':
            return redirect('quadriceps.html')
        elif grupo_muscular== 'Tríceps':
            return redirect('triceps.html')
        elif grupo_muscular == 'Panturrilhas':
            return redirect('panturrilhas.html')
        elif grupo_muscular == 'Glutéos':
            return redirect('gluteos.html')
        elif grupo_muscular == 'Posterior':
            return redirect('posterior.html')
        elif grupo_muscular == 'Antebraço':
            return redirect('antebraco.html')

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
    return render(request,'treino.html', treino)

def registro(request):
    if request.method == "POST":
        return render(request, 'usuarios/registro_agua.html')
    if request.method =="GET":
        return render(request,'usuarios/registro_agua.html')
    else:
        return HttpResponse('Algo deu errado :/')