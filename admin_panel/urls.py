from django.contrib import admin
from django.urls import path
from django import views
from . import views
from django.contrib.auth.decorators import user_passes_test

urlpatterns = [
    path("", user_passes_test(lambda u: u.is_superuser)(views.index), name="index"),
    path(
        "users/listar",
        user_passes_test(lambda u: u.is_superuser)(views.listarUsuario),
        name="listar-usuario",
    ),
    path(
        "users/agregar",
        user_passes_test(lambda u: u.is_superuser)(views.agregarUsuario),
        name="agregar-usuario",
    ),
    path(
        "users/actualizar/<int:id>",
        user_passes_test(lambda u: u.is_superuser)(views.actualizarUsuario),
        name="actualizar-usuario",
    ),
    path(
        "users/eliminar/<int:id>",
        user_passes_test(lambda u: u.is_superuser)(views.eliminarUsuario),
        name="eliminar-usuario",
    ),
    path(
        "products/listar",
        user_passes_test(lambda u: u.is_superuser)(views.listarProductos),
        name="listar-productos",
    ),
    path(
        "products/agregar",
        user_passes_test(lambda u: u.is_superuser)(views.agregarProducto),
        name="agregar-producto",
    ),
    path(
        "products/actualizar/<int:id>",
        user_passes_test(lambda u: u.is_superuser)(views.actualizarProducto),
        name="actualizar-producto",
    ),
    path(
        "products/eliminar/<int:id>",
        user_passes_test(lambda u: u.is_superuser)(views.eliminarProducto),
        name="eliminar-producto",
    ),
    path(
        "categorias/listar",
        user_passes_test(lambda u: u.is_superuser)(views.listarCategorias),
        name="listar-categorias",
    ),
    path(
        "categorias/agregar",
        user_passes_test(lambda u: u.is_superuser)(views.agregarCategoria),
        name="agregar-categoria",
    ),
    path(
        "categorias/actualizar/<int:id>",
        user_passes_test(lambda u: u.is_superuser)(views.actualizarCategoria),
        name="actualizar-categoria",
    ),
    path(
        "categorias/eliminar/<int:id>",
        user_passes_test(lambda u: u.is_superuser)(views.eliminarCategoria),
        name="eliminar-categoria",
    ),
    path(
        "imagenes/listar",
        user_passes_test(lambda u: u.is_superuser)(views.listarImagenes),
        name="listar-imagenes",
    ),
    path(
        "imagenes/agregar",
        user_passes_test(lambda u: u.is_superuser)(views.agregarImagen),
        name="agregar-imagen",
    ),
    path(
        "imagenes/eliminar/<int:id>",
        user_passes_test(lambda u: u.is_superuser)(views.eliminarImagen),
        name="eliminar-imagen",
    ),
]
