from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.index),
    path('shop/', views.shop, name="shop"),
    path('products/', views.products, name="products"),
    path('main/', views.main, name="main"),
    path('make/', views.make_products, name="make"),
    path('edit/', views.edit_products, name="edit")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
