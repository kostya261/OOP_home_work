import pytest

from src.models import Category, Product


@pytest.fixture
def product_type():
    return Product("Smartphone", "Cool_Smartphone", 100, 14)


@pytest.fixture
def category():
    return Category("Электроника", "Различная электроника", [])


@pytest.fixture
def product_data():
    return {"name": "Ноутбук", "price": 50000, "quantity": 3, "description": "Игровой"}


@pytest.fixture
def product_data2():
    return {"name": "Ноутбук", "price": 30000, "quantity": 14, "description": "Игровой"}
