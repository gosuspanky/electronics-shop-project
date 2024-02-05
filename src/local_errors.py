class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = "Файл item.csv поврежден"

    def __str__(self):
        return self.message
