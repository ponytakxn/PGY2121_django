from django.shortcuts import render
from .models import Producto, Categoria, Imagen


# Create your views here.
def index(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, "bacca/index.html", context)


def productos(request, pk):
    producto = Producto.objects.get(id_producto=pk)
    context = {"producto": producto}
    return render(request, "bacca/views/productos.html", context)
