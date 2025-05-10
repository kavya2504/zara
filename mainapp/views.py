from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import AddProductForm  


# Home Page View
def homeView(request):
    template = loader.get_template('home.html')
    context = {
        'products': Product.objects.all(),
        'search_bar': True,
        'current_page': 'home'
    }
    return HttpResponse(template.render(context, request))


# Product Detail Page (CBV)
class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'


# About Page View
def aboutView(request):
    template = loader.get_template('about.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Contact Page View
def contactView(request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Add Product (CreateView)
class AddProduct(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = AddProductForm
    success_url = '/'


# Edit Product (UpdateView)
class EditProduct(UpdateView):
    model = Product
    context_object_name = 'product'
    template_name = 'edit_product.html'
    fields = ['img', 'price', 'stock', 'desc']
    success_url = '/'


# Delete Product (DeleteView)
class DelProduct(DeleteView):
    model = Product
    template_name = 'del_product.html'
    success_url = '/'


# 🔍 Search View (fixed and moved outside any class)
def searchView(request):
    query = request.GET.get('search_text')
    result_products = Product.objects.filter(name__icontains=query)

    context = {
        'prods': result_products,
        'query': query,
        'search_bar': True
    }

    template = loader.get_template('search_results.html')
    return HttpResponse(template.render(context, request))