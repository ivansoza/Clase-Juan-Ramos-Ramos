from django.shortcuts import render, HttpResponse

# Create your views here.

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

def productosCatalogos(request):
    return render(request, 'productosCatalogos.html')

def serviciosCatalogos(request):
    return render(request, 'serviciosCatalogos.html')