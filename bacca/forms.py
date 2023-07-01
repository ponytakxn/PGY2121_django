from django.forms import ModelForm
from .models import Producto


class ProductForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "id_categoria", "imagenes", "precio", "stock", "count"]
