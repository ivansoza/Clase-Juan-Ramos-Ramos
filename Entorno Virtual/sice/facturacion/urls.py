from django.urls import path
from facturacion import views

urlpatterns = [
    path("",views.homeFacturacion, name="facturacionHome")
]
