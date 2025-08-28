import pytest

from src.models import Category, Product, Smartphone

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
    "name,description,products,expected_name,expected_desc,"
    "expected_len,expected_cat_count,expected_prod_count",
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
    """    print()
    print()
    print(">>>>")
    print(captured.strip().split("\n"))
    print("<<<<")
    print()
    print()"""
    assert (
        captured.out.split("\n")[2] == "Цена не должна быть нулевая или отрицательная"
    )


def test_add_product(product_data, product_data2):
    prod1 = Product.new_product(product_data)
    prod2 = Product.new_product(product_data2)

    res = prod1 + prod2
    assert res == 570000

    res = prod1 + prod1
    assert res == 300000

    res = prod2 + prod2
    assert res == 840000


def test_str_product(product_data, capsys):
    prod1 = Product.new_product(product_data)
    print(prod1)
    captured = capsys.readouterr()
    assert captured.out.split("\n")[1] == "Ноутбук, 50000 руб. Остаток 3"


def test_str_category(category, product_data, capsys):
    category_electronika = category

    # Добавление нового товара в категорию.
    product = Product.new_product(product_data)
    category_electronika.add_product(product)

    print(category_electronika)
    captured = capsys.readouterr()
    assert captured.out.split("\n")[1] == "Электроника, количество продуктов: 3 шт."


def test_smartphone_class_init(product_data3):
    assert product_data3.name == "Samsung Galaxy S23 Ultra"
    assert product_data3.description == "256GB, Серый цвет, 200MP камера"
    assert product_data3.price == 180000.0
    assert product_data3.quantity == 5
    assert product_data3.memory == 95.5
    assert product_data3.model == "S23 Ultra"
    assert product_data3.efficiency == 256
    assert product_data3.color == "Серый"


def test_lawn_grass_init(product_data4):
    assert product_data4.name == "Газонная трава"
    assert product_data4.description == "Элитная трава для газона"
    assert product_data4.price == 500.0
    assert product_data4.quantity == 20
    assert product_data4.country == "Россия"
    assert product_data4.germination_period == "7 дней"
    assert product_data4.color == "Зеленый"


def test_smartphone_class_add(product_data3, product_data3_1):
    assert product_data3 + product_data3_1 == 2580000.0


def test_smartphone_class_add_incorrect_product(product_data3, product_data4):
    with pytest.raises(TypeError):
        result = product_data3 + product_data4
        print(result)


def test_lawngrass_class_add(product_data4, product_data4_1):
    assert product_data4 + product_data4_1 == 16750.0


def test_lawngrass_class_add_incorrect_product(product_data4, product_data3_1):
    with pytest.raises(TypeError):
        result = product_data4 + product_data3_1
        print(result)


def test_mixin_log(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )
    Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    captured = capsys.readouterr()
    assert (
        captured.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    )


def test_middle_price_with_products():
    """Тест средней цены с товарами."""
    product1 = Product("Товар1", "Описание1", 100, 2)
    product2 = Product("Товар2", "Описание2", 200, 3)
    category = Category("Тест", "Тестовая", [product1, product2])

    assert category.middle_price() == 400.0


def test_middle_price_single_product():
    """Тест средней цены с одним товаром."""
    product = Product("Товар", "Описание", 500, 1)
    category = Category("Тест", "Тестовая", [product])

    assert category.middle_price() == 500.0


def test_middle_price_empty_category():
    """Тест средней цены пустой категории."""
    category = Category("Пустая", "Нет товаров", [])

    assert category.middle_price() == 0.0


def test_middle_price_zero_price():
    """Тест средней цены с товаром нулевой цены."""
    product1 = Product("Товар1", "Описание1", 0, 2)
    product2 = Product("Товар2", "Описание2", 100, 1)
    category = Category("Тест", "Тестовая", [product1, product2])

    assert category.middle_price() == 50.0


def test_product_zero_quantity(capsys):
    """Тест создания продукта с нулевым количеством."""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен!"
    ):
        Product("Товар1", "Описание1", 1000, 0)


def test_product_negative_quantity():
    """Тест создания продукта с отрицательным количеством."""
    with pytest.raises(ValueError) as exc_info:
        Product("Товар1", "Описание1", 1000, -5)

    assert "Товар с нулевым количеством не может быть добавлен!" in str(exc_info.value)
