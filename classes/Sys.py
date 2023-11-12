import msvcrt

from GameInstance import GameInstance
from resources.lang import sys_constants
from . import Interaction
from resources.rooms import rooms
from classes.Inventory import Inventory
from .Fight import Enemy
from .Item import Item
from .Weapon import Weapon


class Sys(Interaction.Interaction):

    def __init__(self):
        super().__init__()
        self.player_data = {}
        self.rooms = rooms
        self.room = 0

        self.player_data["inventory"] = Inventory()
        self.player_data["selected_weapon"] = None
        self.player_data["max_hp"] = 20
        self.been_here = True

    def game_over(self):
        print(sys_constants.game_over)
        key = None
        while key != "r" or "e":
            key = msvcrt.getch().decode('utf-8')

        if key == "r":
            GameInstance(Sys())
            GameInstance().act()
        else:
            exit()

    def act(self):
        while self.room != len(self.rooms):
            if self.been_here:
                self.rooms[self.room].act()
                self.been_here = False
            action = None
            while action != "c":
                action = input(sys_constants.prompt)
                match action:
                    case "c":
                        can_forward = True
                        for i in self.rooms[self.room].contents:
                            if type(i) == Enemy:
                                print(sys_constants.there_are_enemies)
                                self.player_data["inventory"].append(Weapon("Founding Titan's power aka. RUMBLING", 6969))
                                can_forward = False
                        if can_forward:
                            self.room += 1
                            self.been_here = True
                    case "a":
                        self.rooms[self.room].act_after()
                    case "i":
                        self.player_data["inventory"].act()
                    case "e":
                        exit()
