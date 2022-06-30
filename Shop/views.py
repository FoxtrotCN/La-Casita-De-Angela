from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Login Form")


def products(request):
    return HttpResponse("List of products to add by user.")