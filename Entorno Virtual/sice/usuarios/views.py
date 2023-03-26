from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse
from django.contrib import messages



# Create your views here.
def homeUsuarios(request):
    contact_form =ContactForm()

    if request.method == "POST":
        contact_form = ContactForm( data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'El mensaje se ha enviado correctamente.')
            return redirect(reverse("usuariosHome"))
        else:
            messages.error(request, 'El mensaje no se ha enviado correctamente.')
            return redirect(reverse("usuariosHome"))

    return render(request,"homeUsuarios.html",{"form":contact_form})

