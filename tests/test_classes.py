import pytest
from src.classes import Category
from src.classes import Product


@pytest.fixture()
def test_category_without_list():
    return Category('Шоколадная продукция', 'продукция из фабрики уилли уонка')


@pytest.fixture()
def test_category_with_list():
    return Category('Шоколадная продукция', 'продукция из фабрики уилли уонка', ['снукерс', 'киндер сюрприз'])


@pytest.fixture()
def test_product_float_price():
    return Product('киндер сюрприз', 'молочный шоколад, внутри игрушка', 120.2, 33, 'red')


@pytest.fixture()
def test_product_int_price():
    return Product('киндер сюрприз', 'молочный шоколад, внутри игрушка', 120, 33, 'red')


@pytest.fixture()
def test_category_check_counts():
    test_prod_1 = Product('test1', 'something', 33.33, 333, 'red')
    test_prod_2 = Product('test2', 'something', 32.3, 222, 'red')
    test_prod_3 = Product('test2', 'something', 32.3, 222, 'red')
    categ = Category('Шоколадная продукция', 'продукция из фабрики уилли уонка', [test_prod_1, test_prod_2])
    categ.add_products(test_prod_3)
    return Category


@pytest.fixture()
def reset_category_counts():
    Category.categories_count = 0
    Category.unique_products_count = 0


@pytest.fixture()
def test_get_prod_list():
    test_prod_1 = Product('test1', 'something', 33.33, 333, 'white')
    test_prod_2 = Product('test2', 'something', 32.3, 222, 'white')
    test = Category('Шоколадная продукция', 'продукция из фабрики уилли уонка', [test_prod_1, test_prod_2])
    return test.print_products


@pytest.fixture()
def test_price_set():
    return Product('test1', 'something', 33.33, 333, 'red')


@pytest.fixture()
def test_add_products():
    test_prod_1 = Product('test1', 'something', 33.33, 333, 'red')
    test_prod_2 = Product('test2', 'something', 32.3, 222, 'red')
    test = Category('Шоколадная продукция', 'продукция из фабрики уилли уонка')
    add_prod = test.add_products(test_prod_1, test_prod_2)
    return test


@pytest.fixture()
def total_price():
    prod_1 = Product('test1', 'something', 10, 2, 'red')
    prod_2 = Product('test2', 'something', 5, 3, 'red')
    return prod_1 + prod_2


@pytest.fixture()
def test_total_products():
    test_prod_1 = Product('test1', 'something', 33.33, 333, 'red')
    test_prod_2 = Product('test2', 'something', 32.3, 222, 'red')
    test = Category('Шоколадная продукция', 'продукция из фабрики уилли уонка', [test_prod_1, test_prod_2])
    return len(test)


def test_init_without_list(test_category_without_list):
    '''инициализация без аргумента списка с продуктами'''
    assert test_category_without_list.name == 'Шоколадная продукция'
    assert test_category_without_list.description == 'продукция из фабрики уилли уонка'


def test_init_with_list(test_category_with_list):
    '''инициализация с аргументом список с продуктами'''
    assert test_category_with_list.name == 'Шоколадная продукция'
    assert test_category_with_list.description == 'продукция из фабрики уилли уонка'
    assert test_category_with_list.products == ['снукерс', 'киндер сюрприз']


def test_init_float_price(test_product_float_price):
    '''инициализация с аргументом стоимость - флоат'''
    assert test_product_float_price.name == 'киндер сюрприз'
    assert test_product_float_price.description == 'молочный шоколад, внутри игрушка'
    assert test_product_float_price.price == 120.2
    assert test_product_float_price.in_stock == 33


def test_init_int_price(test_product_int_price):
    '''инициализация с интовым аргументом стоимость '''
    assert test_product_int_price.name == 'киндер сюрприз'
    assert test_product_int_price.description == 'молочный шоколад, внутри игрушка'
    assert test_product_int_price.price == 120
    assert test_product_int_price.in_stock == 33


def test_category_counts(reset_category_counts, test_category_check_counts):
    '''чекаем корректность работы счетчиков. не знаю насколько неоходимо, на всякий случай'''
    assert test_category_check_counts.categories_count == 1
    assert test_category_check_counts.unique_products_count == 3


def test_get_formatted_product_list(test_get_prod_list):
    assert test_get_prod_list == 'test1, 33.33 руб. Остаток: 333 шт.\ntest2, 32.3 руб. Остаток: 222 шт.'


def test_prices(test_price_set):
    test_price_set.price = 0
    assert test_price_set.price == 33.33
    test_price_set.price = -11
    assert test_price_set.price == 33.33
    test_price_set.price = 1
    assert test_price_set.price == 1


def test_add_product(test_add_products):
    assert len(test_add_products.products) == 2


def test_total_price_of_prod(total_price):
    assert total_price == 35


def test_test_total_products(test_total_products):
    assert test_total_products == 555
