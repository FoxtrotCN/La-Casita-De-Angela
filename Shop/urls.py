from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  path('register/', views.register_page, name="register"),
                  path('', views.login_user, name="index"),
                  path('logout', views.log_out, name="log_out"),
                  path('shop/', views.shop, name="shop"),
                  path('products/', views.products, name="products"),
                  path('main/', views.main, name="main"),
                  path('make/', views.make_products, name="make"),
                  path('edit/', views.edit_products, name="edit"),
                  path('delete/<int:id>', views.delete_products, name="delete"),
                  path('products/edit/<int:id>', views.edit_products, name="edit")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
