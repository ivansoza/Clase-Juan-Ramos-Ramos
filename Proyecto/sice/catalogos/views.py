from django.shortcuts import render, redirect
from .forms import PropietarioForm, PlacaForm, OficinaForm, VehiculoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def homeCatalogos(request):
    return render(request,"homeCatalogos.html")

@login_required
def oficinaCatalogos(request):
    oficina_form = OficinaForm()

    if request.method =="POST":
        oficina_form = OficinaForm(data=request.POST)
        if oficina_form.is_valid():
            oficina_form.save()
            return redirect(reverse("catalogosOficina")+"?ok")
        else:
            return redirect(reverse("catalogosOficina")+"?error")
        
    return render(request,"oficinaCatalogos.html",{"form":oficina_form})

@login_required
def placaCatalogos(request):
    placa_form = PlacaForm()

    if request.method == "POST":
        placa_form = PlacaForm(data=request.POST)

        if placa_form.is_valid():
            placa_form.save()
            return redirect(reverse("catalogosPlaca")+"?ok")
        else:
            return redirect(reverse("catalogosPlaca")+"?error")
    return render(request,"placaCatalogos.html",{"form":placa_form})

@login_required
def propietarioCatalogos(request):
    propietario_form = PropietarioForm()

    if request.method == "POST":
        propietario_form = PropietarioForm(data=request.POST)

        if propietario_form.is_valid():
            propietario_form.save()
            return redirect(reverse("catalogosPropietario")+"?ok")
        else:
            return redirect(reverse("catalogosPropietario")+"?error")
    return render(request,"propietarioCatalogos.html",{"form":propietario_form})

@login_required
def vehiculoCatalogos(request):
    vehiculo_form = VehiculoForm()

    if request.method == "POST":
        vehiculo_form = VehiculoForm(data=request.POST)

        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect(reverse("catalogosVehiculo")+"?ok")
        else:
            return redirect(reverse("catalogosVehiculo")+"?error")
    return render(request,"vehiculoCatalogos.html",{"form":vehiculo_form})

def exit(request):
    logout(request)
    return redirect ("index")