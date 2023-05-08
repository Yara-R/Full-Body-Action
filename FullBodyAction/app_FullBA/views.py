from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm, UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Medidas

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

@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'usuarios/rosca_com_barra.html', {'form': form})



def rosca_martelo(request):
    if request.method == "POST":
        return render(request, 'usuarios/rosca_martelo.html')
    elif request.method == "GET":
        return render(request, 'usuarios/rosca_martelo.html')
    else:
        return HttpResponse('Deu zica')

def rosca_unilateral(request):
    if request.method == "POST":
        return render(request, 'usuarios/rosca_unilateral.html')
    elif request.method == "GET":
        return render(request, 'usuarios/rosca_unilateral.html')
    else:
        return HttpResponse('Deu zica')
    
