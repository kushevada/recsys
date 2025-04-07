from django.contrib import admin
from .models import Category, Product


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'caloricity', 'proteins', 'fats', 'carbohydrates', 
        'is_for_weight_main', 'is_for_weight_gain', 'is_for_weight_loss')
    list_filter = ('category', 'is_for_weight_loss')
    search_fields = ('name',)
    


admin.site.register(Category)
admin.site.register(Product, ProductsAdmin)