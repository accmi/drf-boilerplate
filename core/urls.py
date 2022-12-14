from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("appauth.urls", namespace="appauth")),
    path("products/", include("products.urls", namespace="products")),
    path("users/", include("users.urls", namespace="users")),
]
