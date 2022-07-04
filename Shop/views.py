from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def index(request):
    return render(request, 'login.html')


def shop(request):
    return render(request, 'base.html')


def products(request):
    products = Product.objects.all()
    # print(products)
    return render(request, 'products/index.html', {'products': products})


def main(request):
    return render(request, 'products/main.html')


def make_products(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'products/make.html', {'form': form})


def edit_products(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('products')

    return render(request, 'products/edit.html', {'form': form})


def delete_products(request, id=id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('products')
