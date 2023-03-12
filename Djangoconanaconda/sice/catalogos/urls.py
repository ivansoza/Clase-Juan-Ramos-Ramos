from django.urls import path
from catalogos import views


urlpatterns = [
    
   path("",views.homeCatalogos, name="catalogosHome"),
   path("productos/",views.productosCatalogos, name="catalogosProducto"),
   path("profesores/list/",views.profList, name="home_catalogos"),
   path("profesores/new/",views.profNew, name="home_catalogos"),

]