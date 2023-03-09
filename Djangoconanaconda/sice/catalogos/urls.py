from django.urls import path
from catalogos import views


urlpatterns = [
    
   path("home/",views.homeCatalogos, name="home_catalogos"),
   path("profesores/list/",views.profList, name="home_catalogos"),
   path("profesores/new/",views.profNew, name="home_catalogos"),

]