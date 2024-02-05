import csv
from local_errors import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            print('Длина наименования товара превышает 10 символов.')
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        cls.all.clear()

        try:
            with open(csvfile, encoding="windows-1251") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

        try:
            for data in reader:

                name = str(data['name'])
                price = float(data['price'])
                quantity = int(data['quantity'])

                cls(name, price, quantity)

        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(some_num):
        return int(float(some_num))

