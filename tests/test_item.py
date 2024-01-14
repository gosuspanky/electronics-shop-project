"""Здесь надо написать тесты с использованием pytest для модуля item."""
from config import DICT_DIR
from src.item import Item


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


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
