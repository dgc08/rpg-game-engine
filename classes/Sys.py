import msvcrt
from time import sleep

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
        self.tried_continue = False
        self.player_data = {}
        self.rooms = rooms
        self.room = 0

        self.player_data["inventory"] = Inventory()
        self.player_data["selected_weapon"] = Weapon("nothing", 0)
        self.player_data["max_hp"] = 20
        self.been_here = True

    def game_over(self):
        print(sys_constants.game_over)
        key = None
        while key != "r" and key != "e":
            key = msvcrt.getch().decode('utf-8')

        if key == "r":
            GameInstance(Sys())
            GameInstance().act()
        else:
            exit()

    def act(self):
        while self.room != len(self.rooms):
            if self.been_here:
                ret_sub = self.rooms[self.room].act()
                if ret_sub and self.continue_room():
                    continue
                self.been_here = False
            action = None
            while action != "c":
                sleep (0.25)
                print(sys_constants.prompt, end="", flush=True)
                action = msvcrt.getch().decode('utf-8')
                print("\n",flush=True)
                match action:
                    case "c":
                        self.continue_room()
                    case "a":
                        self.rooms[self.room].act_after()
                    case "i":
                        self.player_data["inventory"].act()
                    case "e":
                        exit()

    def continue_room(self):
        can_forward = True
        for i in self.rooms[self.room].contents:
            if type(i) == Enemy:
                if self.tried_continue:
                    print(sys_constants.there_are_enemies_special)
                    self.player_data["inventory"].append(Weapon("Founding Titan's power aka. RUMBLING", 6969))
                    self.tried_continue = False
                else:
                    print(sys_constants.there_are_enemies)
                    self.tried_continue = True
                can_forward = False
                return False
        if can_forward:
            self.room += 1
            self.been_here = True
            self.tried_continue = False
            return True
