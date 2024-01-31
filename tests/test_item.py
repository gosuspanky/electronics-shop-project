"""Здесь надо написать тесты с использованием pytest для модуля item.
item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    phone1.number_of_sim = 0
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля
"""
from config import DICT_DIR
from src.item import Item
from src.phone import Phone


def test_calculate_total_price():
    ex1 = Item('помидорка', 15.0, 20)
    assert ex1.calculate_total_price() == 300

    ex2 = Item('луковичок', 20.0, 1)
    Item.pay_rate = 0.8
    ex2.apply_discount()
    assert ex2.calculate_total_price() == 16.0

    ex3 = Item("Смартфон", 10000, 20)
    ex4 = Item("Ноутбук", 20000, 5)
    Item.pay_rate = 0.8
    ex3.apply_discount()
    assert ex3.price == 8_000.0
    assert ex4.price == 20_000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv(DICT_DIR)
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    item1.name = 'Телефон'
    assert item1.name == 'Телефон'

    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


phone1 = Phone("iPhone 14", 120_000, 5, 2)
item2 = Item("Смартфон", 10000, 20)


def test_add():
    assert item2 + phone1 == 25
    assert phone1 + phone1 == 10


def test_number_of_sim():
    phone1.number_of_sim = 5
    assert phone1.number_of_sim == 5


def test_exc_number_of_sim():
    phone1.number_of_sim = 0
    assert phone1.number_of_sim() == 0
