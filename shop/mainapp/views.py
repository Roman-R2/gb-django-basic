import json
from urllib.request import urlopen

from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    url = 'https://jsonplaceholder.typicode.com/users'
    json_response = urlopen(url)
    fake_json = json.loads(json_response.read())

    context = {
        "contacts": fake_json[:3],
    }

    return render(request, 'mainapp/contact.html', context=context)
