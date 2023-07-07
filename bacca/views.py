from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Producto, Categoria, Imagen
from .Carrito import Carrito
from django.utils.text import slugify
from django.http import JsonResponse


# Create your views here.


def signup(request):
    if request.method == "GET":
        return render(request, "bacca/signup.html")
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    email=request.POST["email"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                context = {"error": "El usuario ya existe"}
                return render(request, "bacca/signup.html", context)
        else:
            context = {"error": "Contraseñas no coinciden"}
            return render(request, "bacca/signup.html", context)


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "bacca/signin.html")
    else:
        print(request.POST)
        user = authenticate(
            request,
            username=request.POST["login_usuario"],
            password=request.POST["login_clave"],
        )
        if user is None:
            return render(request, "bacca/signin.html", {"error": "Usuario no existe"})
        else:
            login(request, user)
            return redirect("home")


def index(request):
    productos = Producto.objects.all()

    context = {"productos": productos}
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


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    print(producto.imagenes.first().url_imagen.url)
    slug = slugify(producto.nombre)
    carrito.agregar(producto)
    return redirect("productos", nom=slug)


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.eliminar(producto)
    return redirect("home")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.restar(producto)
    return redirect("home")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("home")
