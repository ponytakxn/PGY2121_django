from django.shortcuts import render
from .models import Producto, Categoria, Imagen


# Create your views here.
def index(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "bacca/index.html", context)


def praga(request):
    context = {}
    return render(request, "bacca/views/praga.html", context)
