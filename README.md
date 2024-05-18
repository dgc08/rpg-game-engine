# A simple Game Engine for text-based RPGs

This game engine allows you to create simple textadventures, which all work after the same principle:

You run games by executing the `main.py` file using a python interpreter. If you haven't changed anything, the default game will play. You can also build the python program into an executable, if you don't want to distribute the whole source code and a python interpreter. This can be done by using tools like [pyinstaller](https://pyinstaller.org/en/stable/)

All the game-specific code lies in the `resources` directory, which can and should be modified to your content.

## How games made in this engine work
You have a list of `Room`s, through which the Player progresses. These Rooms are filled with objects themselfs:
- Enemies, which you have to fight 
- Items, which include
  - Equipable Weapons, which provide ATK to the player
  Plus items, which you define and program yourself
- Interactions, for example NPCs and narrator dialogues. There is the `SimpleInteraction` class, which allows you to create dialogues fast without creating new classes
- Own game objects. All objects in rooms need to implement a few functions, which is why they all inherit the `Interaction` class.

## How to create your own game
TODO

### All core game classes and how to use them
TODO
