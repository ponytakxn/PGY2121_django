from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column="idCategoria", primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)


class Imagen(models.Model):
    id_imagen = models.AutoField(db_column="idImagen", primary_key=True)
    url_imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        imgUrl = str(self.url_imagen)
        splittedUrl = imgUrl.split("/")
        return splittedUrl[1]


class Producto(models.Model):
    id_producto = models.AutoField(db_column="idProducto", primary_key=True)
    nombre = models.CharField(max_length=40, blank=False, null=False)
    id_categoria = models.ForeignKey(
        "Categoria", on_delete=models.CASCADE, db_column="idCategoria"
    )
    imagenes = models.ManyToManyField("Imagen")
    precio = models.IntegerField()
    stock = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return str(self.nombre)


class Pedido(models.Model):
    id = models.AutoField(db_column="idPedido", primary_key=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, db_column="cliente")
    carrito = models.TextField()
    total = models.IntegerField()
    tipo_pago = models.CharField(max_length=20, blank=False, null=False)
    estado = models.CharField(max_length=20, blank=False, null=False)


class FormularioContacto(models.Model):
    id = models.AutoField(db_column="idFormulario", primary_key=True)
    email = models.CharField(max_length=40, blank=False, null=False)
    solicitud = models.TextField()
    suscrito = models.BooleanField()
