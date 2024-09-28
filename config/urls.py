from django.contrib import admin
from django.urls import path, include
# from product import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", include('product.urls')),
    path('',include('pages.urls')),
]
