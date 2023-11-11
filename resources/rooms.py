from GameInstance import GameInstance
from classes.Room import Room
from classes.SimpleInteraction import SimpleInteraction
from classes.Weapon import Weapon

rooms =  []

rooms.append([Room([SimpleInteraction("e"),
               SimpleInteraction("You got stuff hehe", "", lambda: (GameInstance().player.append(Weapon("Weapon 1", 1, 5)),
                                                                    GameInstance().player.append(Weapon("Weapon 2", 2, 7))))], "stay")])