from django.db import models


# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column="idCategoria", primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)


class Imagen(models.Model):
    id_imagen = models.AutoField(db_column="idImagen", primary_key=True)
    url_imagen = models.ImageField(upload_to="productos", null=True)


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
