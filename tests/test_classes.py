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
    return Product('киндер сюрприз', 'молочный шоколад, внутри игрушка', 120.2, 33)

@pytest.fixture()
def test_product_int_price():
    return Product('киндер сюрприз', 'молочный шоколад, внутри игрушка', 120, 33)


@pytest.fixture()
def test_category_check_counts():
    return Category('Шоколадная продукция', 'продукция из фабрики уилли уонка', ['снукерс', 'киндер сюрприз'])


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

def test_category_counts(test_category_check_counts):
    '''чекаем корректность работы счетчиков. не знаю насколько неоходимо, на всякий случай'''
    assert test_category_check_counts.categories_count == 1
    assert test_category_check_counts.unique_products_count == 2
