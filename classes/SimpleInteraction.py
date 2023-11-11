from .Interaction import Interaction
from utils import printText

class SimpleInteraction(Interaction):
    def __init__(self, text, textSecond = None, execute = None):
        if execute == None:
            execute = lambda : None
        if textSecond == None:
            textSecond = text
        super().__init__()
        self.text = text
        self.textSecond = textSecond
        self.execute = execute

    def act(self):
        if self.text is not None:
            printText(self.text)
            self.execute()

    def act_after(self):
        if self.textSecond is not None:
            printText(self.textSecond)