class Category:
    '''для работы с категориями товаров и список товаров. при инициализации если не передавать список то создаст
     пустой словарь.'''
    categories_count = 0
    unique_products_count = 0

    def __init__(self, name:str, description:str, products:list = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.categories_count += 1
        Category.unique_products_count += len(self.products)

    # def __repr__(self):
    #     return f'name={self.name}, description={self.description}, products={self.products}'


class Product:
    '''пока особо ничего не делает, может хранить только распарсинную инфу из списка словарей'''
    def __init__(self, name: str, description : str, price: float, in_stock: int):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock


    # def __repr__(self):
    #     return self.name, self.description