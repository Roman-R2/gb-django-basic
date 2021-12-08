import json
from urllib.request import urlopen

from django.shortcuts import get_object_or_404, render

from basketapp.models import Basket
from mainapp.models import Category, Product
from mainapp.services import get_basket, get_hot_product, get_same_products, \
    get_links_menu


def index(request):
    products = Product.objects.all()[:4]
    context = {
        "products": products,
        'basket': get_basket(request.user)
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request, slug=None):
    if slug is None:
        products_list = Product.objects.all()
        this_category = {"name": "Все"}
        hot_product = products_list.first()
        print(hot_product)
    else:
        this_category = get_object_or_404(Category, slug=slug)
        products_list = Product.objects.filter(category__slug=slug)
        hot_product = get_hot_product(this_category)
        print(hot_product)

    context = {
        'links_menu': get_links_menu(),
        'products_list': products_list,
        'this_category': this_category,
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
        'basket': get_basket(request.user),
        # 'basket': sum(list(Basket.objects.filter(
        #     user=request.user
        # ).values_list('quantity', flat=True)))
    }
    return render(request, 'mainapp/products.html', context=context)


def contact(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    json_response = urlopen(url)
    fake_json = json.loads(json_response.read())

    context = {
        "contacts": fake_json[:3],
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/contact.html', context=context)


def product(request, slug):
    context = {
        'links_menu': get_links_menu(),
        'product': get_object_or_404(Product, slug=slug),
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', context=context)
