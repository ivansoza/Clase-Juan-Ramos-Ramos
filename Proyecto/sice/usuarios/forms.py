from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta: 
        model = Contact
        #fields = '__all__' Mostrar todos los campos
        fields = ["name", "email","message","contact_type","subscription"]
