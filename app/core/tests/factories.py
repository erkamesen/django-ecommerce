import factory

from product.models import (
    Category,
    Brand,
    Product
)
from custom_user.models import CustomUser


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Category_{n}")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: f"Brand_{n}")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: f"Product_{n}")
    description = "test description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    name = "test name"
    email = factory.Sequence(lambda n: f"test_{n}@mail.com")
    phone = factory.Sequence(lambda n: f"+90525729484{n}")
    is_active = True
    is_verified = True
    is_admin = False
    is_staff = False
