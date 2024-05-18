from classes.Sys import Sys
from GameInstance import GameInstance

GameInstance(Sys())  # GameInstance is a Singleton Provider (Makes sure every class can access the Player and stuff)
# Sys is main class

GameInstance().act()  # Without any argument, GameInstance returns what it was given last,
# in that case the game main class, and the game gets started
