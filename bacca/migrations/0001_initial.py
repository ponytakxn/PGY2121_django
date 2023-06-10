# Generated by Django 4.1.2 on 2023-06-10 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id_categoria",
                    models.AutoField(
                        db_column="idCategoria", primary_key=True, serialize=False
                    ),
                ),
                ("categoria", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Imagen",
            fields=[
                (
                    "id_imagen",
                    models.AutoField(
                        db_column="idImagen", primary_key=True, serialize=False
                    ),
                ),
                ("url_imagen", models.ImageField(null=True, upload_to="productos")),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id_producto",
                    models.AutoField(
                        db_column="idProducto", primary_key=True, serialize=False
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("precio", models.IntegerField()),
                ("stock", models.IntegerField()),
                ("count", models.IntegerField()),
                (
                    "id_categoria",
                    models.ForeignKey(
                        db_column="idCategoria",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bacca.categoria",
                    ),
                ),
                ("imagenes", models.ManyToManyField(to="bacca.imagen")),
            ],
        ),
    ]
