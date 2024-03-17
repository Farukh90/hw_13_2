class Category:
    '''для работы с категориями товаров и список товаров. при инициализации если не передавать список то создаст
     пустой словарь.'''
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

    @products.setter
    def products(self, product):
        self.__products = product

    @property
    def print_products(self):
        all_products = []
        for product in self.__products:
            all_products.append(f'{product.name}, {product.price} руб. Остаток: {product.in_stock} шт.')
        return all_products

    # def __repr__(self):
    #     return f'name={self.name}, description={self.description}, products={self.__products}'


class Product:
    '''пока особо ничего не делает, может хранить только распарсинную инфу из списка словарей'''

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

#
# if __name__ == "__main__":
#
#
#     prod_1 = Product('somesome', 'aha aha', 233, 3333)
#
#     prod_2 = Product('somesome122211', 'a111ha aha', 233, 2333)
#
#     test = Category('something', 'bla bla', [prod_1, prod_2])
#
#     prod_3 = Product('somesome111', 'aha aha', 233, 3333)
#
#     test.products.append(prod_3)
#
#     prod_4 = Product.create_prod('with_cls_met', 'justtest', 222.55, 333)
#
#     test.products.append(prod_4)
#
#     new = Product.create_prod('ff', 'fffff', 110, 444)
#
#     new.price = 0
#
#     print(new.price)
#
#     print('\n'.join(test.print_products))
# print(test.print_products)

# print(test.unique_products_count)
