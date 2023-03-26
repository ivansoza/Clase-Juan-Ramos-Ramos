from django.urls import path
from catalogos import views

# Una lista de patrones de URL.
urlpatterns = [
    path("",views.homeCatalogos, name="catalogosHome"),
    path('crear_placa/', views.crear_placa, name='crear_placa'),
    path("productos/",views.productosCatalogos, name="catalogosProducto"),
    path("servicios/",views.serviciosCatalogos, name="catalogosServicios"),


]
