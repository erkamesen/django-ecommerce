from pytest_factoryboy import register
from rest_framework.test import APIClient
import pytest
from django.urls import reverse
from core.tests.factories import (
    CategoryFactory,
    BrandFactory,
    ProductFactory,
    CustomUserFactory
)


pytestmark = pytest.mark.django_db

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(CustomUserFactory)


@pytest.fixture
def client() -> APIClient:
    return APIClient
