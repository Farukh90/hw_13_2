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
                print(f"нельзя добавить объект {product}")

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


class Product:
    '''хранение информации о товаре'''

    def __init__(self, name: str, description: str, price: float, in_stock: int, color: str):
        self.name = name
        self.description = description
        self._price = price
        self.in_stock = in_stock
        self.color = color

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.in_stock} шт.'

    def __add__(self, other):
        return self._price * self.in_stock + other.price * other.in_stock

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


class Smartphone(Product):
    def __init__(self, name, description, price, in_stock, color, perfomance: int, model: str, storage_capacity: int):
        super().__init__(name, description, price, in_stock, color)
        self.perfomance = perfomance
        self.model = model
        self.storage_capacity = storage_capacity

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self._price * self.in_stock + other.price * other.in_stock
        else:
            raise TypeError


class GrassLawns(Product):
    def __init__(self, name, description, price, in_stock, color, made_in: str, germination: int):
        super().__init__(name, description, price, in_stock, color)
        self.made_in = made_in
        self.germination = germination

    def __add__(self, other):
        if isinstance(other, GrassLawns):
            return self._price * self.in_stock + other.price * other.in_stock
        else:
            raise TypeError



