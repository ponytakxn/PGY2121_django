from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("productos/<str:nom>", views.productos, name="productos"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("login/", views.signin, name="login"),
    path("agregar/<int:producto_id>", views.agregar_producto, name="agregar"),
    path("sumar/<int:producto_id>", views.sumar_producto, name="add"),
    path("restar/<int:producto_id>", views.restar_producto, name="sub"),
    path("eliminar/<int:producto_id>", views.eliminar_producto, name="del"),
    path("carrito", views.carrito, name="carrito"),
    path("checkout", views.checkout, name="checkout"),
]
