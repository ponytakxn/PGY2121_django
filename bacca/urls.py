from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/<int:pk>", views.productos, name="productos"),
]
