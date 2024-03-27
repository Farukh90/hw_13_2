from src.Product_cls import Product


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
            raise TypeError('можно складывать только со смартфонами')
