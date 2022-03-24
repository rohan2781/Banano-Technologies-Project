from django.core import validators
from django import forms
from .models import extended_user
from django.contrib.auth.models import User

class ClientRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','last_name','email','password')
        widgets = {
        'username' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
