import pytest
from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APIClient

from shop.models import Product

pytestmark = pytest.mark.django_db

PRODUCTS_URL = "/api/shop/products/"


@pytest.fixture
def sample_product():
    # Before test
    file = SimpleUploadedFile(
        "abc.jpg",
        b"file_content",
        "image/jpeg",
    )
    product = Product.objects.create(
        title="Product 1",
        description="Description of Product 1.",
        price=Decimal("100.00"),
        image=file,
    )

    yield product

    # After test
    product.image.delete()


def test_get_products_empty():
    # Arrange
    client = APIClient()

    # Act
    response = client.get(PRODUCTS_URL)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []


def test_get_existing_products(sample_product):
    # Arrange
    client = APIClient()

    # Act
    response = client.get(PRODUCTS_URL)

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data == [
        {
            "title": sample_product.title,
            "description": sample_product.description,
            "price": str(sample_product.price),
            "image": sample_product.image.url,
        }
    ]


def test_get_non_existing_product():
    # Arrange
    client = APIClient()

    # Act
    response = client.get(PRODUCTS_URL + "1/")

    # Assert
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == {"detail": "Not found."}


def test_get_existing_product(sample_product):
    # Arrange
    client = APIClient()

    # Act
    response = client.get(PRODUCTS_URL + "1/")

    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "title": sample_product.title,
        "description": sample_product.description,
        "price": str(sample_product.price),
        "image": sample_product.image.url,
    }
