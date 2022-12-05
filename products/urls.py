from django.urls import path

from .views import (
    MakerListCreateView,
    MakerRetrieveUpdateDestroyView,
    ProductCategoryListCreateView,
    ProductCategoryRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
)

app_name = "products"
urlpatterns = [
    path(
        "",
        ProductListCreateView.as_view(),
    ),
    path(
        "<int:pk>/",
        ProductRetrieveUpdateDestroyView.as_view(),
    ),
    path(
        "categories/",
        ProductCategoryListCreateView.as_view(),
    ),
    path(
        "categories/<int:pk>/",
        ProductCategoryRetrieveUpdateDestroyView.as_view(),
    ),
    path(
        "makers/",
        MakerListCreateView.as_view(),
    ),
    path(
        "makers/<int:pk>/",
        MakerRetrieveUpdateDestroyView.as_view(),
    ),
]
