from django.shortcuts import HttpResponse

# Create your views here.

def homeCatalogos(request):
    return HttpResponse("ESTAS EN EL HOME DE LA APLICACION DE CATALOGOS")

def profList(request):
    return HttpResponse("Estas en la lista ")

def profNew(request):
    return HttpResponse("Estas en la lista nueva ")