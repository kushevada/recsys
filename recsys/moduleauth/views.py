from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import Profile


# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

def profile(request):
    return render(request, "profile.html")

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/signin')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')