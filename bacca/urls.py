from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/<str:nom>", views.productos, name="productos"),
]
