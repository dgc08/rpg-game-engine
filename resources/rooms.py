# from GameInstance import GameInstance
from classes.Fight import Enemy
from classes.Room import Room
from classes.SimpleInteraction import SimpleInteraction
from classes.Weapon import Weapon

rooms = [Room([SimpleInteraction("e"),
               Weapon("Weapon 1", 5),
               Weapon("Weapon 2", 7)],
              # SimpleInteraction("You got stuff hehe", "",
              #                  lambda: (GameInstance().player_data.inventory.append(),
              #                           GameInstance().player_data.inventory.append(Weapon("Weapon 2", 2, 7))))],
              True),
         Room([Enemy("maballs", 15, 10, ["amabatakaam", "bals"])]),
         Room([SimpleInteraction("You won. Epic; bye bye; its over; just like aot 😢")], True)
         ]
