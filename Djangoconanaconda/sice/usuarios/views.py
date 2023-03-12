from django.shortcuts import render,HttpResponse

# Create your views here.

def homeUsuarios(request):
    return render(request, 'homeUsuarios.html')
