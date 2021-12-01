from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

<<<<<<< HEAD
from .forms import ShopUserLoginForm
=======
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
>>>>>>> parent of bf133bd (Revert "04 django homework")


def login(request):
    login_form = ShopUserLoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainapp:index'))

    context = {
        'login_form': login_form,
    }

    return render(request, 'authapp/login.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
<<<<<<< HEAD
=======


def edit(request):
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
    context = {
        "edit_form": edit_form,
    }

    return render(request, 'authapp/edit.html', context=context)


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        register_form = ShopUserRegisterForm()
    context = {
        "register_form": register_form,
    }

    return render(request, 'authapp/register.html', context=context)
>>>>>>> parent of bf133bd (Revert "04 django homework")
