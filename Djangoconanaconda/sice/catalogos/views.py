
from django.shortcuts import render,HttpResponse

# Create your views here.

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

def productosCatalogos(request):
    return render(request, 'productosCatalogos.html')

def profList(request):
    return HttpResponse("Estas en la lista ")

def profNew(request):
    return HttpResponse("Estas en la lista nueva ")