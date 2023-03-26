from django.shortcuts import render, HttpResponse
from .forms import PlacaForm

# Create your views here.

def crear_placa(request):
    if request.method == 'POST':
        form = PlacaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_confirmacion')
    else:
        form = PlacaForm()

    return render(request, 'homeCatalogos.html', {'form': form})

def homeCatalogos(request):
    return render(request, 'homeCatalogos.html')

def productosCatalogos(request):
    return render(request, 'productosCatalogos.html')

def serviciosCatalogos(request):
    return render(request, 'serviciosCatalogos.html')