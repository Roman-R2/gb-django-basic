from django.shortcuts import render

from authapp.models import ShopUser
from mainapp.models import Product, Category


def users(request):
    context = {
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/users_list.html', context=context)


def user_create(request):
    context = {

    }
    return render(request, '', context=context)


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


def categories(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'adminapp/categories_list.html', context=context)


def category_create(request):
    context = {

    }
    return render(request, '', context=context)


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def products(request, pk):
    context = {
        'object_list': Product.objects.filter(category__pk=pk),
    }

    return render(request, 'adminapp/products_list.html', context=context)


def product_create(request):
    context = {

    }
    return render(request, '', context=context)


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def product_read(request):
    pass
