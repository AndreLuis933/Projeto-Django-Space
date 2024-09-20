from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from usuarios.forms import LoginForm, CadastroForm

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form['nome'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password= senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request,f'{nome} logado com sucesso!')
                return redirect('index')

            else:
                messages.error(request, 'Erro ao efetuar login')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            
            nome = form['nome'].value()
            email = form['email'].value()
            senha = form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuario ja existente')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logaut realizado com sucesso')
    return redirect('login')

