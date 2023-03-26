from django.urls import path
from usuarios import views

urlpatterns = [
    path("",views.homeUsuarios,name="usuariosHome"),
    path("usuarios/",views.formUsuarios,name="usuariosForm")
]
