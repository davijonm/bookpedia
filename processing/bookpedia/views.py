from django.shortcuts import render, get_object_or_404

from .models import Livro, Autor

# Create your views here.


def index(request):
    autor_list = Autor.objects.all
    context = {"autor_list": autor_list}
    return render(request, "bookpedia/index.html", context)


def resultados(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    livros_list = autor.livro_set.all()
    context = {"livros_list": livros_list}
    return render(request, "bookpedia/resultados.html", context)


def resumo(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    context = {"livro": livro}
    return render(request, "bookpedia/resumo.html", context)
