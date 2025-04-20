from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserInfoForm, WeightHistoryForm
from .models import Profile, WeightHistory
from modulerec.forms import ExcludedProductsForm


# Create your views here.
# регистрация
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
            except ValidationError as e:
                form.add_error(None, e)
        return redirect('/signin')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

# авторизация
def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

# выход
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

# профиль
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    weight_form = WeightHistoryForm()

    if request.method == 'POST':
        info_form = UserInfoForm(request.POST, instance=profile)
        excl_form = ExcludedProductsForm(request.POST, instance=profile)
        weight_form = WeightHistoryForm(request.POST)

        if info_form.is_valid() and excl_form.is_valid():
            info_form.save()
            excl_form.save()
            return redirect('profile')
        
        elif 'save_weight' in request.POST and weight_form.is_valid():
            wh = weight_form.save(commit=False)
            wh.profile = profile
            wh.save()
            profile.weight = wh.weight
            profile.save()
            return redirect('profile')
        
    else:
        info_form = UserInfoForm(instance=profile)
        excl_form = ExcludedProductsForm(instance=profile)

    history = profile.weight_history.order_by('date')
    weights = [entry.weight for entry in history]
    dates = [entry.date.strftime('%d.%m') for entry in history]

    return render(request, 'profile.html', {
        'form': info_form, 
        'excl_form': excl_form,
        'weight_form': weight_form,
        'weights': weights,
        'dates': dates,
        })