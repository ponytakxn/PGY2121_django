from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('productos/praga', views.praga, name='praga'),
]