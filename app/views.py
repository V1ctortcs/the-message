from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Users
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):

    if request.POST:
        username = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=',request.user,'Entrou -=-=-=-=-=-=-=-=-=-=-=-=-=' )
            login(request, user)
            return redirect('/themessage/home/')
        else:
            messages.error(request, 'Usuário ou Senha Ivalidos, Tente Novamente')
    return redirect('themessage/login/')


@login_required(login_url='themessage/login')
def home (request):
    return render(request,'home.html')

def logout_user(request):
    print ('-=-=-=-=-=-=-=-=-=-=-=-=-=',request.user,'Saiu -=-=-=-=-=-=-=-=-=-=-=-=-=')
    logout(request)
    return redirect ('/themessage/login/')

def perfil_user(request):
    user = Users.objects.filter(ativo=True, user=request.user)
    return render(request, 'perfil.html', {'user_model': user})

def registrar_user(request):
    return render(request, 'registrar.html')

def recuper_senha_user(request):
    return render(request, 'recuperarsenha.html')

def set_user(request):

    usernome = request.POST.get('nome')
    usersobrenome = request.POST.get('sobrenome')
    username = request.POST.get('user')
    useremail = request.POST.get('email')
    usersenha = request.POST.get('senha')

    if User.objects.filter(username=username):
        messages.error(request, 'Usuário Invalido!! Já em uso')
        return redirect('/themessage/registrar/')
    else:
        user = User.objects.create_user(username, useremail, usersenha, first_name=usernome, last_name=usersobrenome)
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=', user, 'cadastrado -=-=-=-=-=-=-=-=-=-=-=-=-=')
        return redirect('/themessage/login/')