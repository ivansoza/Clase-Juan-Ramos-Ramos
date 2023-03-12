from django.shortcuts import render,HttpResponse

# Create your views here.

def homeRevisiones(request):
    return render(request, 'homeRevisiones.html')
