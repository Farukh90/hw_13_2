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