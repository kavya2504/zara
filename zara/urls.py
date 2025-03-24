"""
URL configuration for zara project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  
from mainapp import views  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homeView, name="homepage"),  
    path("about/", views.aboutView, name="aboutpage"),
    path("contact/", views.contactpageView, name="contactpage"),  
    path('category/', views.Categorie1, name='Categorie1'),
    path('category2/', views.Categorie2, name='Categorie2'),
    path('Categorie3/', views.Categorie3, name='Categorie3'),
    path('search/', views.search_results, name='search_results'),

]



