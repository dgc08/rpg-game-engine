from resources.lang import sys_constants
from . import Interaction
from resources.rooms import rooms

class Sys(Interaction.Interaction):

    def __init__(self):
        super().__init__()
        self.player = []
        self.player_data = {}
        self.rooms = rooms
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
