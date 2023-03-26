from django.shortcuts import render

# Create your views here.
def homeRemisiones(request):
    return render(request,"homeRemisiones.html")