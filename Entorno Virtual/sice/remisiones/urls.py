from django.urls import path
from remisiones import views

urlpatterns = [
    path("",views.homeRemisiones, name="remisionesHome")
]
