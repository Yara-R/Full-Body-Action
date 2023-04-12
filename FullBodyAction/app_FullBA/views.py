from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate

def home(request):
    return render(request,'usuarios/cadastro.html')

def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('password')
    novo_usuario.save()

    return render(request,'usuarios/login.html')

def login(request):
    if request.method == "GET":
        return render(request,'usuarios/login.html')
    else:
        email = request.Post.get('email')
        senha = request.POST.get('senha')

        user = authenticate(email=email, senha=senha)

        if user:
            return render(request, 'usuarios/exercicios.html')
        else:
            return HttpResponse("Email ou senha inválidos")
        

def treino(request):
    return render(request,'treino.html', treino)

        
def exercicios():
    pass