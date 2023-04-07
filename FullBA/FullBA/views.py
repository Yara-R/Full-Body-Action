from django.shortcuts import render

def minha_view(request):
    return render(request, 'main.html')
