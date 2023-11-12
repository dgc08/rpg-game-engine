import msvcrt

from GameInstance import GameInstance
from classes.Interaction import Interaction
from classes.Item import Item
from classes.Weapon import Weapon
from resources.lang.sys_constants import inventory_open, inventory_empty, now_equiped


class Inventory(Interaction):
    def __init__(self):
        super(Inventory, self).__init__()
        self.container = []

    def append(self, obj: Item):
        self.container.append(obj)

    def paint_options(self, position):
        if len(self.container) == 0:
            print(inventory_empty)
            return

        elements = []
        for i in range(len(self.container)):
            name = str(self.container[i])
            if type(self.container[i]) == Weapon:
                name += " (WEAPON)"
            else:
                name += " (ITEM)"

            if i == position:
                elements.append(f"[*] {name}")
            else:
                elements.append(f"[ ] {name}")

        to_paint = " | ".join(elements) + " "
        print("\r" + to_paint, end="", flush=True)

    def act(self):
        print(inventory_open, "\n")
        print(now_equiped.format(**vars(GameInstance().player_data["selected_weapon"])), "\n")
        # print(" | ".join(str(obj) for obj in self.player))
        position = 0

        key = None
        while key != "e":
            self.paint_options(position)
            key = msvcrt.getch().decode('utf-8')

            match key:
                case "a":
                    position = (position - 1) % len(self.container)
                case "d":
                    position = (position + 1) % len(self.container)
                case "q":
                    if len(self.container) == 0:
                        continue

                    print()
                    self.container[position].use(self.container)
                case "e":
                    print("\n")

    @classmethod
    def test(cls):
        class ItemT(Item):
            def use(self, inventory_container: list[Item]):
                print(f"You used {self.name}.")
                super(ItemT, self).use(inventory_container)

        i = Inventory()
        i.append(ItemT("EE"))
        i.append(ItemT("Ea"))
        i.append(ItemT("ba"))

        i.act()
