from GameInstance import GameInstance
from classes.Fight import Enemy


class Code(Enemy):
    def __init__(self, name, correct):
        self.name = name
        self.correct = correct

    def act(self):
        inp = input("Enter code: ")
        if inp == self.correct:
            print("Access granted.")
            GameInstance().rooms[GameInstance().room].contents.remove(self)
        else:
            print("Incorrect code. Try again.")
