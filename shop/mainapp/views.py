import json
from urllib.request import urlopen

from django.shortcuts import render

from .models import Category, Product


def index(request):
    products = Product.objects.all()[:4]
    context = {
        "products": products,
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request, slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    print('--------> ', categories)
    context = {
        'categories': categories,
    }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    json_response = urlopen(url)
    fake_json = json.loads(json_response.read())

    context = {
        "contacts": fake_json[:3],
    }

    return render(request, 'mainapp/contact.html', context=context)
