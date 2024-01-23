from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if (not username) or (not password1) or (not password2):
            messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, "O usuário já existe!")
            return redirect("signup")

        if password1 != password2:
            messages.add_message(request, constants.ERROR, "As senhas não conferem!")
            return redirect("signup")

        try:
            user = User.objects.create_user(username=username, password=password1)
            messages.add_message(
                request, constants.SUCCESS, "Usuário criado com sucesso!"
            )
            return redirect("login")
        except:
            messages.add_message(request, constants.ERROR, "Erro interno do servidor!")
            return redirect("signup")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password1")

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            messages.add_message(
                request, constants.SUCCESS, "Login realizado com sucesso!"
            )
            return redirect("/flashcard/novo_flashcard/")
        else:
            messages.add_message(
                request, constants.ERROR, "Usuário ou senha inválidos!"
            )

            return redirect("login")


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.add_message(
            request, constants.SUCCESS, "Logout realizado com sucesso!"
        )
        return redirect("login")
