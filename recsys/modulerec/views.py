from django.shortcuts import render, redirect
from .models import Category, Product
from moduleauth.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import GoalForm


# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def foru(request):
    return render(request, 'foru.html')

def catalog_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog.html', {'categories': categories, 'products': products})

@login_required
def foru_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('profile')

    form = GoalForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        profile.goal = form.cleaned_data['goal']
        profile.save()
        return redirect('foru')

    if profile.goal == 'gain':
        products = Product.objects.filter(is_for_weight_gain=True)
    elif profile.goal == 'lose':
        products = Product.objects.filter(is_for_weight_loss=True)
    else:
        products = Product.objects.filter(is_for_weight_main=True)
    
    return render(request, 'foru.html', {
            'profile': profile,
            'products': products,
            'goal_form': form
        })