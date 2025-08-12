class Product:
    """Class описывает продукт: его имя, описание, цена, количество"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """
        возвращает цену продукта
        :return: integer
        """
        return self.__price

    def set_price(self, new_price):
        """
        Устанавливает новую цену продукта.

        :param new_price: - новая цена продукта
        :return:
        """
        if new_price <= 0:
            print(f"\nЦена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            ask = input(
                f"\nУстанавливаемая цена ниже. Продолжить? y (значит Да): "
            ).lower()
            if ask != "y":
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Создаёт новый продукт из словаря.

        :param product_data: Словарь с ключами name, price, description, quantity.
        :return: Объект класса Product.
        """
        return cls(
            name=product_data["name"],
            price=product_data["price"],
            description=product_data["description"],
            quantity=product_data["quantity"],
        )


class Category:
    """Class описывает категорию продукта: имя категории, описание категории и список продуктов"""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        # Обновляем счетчики
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def product(self) -> list:
        """
        возвращает список продуктов
        :return: list
        """
        return self.__products

    def add_product(self, product):
        """
        Добавляет новый продукт в список продуктов данной категории
        :param product: класс Product
        :return:
        """
        self.__products.append(product)

