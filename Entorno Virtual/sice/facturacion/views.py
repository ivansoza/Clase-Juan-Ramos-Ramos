from django.shortcuts import render, HttpResponse

# Create your views here.
def  homeFacturacion(request):
    return render (request,'homeFacturacion.html')