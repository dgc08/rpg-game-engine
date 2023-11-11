from. import Interaction

class Room(Interaction.Interaction):
    def __init__(self, contents: list[Interaction], to_return=None):
        super().__init__()
        self.contents = contents
        self.to_return = to_return

    def act(self):
        for i in self.contents:
            i.act()
        return self.to_return

    def act_after(self):
        for i in self.contents:
            i.act_after()