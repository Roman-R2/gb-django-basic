import json
from urllib.request import urlopen

from django.http import Http404
from django.shortcuts import render, get_object_or_404

from mainapp.models import Category, Product


def index(request):
    products = Product.objects.all()[:4]
    context = {
        "products": products,
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request, slug=None):
    categories = Category.objects.all()

    if slug is None:
        products_list = Product.objects.all()
        this_category = {"name": "Все"}
    else:
        this_category = get_object_or_404(Category, slug=slug)
        products_list = Product.objects.filter(category__slug=slug)

    context = {
        'links_menu': categories,
        'products_list': products_list,
        'this_category': this_category,
        # 'hot_product': Product.objects.all().first(),
        'same_products': Product.objects.all()[:3],
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
