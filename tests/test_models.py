import pytest

from src.models import Category, Product

sample_products = [
    Product("Product1", "Descript1", 100, 5),
    Product("Product2", "Descript2", 200, 3),
]


def test_init_products(product_type) -> None:
    assert product_type.name == "Smartphone"
    assert product_type.description == "Cool_Smartphone"
    assert product_type.price == 100
    assert product_type.quantity == 14


@pytest.mark.parametrize(
    "name,description,products,expected_name,expected_desc,expected_len,expected_cat_count,expected_prod_count",
    [
        # Тест 1: Обычная категория с продуктами
        (
            "Electronics",
            "Tech gadgets",
            sample_products,
            "Electronics",
            "Tech gadgets",
            2,
            1,
            2,
        ),
        # Тест 2: Категория без продуктов
        ("Books", "Reading materials", [], "Books", "Reading materials", 0, 1, 0),
        # Тест 3: Категория с одним продуктом
        (
            "Food",
            "Delicious items",
            [sample_products[0]],
            "Food",
            "Delicious items",
            1,
            1,
            1,
        ),
        # Тест 4: Пустое название категории
        ("", "No name category", [], "", "No name category", 0, 1, 0),
    ],
)
def test_category_creation(
    name,
    description,
    products,
    expected_name,
    expected_desc,
    expected_len,
    expected_cat_count,
    expected_prod_count,
):
    # Создаю категорию
    category = Category(name, description, products)

    # Проверяю атрибуты
    assert category.name == expected_name
    assert category.description == expected_desc
    assert len(category.product) == expected_len

    # Проверяю счетчики категорий и продуктов
    # print(Category.category_count, expected_cat_count)
    # print(Category.product_count, expected_prod_count)
    assert Category.category_count == expected_cat_count
    assert Category.product_count == expected_prod_count

    # Обнуляю счётчики перед следующим тестом
    Category.category_count = 0
    Category.product_count = 0


def test_add_new_product(category, product_data, capsys):

    # Создание категории 'Электроника'
    category_electronika = category

    # Добавление нового товара в категорию.
    product = Product.new_product(product_data)
    category_electronika.add_product(product)

    """
    print()
    print(category_electronika.name)
    print(product.name)"""

    assert len(category.product) == 1
    assert category.product[0].name == "Ноутбук"
    assert category.product[0].description == "Игровой"

    # Пробую поменять цену на нулевую
    product.set_price(0)
    captured = capsys.readouterr()
    assert captured.out == "\nЦена не должна быть нулевая или отрицательная\n"
