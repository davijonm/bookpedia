from django.db import models

# Create your models here.


# Nome do livro - texto com 200 caracteres + data da publicação
class Autor(models.Model):
    nome = models.CharField(max_length=200)


# Autor - Todo livro vai estar vinculado a um autor
class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    paginas = models.IntegerField(default=0, blank=True, null=True)
    resumo = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField("date published")
