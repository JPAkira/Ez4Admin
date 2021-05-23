from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        if campo_vazio(username) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(request, username=username, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('index')
            else:
                messages.error(request, 'Senha errada')
                return redirect('login')
        else:
            messages.error(request, 'Login ou senha errada')
            return redirect('login')
    return render(request, 'index/register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def campo_vazio(campo):
    return not campo.strip()