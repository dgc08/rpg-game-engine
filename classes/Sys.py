from . import Interaction
from .Room import Room
from .SimpleInteraction import SimpleInteraction
from .Weapon import Weapon
from resources.lang import sys_constants


class Sys(Interaction.Interaction):
    sysob = None

    def __init__(self):
        super().__init__()
        self.player = []
        self.rooms = [Room([SimpleInteraction("e"),
               SimpleInteraction("You got stuff hehe", "", lambda: (Sys.sysob.player.append(Weapon("Weapon 1", 1, 5)), Sys.sysob.player.append(Weapon("Weapon 2", 2, 7))))], "stay")]
        self.room = 0

    def act(self):
        while self.room != len(self.rooms):
            if self.rooms[self.room].act() != "stay":
                self.room += 1
            else:
                action = None
                while action != "c":
                    action = input(sys_constants.prompt)
                    match action:
                        case "c":
                            self.room += 1
                        case "a":
                            self.rooms[self.room].act_after()
                        case "i":
                            print(" | ".join(str(obj) for obj in self.player))

    @classmethod
    def start_game(cls):
        cls.sysob = Sys()
        cls.sysob.act()