from GameInstance import GameInstance
from classes.Item import Item
from resources.lang import sys_constants


class Weapon(Item):
    def __init__(self, name, atk):
        super().__init__(name)
        self.atk = atk

    def use(self, inventory_container):
        print(sys_constants.equip.format(**vars(self)))
        GameInstance().player_data["selected_weapon"] = self
