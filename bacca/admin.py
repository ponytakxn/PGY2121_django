from django.contrib import admin
from .models import Producto, Categoria, Imagen, Pedido, FormularioContacto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Imagen)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(FormularioContacto)
