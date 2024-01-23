from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from .models import Categoria, Flashcard


def add_flashcard(request):
    if not request.user.is_authenticated:
        messages.add_message(
            request, constants.SUCCESS, "Logout realizado com sucesso!"
        )
        return redirect("login")

    if request.method == "GET":
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        flashcards = Flashcard.objects.filter(user=request.user)

        categoria_filtrada = request.GET.get("categoria")
        dificuldade_filtrada = request.GET.get("dificuldade")

        if categoria_filtrada:
            flashcards = flashcards.filter(categoria__id=categoria_filtrada)

        if dificuldade_filtrada:
            flashcards = flashcards.filter(dificuldade=dificuldade_filtrada)

        return render(
            request,
            "add_flashcard.html",
            {
                "categorias": categorias,
                "dificuldades": dificuldades,
                "flashcards": flashcards,
            },
        )
    elif request.method == "POST":
        pergunta = request.POST.get("pergunta")
        resposta = request.POST.get("resposta")
        categoria = request.POST.get("categoria")
        dificuldade = request.POST.get("dificuldade")

        if len(pergunta.strip()) == 0 or len(resposta.strip()) == 0:
            messages.add_message(
                request,
                constants.ERROR,
                "Preencha todos os campos!",
            )
            return redirect("add_flashcard")

        flashcard = Flashcard(
            user=request.user,
            pergunta=pergunta,
            resposta=resposta,
            categoria_id=categoria,
            dificuldade=dificuldade,
        )

        flashcard.save()

        messages.add_message(
            request, constants.SUCCESS, "Flashcard criado com sucesso!"
        )

        return redirect("add_flashcard")
