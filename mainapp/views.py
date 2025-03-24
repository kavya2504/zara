from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def homeView(request):
    return render(request, 'home.html')  

def aboutView(request):
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


