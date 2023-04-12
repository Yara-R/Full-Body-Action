from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/cadastro.html')

def login():
    pass


def usuarios(request):
    # Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('password')
    novo_usuario.save()

    # Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a pagina de listagem de usuários 
    return render(request, 'usuarios/usuarios.html', usuarios)


def treino(request, dealer_id):
    #usuario irá escolher o musculo no qual quer visualizar os exercicios 
    treino = treino()
    treino.t = request('treino')
    