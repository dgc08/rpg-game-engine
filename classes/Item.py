from classes.Interaction import Interaction
from resources.lang.sys_constants import where_default, you_found
from utils import printText
from GameInstance import GameInstance


class Item (Interaction):
    def __init__(self, name, where=where_default, gets_used = True, use_lambda = lambda: None):
        super().__init__()
        self.use_lambda = use_lambda
        self.gets_used = gets_used
        self.where = where
        self.name = name

    def use(self, inventory_container):
        if self.gets_used:
            inventory_container.remove(self)
        self.use_lambda()

    def __str__(self):
        return self.name

    def act(self):
        printText(you_found.format(**vars(self)))
        GameInstance().rooms[GameInstance().room].contents.remove(self)
        GameInstance().player_data["inventory"].append(self)
