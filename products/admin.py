from django.contrib import admin
from .models import ProductCategory, Maker, Product

admin.site.register(ProductCategory)
admin.site.register(Maker)
admin.site.register(Product)
