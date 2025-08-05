class Product:
    """Class описывает продукт: его имя, описание, цена, количество"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Class описывает категорию продукта: имя категории, описание категории и список продуктов"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        # Обновляем счетчики
        Category.category_count += 1
        Category.product_count += len(products)
