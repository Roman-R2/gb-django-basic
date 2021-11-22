from django.urls import path

from . import views

app_name = 'mainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),

    path('products/all/', views.products, name='products_all'),
    path('products/home/', views.products, name='products_home'),
    path('products/office/', views.products, name='products_office'),
    path('products/modern/', views.products, name='products_modern'),
    path('products/classic/', views.products, name='products_classic'),

]
