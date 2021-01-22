from django import forms
from .models import Contacto, Bicicleta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#formulario para contacto
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos" ]

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Bicicleta
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', "last_name", "email", "password1", "password2"]