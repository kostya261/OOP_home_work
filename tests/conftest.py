import pytest

from src.models import Category, LawnGrass, Product, Smartphone


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


@pytest.fixture
def product_data3():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def product_data3_1():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture
def product_data4():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def product_data4_1():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
