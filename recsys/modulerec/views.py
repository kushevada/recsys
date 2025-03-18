from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def catalog(request):
    return render(request, 'catalog.html')