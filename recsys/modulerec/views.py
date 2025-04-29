from django.shortcuts import render, redirect, get_object_or_404
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

# каталог
def catalog_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None

        if profile:
            if profile.goal == 'gain':
                products = products.filter(is_for_weight_gain=True)
            elif profile.goal == 'lose':
                products = products.filter(is_for_weight_loss=True)
            else:
                products = products.filter(is_for_weight_main=True)

    return render(request, 'catalog.html', {
        'categories': categories, 
        'products': products,
        'profile': profile,
        })

# кнопки исключений
@login_required
def exclude_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    profile = Profile.objects.get(user=request.user)
    profile.excluded_products.add(product)
    return redirect('catalog')

@login_required
def exclude_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    profile = Profile.objects.get(user=request.user)
    products_in_category = Product.objects.filter(category=category)
    profile.excluded_products.add(*products_in_category)
    return redirect('catalog')

# кнопки включений
@login_required
def include_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    profile = Profile.objects.get(user=request.user)
    profile.excluded_products.remove(product)
    return redirect('catalog')

@login_required
def include_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    profile = Profile.objects.get(user=request.user)
    products_in_category = Product.objects.filter(category=category)
    profile.excluded_products.remove(*products_in_category)
    return redirect('catalog')

# рекомендации
@login_required
def foru_view(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return redirect('profile')

    # выбор цели
    form = GoalForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        profile.goal = form.cleaned_data['goal']
        profile.save()
        return redirect('foru')

    # расчет суточной нормы БЖУ и ккал
    pfc = profile.calculate_daily_pfc()

    # исключенные продукты
    excluded = profile.excluded_products.all()

    # парсинг с фильтром по цели
    if profile.goal == 'gain':
        products = Product.objects.filter(is_for_weight_gain=True).exclude(id__in=excluded)
    elif profile.goal == 'lose':
        products = Product.objects.filter(is_for_weight_loss=True).exclude(id__in=excluded)
    else:
        products = Product.objects.filter(is_for_weight_main=True).exclude(id__in=excluded)
    
    return render(request, 'foru.html', {
        'profile': profile,
        'products': products,
        'goal_form': form,
        'macros': pfc,
        'user_goal': profile.goal,
    })