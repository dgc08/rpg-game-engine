from classes.Item import Item

class Weapon (Item):
    def __init__(self, name, range, atk):
        super().__init__(name)
        self.range = range
        self.atk = atk