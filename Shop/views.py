from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'login.html')


def shop(request):
    return render(request, 'base.html')


def products(request):
    return render(request, 'products/index.html')


def main(request):
    return render(request, 'products/main.html')


def make_products(request):
    return render(request, 'products/make.html')
