from rest_framework import status
from django.urls import reverse
import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCategoryAPIs:

    def test_list_categories(self, client: APIClient, category_factory):
        category_factory.create_batch(4)
        client = client()
        endpoint = reverse("category-list")

        res = client.get(endpoint)

        assert res.status_code == status.HTTP_200_OK
        assert len(res.data) == 4


@pytest.mark.django_db
class TestBrandAPIs:

    def test_list_brands(self, client: APIClient, brand_factory):
        client = client()
        endpoint = reverse("brand-list")

        res = client.get(endpoint)

        assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestProductAPIs:

    def test_list_products(self, client: APIClient, product_factory):
        client = client()
        endpoint = reverse("product-list")

        res = client.get(endpoint)

        assert res.status_code == status.HTTP_200_OK

    def test_retrieve_product(self, client: APIClient, product_factory):
        product = product_factory()
        client = client()
        endpoint = reverse("product-detail", kwargs={"product_id": product.id})

        res = client.get(endpoint)

        assert res.status_code == status.HTTP_200_OK
