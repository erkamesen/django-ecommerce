import pytest


@pytest.mark.django_db
class TestCategoryModel:

    def test_str_method(self, category_factory):
        category = category_factory()
        assert category.__str__().startswith("Category_")


@pytest.mark.django_db
class TestBrandModel:

    def test_str_method(self, brand_factory):
        brand = brand_factory()
        assert brand.__str__().startswith("Brand_")


@pytest.mark.django_db
class TestProductModel:

    def test_str_method(self, product_factory):
        product = product_factory()
        assert product.__str__().startswith("Product_")
