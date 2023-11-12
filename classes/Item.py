from classes.Interaction import Interaction
from resources.lang.sys_constants import where_default, you_found
from utils import printText
from GameInstance import GameInstance


class Item (Interaction):
    def __init__(self, name, where=where_default):
        super().__init__()
        self.where = where
        self.name = name

    def use(self, inventory_container):
        inventory_container.remove(self)

    def __str__(self):
        return self.name

    def act(self):
        printText(you_found.format(**vars(self)))
        GameInstance().rooms[GameInstance().room].contents.remove(self)
        GameInstance().player_data["inventory"].append(self)
