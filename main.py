from src.models import Category, Product

if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.product))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром,"
        " станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.product))
    print(category2.product)

    print(Category.category_count)
    print(Category.product_count)

    print("\nкак пример что содержится в классе category1:\n")
    for product in category1.product:
        print(f"Название: {product.name}")
        print(f"Описание: {product.description}")
        print(f"Цена: {product.price}")
        print("-----")

    prod3 = Product("Androider 13", "Круче Супер Крутого крутого телефона",
                    30_000, 15)
    category1.add_product(prod3)

    # Данные товара в виде словаря
    product_data = {
        "name": "Ноутбук",
        "price": 50000,
        "description": "Игровой ноутбук с RTX 3060",
        "quantity": 10,
    }

    laptop_1 = Product.new_product(product_data)

    category2.add_product(laptop_1)

    print()
    for product in category2.product:
        print(f"Название: {product.name}")
        print(f"Описание: {product.description}")
        print(f"Цена: {product.price}")
        print("-----")

    prod3.set_price(0)
    #    prod3.set_price(20000)
    print(prod3.price)

    # 15.1
    print()
    print("_____Домашнее задание 15.1______")

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        " но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.product)
    # ^____ этот момент я не понял, что от меня требуется.
    # точнее Герман ИИ объяснил, что должно вывести названия этих продуктов
    # но тогда не будет выводиться
    # Смартфоны, количество продуктов: 7 шт.    ????
    # опять же я не понял, что именно должна вывести данная строка в категории.
    # колличество всех продуктов на складе или число внесенных продуктов

    # print()
    # for product in category1.product:
    #    print(product)

    print()
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    print("_____Домашнее задание 16.2______")

    from src.models import Product, Category

    if __name__ == '__main__':
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        print()
        """    print(product1.__repr__())
        print(product2.__repr__())
        print(product3.__repr__())
        print()
        """

        print(product1.name)
        print(product1.description)
        print(product1.price)
        print(product1.quantity)

        print(product2.name)
        print(product2.description)
        print(product2.price)
        print(product2.quantity)

        print(product3.name)
        print(product3.description)
        print(product3.price)
        print(product3.quantity)

        category1 = Category("Смартфоны",
                             "Смартфоны, как средство не только коммуникации, "
                             "но и получения дополнительных функций для удобства жизни",
                             [product1, product2, product3])

        print(category1.name == "Смартфоны")
        print(category1.description)
        print(len(category1.product))
        print(category1.category_count)
        print(category1.product_count)

        print()

        product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        #    print(product4.__repr__())
        category2 = Category("Телевизоры",
                             "Современный телевизор, который позволяет наслаждаться просмотром, "
                             "станет вашим другом и помощником",
                             [product4])

        print(category2.name)
        print(category2.description)
        print(len(category2.product))
        print(category2.product)

        print(Category.category_count)
        print(Category.product_count)