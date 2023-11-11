class Item:
    def __init__(self, name):
        self.name = name

    def use(self):
        pass

    def __str__(self):
        return self.name