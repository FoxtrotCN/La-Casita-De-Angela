from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shop/', views.shop, name="shop"),
    path('products/', views.products, name="products"),
    path('main/', views.main, name="main"),
    path('make/', views.make_products, name="make")

]
