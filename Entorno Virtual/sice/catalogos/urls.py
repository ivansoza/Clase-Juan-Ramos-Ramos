from django.urls import path
from catalogos import views

# Una lista de patrones de URL.
urlpatterns = [
    path("",views.homeCatalogos, name="catalogosHome"),
    path("productos/",views.productosCatalogos, name="catalogosProducto"),
    path("servicios/",views.serviciosCatalogos, name="catalogosServicios")


]
