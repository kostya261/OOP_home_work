# Проект домашнего задания на SkyEng
## Описание:
Изучаем ООП.

## Установка:

1. Клонируйте репозиторий:
   [ссылка](https://github.com/kostya261/PythonProject/pull/3)
   
3. Зависимости указанные в файле: *pyproject.toml*
```
[tool.poetry]
name = "oop-home-work"
version = "0.1.0"
description = ""
authors = ["Kosarew Konstantin <kos26193@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"
poetry-core = "^2.1.3"



[tool.poetry.group.lint.dependencies]
flake8 = "^7.3.0"
black = "^25.1.0"
isort = "^6.0.1"
mypy = "^1.17.1"


[tool.poetry.group.dev.dependencies]
pytest-cov = "^6.2.1"
pytest = "^8.4.1"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## Использование:

Откройте проект например в PyCharm, найдите OOP_home_work\src, откройте файл main.py и запустите его.
По желанию можно его всячески модифицировать в рамках тестирования написанных функций.

В OOP_home_work\ описан модуль:
**models.py**, который и реализуют весь скромный функционал домашнего задания.

### models.py
В модуле models.py описаны классы *Product* и *Category*

*class Product* - описывает структуру продукта и производит инициализацию
*class Category* - описывает структуру категории продуктов и производит инициализацию

25.08.2025
*class Smartphone*  - описывает структуру класса Смартфон и производит инициализацию
*class LawnGrass*  - описывает структуру класса Трава и производит инициализацию

26.08.2025
Добавлены:
Абстрактный класс:
*BaseProduct*
И Mixin
*MixinLog* - который отображает на экране информацию о создаваемом классе продукта

Примеры использования:
```
product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

print(product1.name)
print(product1.description)
print(product1.price)
print(product1.quantity)

 smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

print(smartphone1.name)
print(smartphone1.description)
print(smartphone1.price)
print(smartphone1.quantity)
print(smartphone1.efficiency)
print(smartphone1.model)
print(smartphone1.memory)
print(smartphone1.color)

grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    
    
print(grass1.name)
print(grass1.description)
print(grass1.price)
print(grass1.quantity)
print(grass1.country)
print(grass1.germination_period)
print(grass1.color)
```
Результат:
```
Iphone 15
512GB, Gray space
210000.0
8
```

12.08.2025
Добавлены новые методы в классы Product и Category
Product:
геттер price - возвращает цену продукта
и
сеттер set_price - устанавливает новую цену продукта и проверяет что бы была не меньше нуля
добавлен классметод:
new_product - добавляет/ создает новый продукт из словаря
13.08.2025
добавлены методы:
__str__
__add__

25.08.2025
Также в новых классах смартфон и трава реализованы собственные магические методы сложения
которые складывают только продукты своей категории


Category:
геттер product - возвращает список продуктов
сеттер add_product - добавляет новый продукт
13.08.2025
добавлен метод:
__str__



## Тесты
Добавлены тестовые файлы test_models.py
которые проверяют ранее написанные функции.
В них реализованы функции:
1. test_init_products,
2. test_category_creation,
3. test_smartphone_class_init,
4. test_lawn_grass_init,
5. test_smartphone_class_add,
6. test_smartphone_class_add_incorrect_product,
7. test_lawngrass_class_add,
8. test_lawngrass_class_add_incorrect_product,
9. test_mixin_log


Тест запускается из командной строки, командой **pytest**

## Лицензия:

В данном конкретном случае вероятно её ещё нет 8-/
