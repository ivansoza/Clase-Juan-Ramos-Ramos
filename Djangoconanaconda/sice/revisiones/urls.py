from django.urls import path
from revisiones import views


urlpatterns = [
    
   path("",views.homeRevisiones, name="revisionesHome"),


]