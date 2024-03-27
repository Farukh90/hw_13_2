from src.Product_cls import Product
from src.Smartphone_cls import Smartphone


class Category:
    '''Обработка категорий товаров, хранение информации о категории и товарах в категории'''
    categories_count = 0
    unique_products_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.categories_count += 1
        Category.unique_products_count += len(self.__products)

    @property
    def products(self):
        return self.__products

    def add_products(self, *args):
        for product in args:
            if isinstance(product, Product):
                self.__products.append(product)
                Category.unique_products_count += 1
            else:
                raise TypeError(f"нельзя добавить объект {product}")

    @property
    def print_products(self):
        return '\n'.join(map(str, self.__products))

    def __len__(self):
        total_stock = 0
        for el in self.__products:
            total_stock += el.in_stock
        return total_stock

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'
