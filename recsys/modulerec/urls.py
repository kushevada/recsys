from django.urls import path, include
from . import views
from moduleauth import urls as other_app_urls



urlpatterns = [
    path('auth/', include(other_app_urls)),
    path('', views.index, name='index'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('foru/', views.foru_view, name='foru'),
]
