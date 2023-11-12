from. import Interaction

class Room(Interaction.Interaction):
    def __init__(self, contents: list[Interaction], stay=False):
        super().__init__()
        self.contents = contents
        self.to_return = stay

    def act(self):
        #print(self.contents)
        for i in self.contents.copy():
            #print("act on", i)
            i.act()
        #print("done actin")
        return self.to_return

    def act_after(self):
        for i in self.contents:
            i.act_after()

        return self.to_return