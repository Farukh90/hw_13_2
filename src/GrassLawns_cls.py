from Product_cls import Product


class GrassLawns(Product):
    def __init__(self, name, description, price, in_stock, color, made_in: str, germination: int):
        super().__init__(name, description, price, in_stock, color)
        self.made_in = made_in
        self.germination = germination

    def __add__(self, other):
        if isinstance(other, GrassLawns):
            return self._price * self.in_stock + other.price * other.in_stock
        else:
            raise TypeError('можно складывать только с газонной травой ')
