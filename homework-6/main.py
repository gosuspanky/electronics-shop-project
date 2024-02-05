from src.item import Item
from config import SRC_DIR

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    # Item.instantiate_from_csv("item.csv")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(SRC_DIR)
    # InstantiateCSVError: Файл item.csv поврежден
