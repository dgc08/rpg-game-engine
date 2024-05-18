from resources.src.Code import Code

from GameInstance import GameInstance
from utils import printText
from classes.Fight import Enemy
from classes.Item import Item
from classes.Room import Room
from classes.SimpleInteraction import SimpleInteraction
from classes.Weapon import Weapon

def on_start():
    printText ("Hello from RPG text-based game engine. Enjoy the default game!!;")

# Custom Function
def set_lives():
    GameInstance().player_data["max_hp"] = 100


rooms = [Room([
        SimpleInteraction("You receive a mission briefing: Infiltrate the high-security compound and gather intel."),
        Weapon("Silenced Pistol", 8)
    ], True),

    Room([
        SimpleInteraction("You are in the courtyard. Be cautious of patrolling guards."),
        Enemy("Guard Dog", 10, 4, ["The guard dog barks menacingly.", "You narrowly dodge a fierce bite."], [], True)
    ]),

    Room([
        SimpleInteraction("You find a computer terminal. It seems to be password-protected.;"),
        Item("Note", "drawer. It seems to be important", False, lambda: print("You found a note with a code: 'Gg'."))
    ]),

    Room([
        SimpleInteraction("You encounter a guard. He seems suspicious."),
        Enemy("Suspicious Guard", 20, 10, ["The guard eyes you suspiciously.", "He makes a threatening move."],
              [Weapon("a heavy Pistol", 10, "the Guard's corpse")]),
    ]),

    Room([
        SimpleInteraction("You reach the main server room. Enter the code to access classified information."),
        Code("Computer Terminal", "Gg"),
    ]),

    Room([
        SimpleInteraction(
            "You enter the server room. You look for a computer, but you can't find one. ;Cut:1;The door shuts behind you. ; Cut:2;You turn around and see a mysterious figure."),
        SimpleInteraction(
            "Mysterious Figure: Oh, hello. What are you doing here? ;He turns the lights on; You see, its Mirki, the master behind this organization.; Mirki: You must be an agent from David E-Sports,"),
        SimpleInteraction(
            "   Stealing information from Mirki E-Sports.; Mirki: You guys are so bad at playing valorant, you are even doing economic espionage!; Cut:1;   OK, then, let's duel in Valorant.;nwenwe")
    ], True),
    Room([Weapon("a Vandal", 20, "on the ground in Valorant. Make sure to eqiup it, your normal weapons won't do much"),
          Item("a Shield", "on the ground in Valorant. Make sure to use it, or you'll be dead in notime", True,
               set_lives)]),
    Room([Enemy("Mirki with an Operator", 100, 30,
                ["I am a Valorant god!! (But pretty nerfed in this game)", "Ha you fool", "Imagine", "Gg", "Gg"], [])],
         True),

    Room([SimpleInteraction(
        "\nYou defeated Mirki. Mirki is dead.;Mirki can no longer play competetive.;Mirki E-Sports does not exist anymore because no Mirki.; Now David ESports are the best! You are rich now beaucse david gave you 69 000 $.;THE END", )],
         True),
    Room([SimpleInteraction("Cut:1;...;Cut:1; Or is it?\n")], True),
    Room([Enemy("Vsauce", 70, 30, [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "The shortest war in history was between Britain and Zanzibar in 1896, lasting only 38 to 45 minutes.",
        "Bananas are berries, but strawberries aren't. In botanical terms, berries have seeds inside, and strawberries have their seeds on the outside.",
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the iron. It contracts back in the winter.",
        "Cows have best friends and can become stressed when they are separated.",
        "The longest word without a vowel is 'rhythms.'",
        "The Great Wall of China is not visible from the Moon with the naked eye.",
        "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
        "Octopuses have three hearts: two pump blood to the gills, and one pumps it to the rest of the body.",
        "The longest time between two twins being born is 87 days.",
        "The smell of freshly-cut grass is actually a plant distress call.",
        "The world's largest desert is not the Sahara but Antarctica.",
        "A group of flamingos is called a 'flamboyance.'",
        "The oldest known recipe is for beer. It dates back to around 3,900 BCE in ancient Sumeria.",
    ], [Weapon("A terrorists Bomb", 6)], Weapon("An atomic bomb", 696969))], True),
    Room([SimpleInteraction(
        "The terrorist bomb exploded.; You are fine, but everyone else at Mirki ESports died. Vsauce turned out to be an indian terrorist.;"
        "You got a new atomic bomb so you decide to make a retalliation strike on India.;"
        "India is also a nuclear power, so they laünch nukes back on you.But their nukes are bad, so they miss and hit the US, China and Russia.;"
        "You started nuclear war between major powers. Humanity went extinct.;THE END;Cut:1;...;Cut:1;Or is it?;Ok no it's the end; bai bai uwu")],
         True)

]
