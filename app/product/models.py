from django.db import models
from core.models import TimeStampedMixin
from mptt.models import TreeForeignKey, MPTTModel
# Create your models here.


class Category(MPTTModel):
    name = models.CharField(max_length=120)
    parent = TreeForeignKey("self", on_delete=models.SET_NULL,
                            null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name", ]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(TimeStampedMixin):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,
                              related_name="products")
    category = TreeForeignKey(Category, related_name="products",
                              on_delete=models.SET_NULL,
                              null=True, blank=True)

    def __str__(self):
        return self.name
