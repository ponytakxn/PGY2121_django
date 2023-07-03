from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from bacca.models import Producto, Categoria, Imagen

# Create your views here.
TEMPLATE_DIRS = 'os.path.join(BASE_DIR, "templates")'


def index(request):
    return render(request, "index.html")


def listarUsuario(request):
    context = {"usuarios": User.objects.all()}
    return render(request, "users/listarUsuario.html", context)


def agregarUsuario(request):
    if request.method == "GET":
        return render(request, "users/agregarUsuario.html")
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password1"],
                    is_superuser=request.POST["radio"],
                )
                user.save()
                return redirect("listar-usuario")
            except IntegrityError:
                context = {"error": "El usuario ya existe"}
                return render(request, "users/agregarUsuario.html", context)
        else:
            context = {"error": "Contraseñas no coinciden"}
            return render(request, "users/agregarUsuario.html", context)


def actualizarUsuario(request, id):
    context = {
        "usuario": User.objects.get(id=id),
    }
    if request.method == "GET":
        return render(request, "users/actualizarUsuario.html", context)
    else:
        user = User.objects.create_user(
            id=id,
            username=request.POST["username"],
            email=request.POST["email"],
            is_superuser=request.POST["radio"],
        )
        user.save()
        return redirect("listar-usuario")


def eliminarUsuario(request, id):
    user_to_delete = User.objects.get(id=id)
    user_to_delete.delete()
    return redirect("listar-usuario")


def listarProductos(request):
    context = {
        "productos": Producto.objects.all(),
    }
    return render(request, "products/listarProductos.html", context)


def agregarProducto(request):
    context = {
        "categorias": Categoria.objects.all(),
        "imagenes": Imagen.objects.all(),
    }
    if request.method == "GET":
        return render(request, "products/agregarProducto.html", context)
    else:
        product = Producto.objects.create(
            nombre=request.POST["nombre"],
            id_categoria=get_object_or_404(
                Categoria, categoria=request.POST["categoria"]
            ),
            precio=request.POST["precio"],
            stock=request.POST["stock"],
            count=request.POST["count"],
        )
        product.imagenes.set(request.POST.getlist("imagenes"))
        product.save()
        return redirect("listar-productos")


def actualizarProducto(request, id):
    context = {
        "producto": Producto.objects.get(id_producto=id),
    }

    if request.method == "GET":
        return render(request, "products/actualizarProducto.html", context)
    else:
        producto = Producto.objects.get(id_producto=id)
        producto.nombre = request.POST["nombre"]
        producto.precio = request.POST["precio"]
        producto.stock = request.POST["stock"]
        producto.count = request.POST["count"]
        producto.save()
        return redirect("listar-productos")


def eliminarProducto(request, id):
    product_to_delete = Producto.objects.get(id_producto=id)
    product_to_delete.delete()
    return redirect("listar-productos")


def listarCategorias(request):
    context = {"categorias": Categoria.objects.all()}
    return render(request, "categorias/listarCategorias.html", context)


def agregarCategoria(request):
    if request.method == "GET":
        return render(request, "categorias/agregarCategoria.html")
    else:
        categoria = Categoria.objects.create(
            categoria=request.POST["categoria"].lower(),
        )
        categoria.save()
        return redirect("listar-categorias")


def actualizarCategoria(request, id):
    context = {
        "categoria": Categoria.objects.get(id_categoria=id),
    }

    if request.method == "GET":
        return render(request, "categorias/actualizarCategoria.html", context)
    else:
        categoria = Categoria.objects.get(id_categoria=id)
        categoria.categoria = request.POST["categoria"].lower()
        categoria.save()
        return redirect("listar-categorias")


def eliminarCategoria(request, id):
    categoria_to_delete = Categoria.objects.get(id_categoria=id)
    categoria_to_delete.delete()
    return redirect("listar-categorias")
