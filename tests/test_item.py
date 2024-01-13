"""Здесь надо написать тесты с использованием pytest для модуля item."""

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

