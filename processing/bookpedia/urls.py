from django.urls import path

from . import views

app_name = "bookpedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:autor_id>/resultados/", views.resultados, name="resultados"),
    path("<int:livro_id>/resumo/", views.resumo, name="resumo"),
]
