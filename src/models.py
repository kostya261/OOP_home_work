class Product:
    """Class описывает продукт: его имя, описание, цена, количество"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток {self.quantity}"

    def __add__(self, other):
        if not isinstance(other, Product):  # Проверяет класс и наследников
            raise TypeError(f"Ожидается Product, получен {type(other).__name__}")
        return self.__price * self.quantity + other.price * other.quantity

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
            print("\nЦена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            ask = input(
                "\nУстанавливаемая цена ниже. Продолжить? y (значит Да): "
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


class Smartphone(Product):
    """
    Добавляет класс Смартфоны, как дочерний от Product класса
    описывает специфику смартфонов в отличие от обычных продуктов
    """

    def __init__(
        self, name, description, price, quantity, memory, model, efficiency, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):
    """
    Добавляет класс Трава, как дочерний от Product класса
    описывает специфику продукта Трава в отличие от обычных продуктов
    """

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


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

    def __str__(self):
        counter_product = 0
        for iterator in self.__products:
            counter_product += iterator.quantity

        return f"{self.name}, количество продуктов: {counter_product} шт."  # self.product_count

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
        if not isinstance(product, Product):  # Проверяет класс и наследников
            raise TypeError(f"Ожидается Product, получен {type(product).__name__}")
        self.__products.append(product)


if __name__ == "__main__":
    product = {
        "name": "Телефон 1",
        "description": "Телефон для крутых",
        "price": 50_000,
        "quantity": 12,
    }

    product2 = {
        "name": "Телефон 2",
        "description": "Телефон для не крутых",
        "price": 10_000,
        "quantity": 120,
    }

    prod1 = Product.new_product(product)
    prod2 = Product.new_product(product2)

    category_1 = Category("Смартфоны", "Крутейшие смартфоны", [prod1, prod2])

    # print(prod1)
    # print(prod2)

    print(category_1)
    print(prod1 + prod2)
