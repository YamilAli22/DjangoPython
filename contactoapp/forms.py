from django import forms
from .models import Contacto

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=30, label="Tu nombre", required=True)
    email = forms.EmailField(max_length=25, label="Tu email", required=True)
    mensaje = forms.CharField(max_length=500, label="Mensaje", required=True, widget=forms.Textarea)
    