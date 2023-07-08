from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Producto, Pedido, FormularioContacto
from .Carrito import Carrito
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
import json

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
    if request.method == "POST":
        suscrito = request.POST.get("usr_aceptocondiciones") == "true"
        print("suscrito" + str(suscrito))
        formulario = FormularioContacto.objects.create(
            email=request.POST["usr_email"],
            solicitud=request.POST["usr_solicitud"],
            suscrito=suscrito,
        )
        formulario.save()
        return redirect("home")
    else:
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


def sumar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")


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
    return redirect("carrito")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.restar(producto)
    return redirect("carrito")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")


@login_required
def carrito(request):
    context = {"productos": Producto.objects.all()}
    return render(request, "bacca/views/carrito_detalle.html", context)


@login_required
def checkout(request):
    cart = Carrito(request)
    if request.method == "POST":
        pedido_carrito = cart.procesar_carrito()
        pedido = Pedido.objects.create(
            cliente=request.user,
            carrito=json.dumps(pedido_carrito),
            total=int(request.POST["total-compra"]),
            tipo_pago=request.POST["tipo-pago"],
            estado="pendiente",
        )
        pedido.save()
        for productos in pedido_carrito:
            producto = Producto.objects.get(id_producto=productos.get("id_producto"))
            producto.stock -= productos.get("cantidad")
            producto.count += productos.get("cantidad")
            producto.save()
        cart.limpiar()
        return redirect("home")
    else:
        return render(request, "bacca/views/checkout.html")


@login_required
def misPedidos(request):
    pedidos = Pedido.objects.all()
    pedidos_parsed = []

    for pedido in pedidos:
        pedido.carrito = json.loads(pedido.carrito)
        pedidos_parsed.append(pedido)

    context = {
        "productos": Producto.objects.all(),
        "pedidos": pedidos_parsed,
        "usuario": request.user,
    }

    return render(request, "bacca/views/pedidos.html", context)
