Magic Isn't Free: A Game for CSCI121
by Hannah Hellerstein (hanheller)


[How to Play]:
    Please make sure all files are in the same directory. From there, open up a command terminal,
and launch 'main.py' by typing 'python3 -i main.py'.
    
    If you get lost in the labrynths (which is easy, to be fair), there are maps in a folder labeled MAPS. Be warned though: these maps do not cover how many or what types of monsters will be in a specific labrynth, it just covers items... It also shows where barracades are, but not what can break them!

[Also, don't mention that I said this, but... type in 'powerup' if you just wanna be able to get through the game, fairly effortlessly. ／人◕ ‿‿ ◕人＼]


[Notes/Forewarning]:
    This game is HEAVILY based on the series "Puella Magi Madoka Magica." Some liberties were taken, but
for the large part this game is intended to take place in the same universe, with the same rules.
Because of this, know that this game and it's source material can get disturbing. 
Puella Magi Madoka Magica resides within the Psycological Horror genre, and while I have tried 
to avoid some of the more disturbing aspects, please know that this is game is not for everyone.

[Premise]:
    Idea: I'll be using the 'Adventure' base to construct this game. I'll be taking heavy inspiration from the show
"Puella Magi Madoka Magica," in that you are a person with magical powers sent out to fight "Witches."
You will be entering complex "labrynths" to fight powerful Witches and their familiars, and uncover a plot along the way. 

[Point Breakdown]:
(Because this project has been created for a CS121 class, grading has been based on a point system. You can find the point breakdown below.)

me command - 2 points.
Added a simple 'me' or 'status' command that displays your current attributes, stats, name, health/mana, and other things. 

bigger world - 2 points.
In total, the three labrynths have 66 unique rooms.

wait command - 2 points.
Typing "wait" will have it so that the player waits 1 turn in that room.

inspect command - 2 points.
Added an 'inspect' command that lets you inspect items in your inventory, items in rooms, and NPCs in the room you are in.

drop command - 2 points.
Added the ability to drop items in your current location, so long as you have the item in your inventory.

healing items - 2 points.
Grief seeds restore mana, Candy restores HP.

player attributes - 3 points.
The player now has multiple stats. They have health, mana, attack strength, magic strength, defense, and greif. Most of those are relevant to battling, while the last is relevant to what ending you can get.

more monsters - 3 points.
Each labrynth has their own unique monsters, falling under three categories: Minions, Familiars, and Witches. This leads to 9 different monsters with their own unique stats. There are also trap monsters that are randomized yet weaker than witches.

special rooms - 3 points.
You have safe rooms (you get a free heal), boss rooms (no fleeing), and nightmare rooms (spawns powerful randomized enemies if you take the item within.)

victory condition - 3 points.
Depending on if you used your wish or not, and how high your plotawareness/grief stat are, you get different endings once you defeat the final boss.

locked doors - 3 points. 
Certian doors can only be unlocked by using the correct item on them, or by choosing the correct answer in a multiple choice question.

magic - 4 points.
Player now has access to three different types of attacking magic: Neutral, Light, and Dark. Neutral magic costs more and hits harder, but has no type strengths/disadvantages. Meanwhile, using Light-magic on a Dark-type enemy leads to increased damage, while using Light-magic on a Light-type enemy leads to decreased damage. The reverse is true for Dark-type magic.

levelling up - 4 points.
After killing a monster, a player gains EXP. After killing a number of monsters, the player can level up, with all of their stats increasing. The amount of EXP required to level up increases by each level. Levelling up does not heal the player, this is intentional.

characters - 4 points.
Two NPCs: Niva and Query. You can talk to them, and they have different things to say depending on where in the plot you are.

helper - 4 points.
Kyuubey. Gives advice, can use him to use up your wish at a cost. 



Total: 43

------

Thanks to:
Jacob Smith, my friend and guy who helped me through my constant whining over this project.
The students and teachers for the CSCI121 class at reed, spring 2018.
http://patorjk.com, for giving me text art to work with. 




