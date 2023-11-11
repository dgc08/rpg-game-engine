from classes.Interaction import Interaction
from utils import printText
from .utils import attack
from resources.lang import fight


class Enemy(Interaction):
    def __init__(self, player_hp: int, player_atk: int, name: str, hp: int, atk: int, voicelines: list[str], loop_voicelines = False):
        super(Enemy, self).__init__()
        self.player_atk = player_atk
        self.name = name
        self.loop_voicelines = loop_voicelines
        self.player_hp = player_hp
        self.hp = hp
        self.atk = atk
        self.voicelines = voicelines

    def act(self):
        return self.fight()

    def fight(self):
        round = 0

        printText(fight.enemy_attacks.format(**vars(self)))
        while self.player_hp >= 0 and self.hp >= 0:
            if len(self.voicelines) != 0 and (round < len(self.voicelines) or self.loop_voicelines):
                printText(self.voicelines[round % len(self.voicelines)])

            # PLAYER_ATTACK
            printText(fight.your_turn.format(**vars(self)))
            dmg_mul = attack() +  1 # From 1-200
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
            printText(fight.enemy_turn.format(**vars(self)))
            dodge_efficiency = attack() + 1  # Assume attack() is a function that returns a value from 1 to 200

            if dodge_efficiency > 20:
                enemy_dmg = self.atk
            else:
                enemy_dmg = self.atk / (dodge_efficiency * 0.9)

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
            return True
        else:
            printText(fight.you_loose)
            return False


    @staticmethod
    def module_test():
        Enemy(40, 5, "maballs", 15, 10, ["amabatakaam", "bals"]).act()