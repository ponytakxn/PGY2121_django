from django.shortcuts import render
from .models import Producto, Categoria, Imagen


# Create your views here.


def parseUrl(nombre):
    return "-".join(nombre.lower().split(" "))


def index(request):
    productos = Producto.objects.all()

    context = {"productos": productos, "parseUrl": parseUrl}
    return render(request, "bacca/index.html", context)


def productos(request, nom):
    nomList = nom.split("-")
    nomNewList = []
    for palabra in nomList:
        palabra = palabra.capitalize()
        nomNewList.append(palabra)
    decodeNom = " ".join(nomNewList)

    producto = Producto.objects.get(nombre=decodeNom)
    context = {"producto": producto}
    return render(request, "bacca/views/productos.html", context)
