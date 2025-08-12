from src.models import Product, Category
import pytest

@pytest.fixture
def product_type():
    return Product("Smartphone", "Cool_Smartphone", 100, 14)


@pytest.fixture
def category():
    return Category("Электроника", "Различная электроника", [])

@pytest.fixture
def product_data():
    return {
        "name": "Ноутбук",
        "price": 50000,
        "quantity": 3,
        "description": "Игровой"
    }