from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('foru/', views.foru, name='foru'),
]
