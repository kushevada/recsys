from django.shortcuts import render
from .models import Category, Product
from moduleauth.models import Profile



# Create your views here.
def index(request):
    return render(request, "index.html")

def catalog(request):
    return render(request, 'catalog.html')

def foru(request):
    return render(request, 'foru.html')

def catalog_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog.html', {'categories': categories, 'products': products})

   


# def foru_view(request):

