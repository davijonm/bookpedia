from django.db import models

# Create your models here.

# Nome do livro - texto com 200 caracteres + data da publicação
class Livro(models.Model):
    nome_livro = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


# Autor - Todo livro vai estar vinculado a um autor
class Autor(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    nome_autor = models.CharField(max_length = 200)
    paginas = models.IntegerField(default=0)