from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')

        else:
            messages.success(request, ("There was an error Login In, Try again."))
            return redirect('/')


    else:
        return render(request, 'authentication/login.html', {})


def log_out(request):
    logout(request)
    return redirect('main')


@login_required
def shop(request):
    return render(request, 'base.html')


@login_required
def products(request):
    products = Product.objects.filter(user=request.user)

    return render(request, 'products/index.html', {'products': products})


@login_required
def main(request):
    return render(request, 'products/main.html')


@login_required
def make_products(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        product = form.save()
        product.user = request.user
        product.save()
        return redirect('products')
    return render(request, 'products/make.html', {'form': form})


@login_required
def edit_products(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('products')

    return render(request, 'products/edit.html', {'form': form})


@login_required
def delete_products(request, id=id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('products')
