from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy


from .forms import CustomLoginForm, CustomRegisterForm

from django.contrib.auth.views import LoginView



class UserRegister(CreateView):
    form_class = CustomRegisterForm
    template_name = 'signup.html'
    
    success_url = reverse_lazy('signin') 

class UserLogin(LoginView):
    template_name = 'signin.html'
    form_class = CustomLoginForm
