from django.urls import path
from catalogos import views


urlpatterns = [
    path("",views.homeCatalogos, name="catalogosHome"),
    path("oficina/",views.oficinaCatalogos, name="catalogosOficina"),
    path("placa/",views.placaCatalogos, name="catalogosPlaca"),
    path("propietario/",views.propietarioCatalogos,name="catalogosPropietario"),
    path("vehiculo/",views.vehiculoCatalogos,name="catalogosVehiculo"),
    path("logout/",views.exit,name="exit"),
    path("register/",views.register,name="register"),

]
