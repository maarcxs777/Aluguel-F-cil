from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'html/cadastro.html')
    else:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe usuário com essas informações!')
        
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=senha)
        user.save()

        return render(request, 'html/cadastro_realizado.html')

def login(request):
    if request.method == "GET":
        return render(request, 'html/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(request, username=username, password=senha)

        if user is not None:
            auth_login(request, user)
            return render(request, 'html/home.html')
        else:
            return HttpResponse('Usuário ou Senha incorreta, não existe!')

def logout_sair(request):
    logout(request)
    return render(request, 'html/login.html')

def verificar_sistema(request):
    if request.user.is_authenticated:
        return HttpResponse('Você está logado')
    return HttpResponse('Você precisa está logado')

@login_required
def editar_usuario(request):
    if request.method == "GET":
        return render(request, 'html/configuracoes.html', {'user': request.user})
    else:  # Método POST
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        nova_senha = request.POST.get('nova_senha')

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        # Se uma nova senha for fornecida, atualiza a senha
        if nova_senha:
            user.set_password(nova_senha)
            update_session_auth_hash(request, user)  # Mantém o usuário logado após a mudança de senha

        user.save()

        return redirect('home')
    
@login_required
def perfil(request):
    return render(request, 'html/perfil.html', {'user': request.user})
 # Redireciona para a página inicial ou outra página apropriada
