
# Importación de las funciones render y HttpResponse desde el módulo django.shortcuts.
from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html')