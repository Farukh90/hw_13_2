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
        self.__products.extend(args)

    @property
    def print_products(self):
        all_products = []
        for product in self.__products:
            all_products.append(f'{product.name}, {product.price} руб. Остаток: {product.in_stock} шт.')
        return all_products

    def __repr__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.in_stock} шт.'


class Product:
    '''хранение информации о товаре'''

    def __init__(self, name: str, description: str, price: float, in_stock: int):
        self.name = name
        self.description = description
        self._price = price
        self.in_stock = in_stock

    # def __repr__(self):
    #     return f'{self.name}, {self.description}'

    @classmethod
    def create_prod(cls, name: str, description: str, _price: float, in_stock: int):
        return cls(name, description, _price, in_stock)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('введена некорректная цена')
        else:
            self._price = new_price


