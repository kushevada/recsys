from django.shortcuts import render
from .models import Category, Product
from moduleauth.models import Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, "index.html")

def catalog(request):
    return render(request, 'catalog.html')

@login_required
def foru(request):
    return render(request, 'foru.html')

def catalog_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog.html', {'categories': categories, 'products': products})

@login_required
def foru_view(request):
    profile = Profile.objects.get(user=request.user)
    
    if profile.goal == 'gain':
        products = Product.objects.filter(is_for_weight_gain=True)
    elif profile.goal == 'lose':
        products = Product.objects.filter(is_for_weight_loss=True)
    else:
        products = Product.objects.filter(is_for_weight_main=True)
    
    return render(request, 'foru.html', {
        'profile': profile,
        'products': products
    })