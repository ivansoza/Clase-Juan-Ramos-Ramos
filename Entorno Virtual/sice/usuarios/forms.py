from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
       # fields = "__all__"
        fields =  ["name","email","message","contact_type","subscription"]