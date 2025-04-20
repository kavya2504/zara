# this file is for building custom forms.

from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Import your Product model
from .models import Product

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your username'
        })
    )

    password = forms.CharField(
        label = 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your password'
        })
    )

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your username'
        })
    )

    password1 = forms.CharField(
        label = 'Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Enter your password'
        })
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget= forms.PasswordInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Confirm Password'
        })
    )

    class Meta:
        model = User 
        fields = ('username','password1','password2')



class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
