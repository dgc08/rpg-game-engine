from GameInstance import GameInstance
from classes.Code import Code
from classes.Fight import Enemy
from classes.Item import Item
from classes.Room import Room
from classes.SimpleInteraction import SimpleInteraction
from classes.Weapon import Weapon

def set_lives():
    GameInstance().player_data["max_hp"] = 100

rooms = [

    Room([
        SimpleInteraction("You receive a mission briefing: Infiltrate the high-security compound and gather intel."),
        Weapon("Silenced Pistol", 8)
    ], True),

Room([
        SimpleInteraction("You are in the courtyard. Be cautious of patrolling guards."),
        Enemy("Guard Dog", 10, 4, ["The guard dog barks menacingly.", "You narrowly dodge a fierce bite."])
    ]),

    Room([
        SimpleInteraction("You find a computer terminal. It seems to be password-protected.;"),
        Item("Note with Code", "drawer", False, lambda: print("You found a note with a code: 'Blue Eagle'."))
    ]),

    Room([
        SimpleInteraction("You encounter a guard. He seems suspicious."),
        Enemy("Suspicious Guard", 15, 10, ["The guard eyes you suspiciously.", "He makes a threatening move."], [Weapon("a heavy Pistol", 10, "the Guard's corpse")]),
    ]),

    Room([
        SimpleInteraction("You reach the main server room. Enter the code to access classified information."),
        Code("Computer Terminal", "Blue Eagle"),
    ]),

    Room([
        SimpleInteraction("You enter the server room. You look for a computer, but you can't find one. ;Cut:1;The door shuts behind you. ; Cut:2;You turn around and see a mysterious figure."),
        SimpleInteraction("Mysterious Figure: Oh, hello. What are you doing here? ;He turns the lights on; You see, its Mirki, the master behind this organization.; Mirki: You must be an agent from David E-Sports,"),
        SimpleInteraction("   Stealing information from Mirki E-Sports.; Mirki: You guys are so bad, you are even doing economic espionage!; Cut:1;   OK, then, let's duel in Valorant.;Cut:5;nwenwe")
    ], True),
    Room([Weapon("a Vandal", 20000, "on the ground in Valorant. Make sure to eqiup it, your normal weapons won't do much"),
          Item("a Shield", "on the ground in Valorant. Make sure to use it, or you'll be dead in notime", True, set_lives)]),
    Room([Enemy("Mirki with a Operator", 150, 30, ["I am a Valorant god!! (But pretty nerfed in this game)", "Ha you fool", "Imagine", "Gg", "Gg"], [])], True),
    Room([SimpleInteraction("\nYou defeated Mirki. Mirki is dead.;Mirki can no longer play competetive.;Mirki E-Sports does not exist anymore because no Mirki.; Now David ESports are the best! You are rich now beaucse david gave you 69 000 $.;THE END",)], True)

]

