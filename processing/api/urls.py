from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("get-authors", views.get_home),
    path("add-authors/", views.post_home)
]
