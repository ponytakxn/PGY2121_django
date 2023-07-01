from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/<str:nom>", views.productos, name="productos"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("login/", views.signin, name="login"),
]
