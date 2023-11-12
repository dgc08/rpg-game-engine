from GameInstance import GameInstance
from classes.Item import Item
from resources.lang import sys_constants


class Weapon(Item):
    def __init__(self, name, atk, where = None):
        if where == None:
            super().__init__(name)
        else:
            super().__init__(name,where)
        self.atk = atk

    def use(self, inventory_container):
        print(sys_constants.equip.format(**vars(self)))
        GameInstance().player_data["selected_weapon"] = self
