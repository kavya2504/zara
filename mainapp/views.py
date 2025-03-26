from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse

from .models import Product



def homeView(request):
    template = loader.get_template('home.html')
    context = {
        'products': Product.objects.all()

    }
    return HttpResponse(template.render(context,request))

def aboutView(request):
    template = loader.get_template('about.html')
    context={}
    return render(request, 'about.html')  

def contactpageView(request):
    return render(request, 'contact.html') 



def Categorie1(request):
    return render(request, 'category.html') 

def Categorie2(request):
    return render(request, 'category2.html')
def Categorie3(request):
    return HttpResponse("This is Categorie3 page")
def search_results(request):
    return HttpResponse("This is the search results page")
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})


