from django.contrib import admin
from product.models import Category, Brand, Product
# Register your models here.


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)