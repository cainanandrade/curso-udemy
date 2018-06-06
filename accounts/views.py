from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import UserForm

# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save() #instanciando o form para cripitografrar a senha
            u.set_password(u.password) #comando para criptografar a senha
            u.save() #sem isso o usuário não consegue completar o login
            return HttpResponse('Usuário criado com sucesso!')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(username=u, password=p)

        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuário ou senha inválido!')
    return render(request, 'accounts/user_login.html')

def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, 'Não foi possível alterar sua senha!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form':form})



