from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def homeUsuarios(request):
    return render(request,"homeUsuarios.html")

def formUsuarios(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect (reverse("usuariosForm")+"?ok")

        else:
            return redirect (reverse("usuariosForm")+"?error") 


    return render(request,"formUsuarios.html",{"form":contact_form})