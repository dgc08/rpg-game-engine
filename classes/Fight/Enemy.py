from GameInstance import GameInstance
from classes.Interaction import Interaction
from utils import printText
from .utils import attack
from resources.lang import fight
from ..Item import Item


class Enemy(Interaction):
    def __init__(self, name: str, hp: int, atk: int, voicelines: list[str] = [], loot: list[Item] = [],
                 loop_voicelines=False, player_hp: int = None, player_atk: int = None):
        super(Enemy, self).__init__()

        self.loot = loot
        self.player_atk = player_atk
        self.name = name
        self.loop_voicelines = loop_voicelines
        self.player_hp = player_hp
        self.hp = hp
        self.atk = atk
        self.voicelines = voicelines

    def act(self):
        printText("\033[91m" + fight.enemy_attacks.format(**vars(self)) + "\033[0m")
        if self.player_hp is None or self.player_atk == None:
            self.player_hp = GameInstance().player_data["max_hp"]
            if GameInstance().player_data["selected_weapon"].atk == 0:
                print(fight.no_weapon)
                return
            else:
                self.player_atk = GameInstance().player_data["selected_weapon"].atk

        return self.fight()

    def fight(self):
        round = 0

        while self.player_hp >= 0 and self.hp >= 0:

            # PLAYER_ATTACK
            printText(fight.your_turn.format(**vars(self)))
            dmg_mul = attack() + 1  # From 1-200
            if dmg_mul > 20:
                dmg = 0
            else:
                dmg = self.player_atk / (dmg_mul * 0.9)

            print()
            if dmg_mul == 1:
                printText(fight.you_perfect.format(dmg=dmg))
            elif dmg_mul < 5:
                printText(fight.you_almost_perfect.format(dmg=dmg))
            elif dmg_mul > 20:
                printText(fight.you_miss)
            else:
                printText(fight.you_hit.format(dmg=dmg))
            self.hp -= dmg
            printText(fight.enemy_hp.format(**vars(self)))

            if self.hp <= 0:
                break

            # ENEMY_ATTACK
            if len(self.voicelines) != 0 and ((round < len(self.voicelines) or self.loop_voicelines)):
                print(f"\n\n{self.name}: " + self.voicelines[round % len(self.voicelines)] + "\n\n")
            printText(fight.enemy_turn.format(**vars(self)))
            dodge_efficiency = attack() + 1  # Assume attack() is a function that returns a value from 1 to 200

            if dodge_efficiency > 20:
                enemy_dmg = self.atk
            else:
                enemy_dmg = self.atk - (1 / dodge_efficiency * self.atk)

            print()
            if dodge_efficiency == 1:
                printText(fight.you_perfect_dodge.format(dmg=enemy_dmg))
            elif dodge_efficiency < 6:
                printText(fight.you_almost_perfect_dodge.format(dmg=enemy_dmg))
            elif dodge_efficiency > 20:
                printText(fight.you_fail_to_dodge.format(dmg=enemy_dmg))
            else:
                printText(fight.you_dodge.format(dmg=enemy_dmg))

            self.player_hp -= enemy_dmg
            printText(fight.player_hp.format(**vars(self)))

            round += 1
        if self.hp <= 0:
            printText(fight.you_won)
            if self.loot != []:
                printText(fight.get_loot.format(loot=", ".join([str(i) for i in self.loot])))
            GameInstance().rooms[GameInstance().room].contents.remove(self)
            for i in self.loot:
                GameInstance().player_data["inventory"].append(i)
        else:
            printText(fight.you_loose)
            GameInstance().game_over()

    @staticmethod
    def module_test():
        Enemy("maballs", 15, 10, ["amabatakaam", "bals"], [], False, 40, 5).act()
