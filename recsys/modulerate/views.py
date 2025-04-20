from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Rating
from modulerec.models import Product
from .forms import RatingForm
from django.http import HttpResponseForbidden


# Create your views here.
@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data['value']
            

            existing_rating = Rating.objects.filter(user=request.user, product=product).first()
            
            if existing_rating:
                existing_rating.value = rating_value
                existing_rating.save()
            else:
                rating = Rating(user=request.user, product=product, value=rating_value)
                rating.save()
            
            return redirect('catalog')
    else:
        form = RatingForm()
    
    return render(request, 'product_detail.html', {
        'form': form, 
        'product': product
        })