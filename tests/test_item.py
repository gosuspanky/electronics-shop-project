"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_calculate_total_price():
    ex1 = Item('помидорка', 15.0, 20)
    assert ex1.calculate_total_price() == 300

    ex2 = Item('луковичок', 20.0, 1)
    Item.pay_rate = 0.8
    assert ex2.calculate_total_price() == 16.0


def test_apply_discount():
    ex1 = Item('морковка', 10.0, 10)
    Item.pay_rate = 0.9
    assert ex1.apply_discount() == 9.0
