from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('foru/', views.foru_view, name='foru'),
    path('exclude/<int:product_id>/', views.exclude_product, name='exclude_product'),
    path('exclude_category/<int:category_id>/', views.exclude_category, name='exclude_category'),
    path('include/<int:product_id>/', views.include_product, name='include_product'),
    path('include_category/<int:category_id>/', views.include_category, name='include_category'),
]
