from django import forms
from django.db import models
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import EmailField
import requests
from .models import Nota, Formulario
#from .views import get_dog
#from .models import entrevista

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class NoteForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué te gustaría anotar?'}), required=True)

    class Meta:
        model = Nota
        fields = ['content']

class SentimientoForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ["situacion", "detonante", "sentimiento", "intensidad"]

# class Dogs(forms.ModelForm):
#     image = forms.ImageField(default=)
#     content = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué te gustaría anotar?'}), required=True)
