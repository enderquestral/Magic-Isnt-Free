from room import Room, safeRoom, BossRoom, nightmareRoom
from room import Barrier, quizBarrier
from player import Player, magicSpells
from item import Item
from item import progressionItem, important_note, itemToGiveNewMagic, Candy, GriefSeed
from item import GriefSeed
from monster import Monster
from monster import Minion, Familiar, Witch
from NPC import NPC, Kyuubey
import os
import updater
import time


killedwitch1 = False
killedwitch2 = False
killedwitch3 = False

#def createWorld():
#Here is where you create monsters, ect.
#10 rooms for first dungeon, 20 for 2nd, 30 for 3rd?
#Enemy types: "Dark" , "Light" , "Neutral"
#NOTE: The rooms are not supposed to connect in a sensible way. It's to show how easy it is to get lost in these labrynths. 
#Labrynth 1, 11 rooms
#path=Room("This is the path towards the maze. you draw the rooms as you pass through them. type 'map' to see the map so far. the O is you.", "This is the path in Winter", "Finally! The path out of this maze stands before you.")

d1r1= safeRoom("The starting room. The portal you used to enter has since closed. Occasionally, you see visions of the real world flicker in and out like smoke.")#Starting room. Saferoom. Talk to Niva, Kyuubey, Query here. 
d1r2 = Room("The ground bends and twists in odd ways. Looking down, you notice a large bow fused into the ground, causing the odd terrain.") 
d1r3 = Room("A giant broken sewing machine is justting out from the east wall, it's thread swaying lightly against the breeze. Smaller familiars are seen playing on it, before scurrying away.")
d1r4 = Room("Long flowing ribbons hang from the ceiling. You lightly push them out of the way as you move.")
d1r5 = Room("This room is an increasingly tall cocoon of ribbon. Scarlet ribbons are used as bridges and rope to ascend to new levels.")
d1r6 = Room("The only footing you find are large plastic spools attached to the walls, slowly rotating in different directions. The rest of the room is a pit, the bottom of which you cannot see.")
#Query hangs out here
d1r7 = Room("This room is filled with frayed fabrics, torn cloth, and knotted string. This room is dimmer than the rest of the labrynth.")
#Blockade of Fabric to get to this room
d1r8 = BossRoom("The room of the ribbon witch. The walls and floor are a patchwork of silks, yarn, and fabrics of many different colors. The witch sits in the center of the circular room.")
#Witch room
d1r9 = nightmareRoom("In the distance, you can see familiars tying bows around boxes like an assembly line. They pay you no heed.")
#Scissors on ground here
d1r10 = Room("Knitting needles hold up the cloth of the ceiling like tent poles. Sequins sparkle on the fabric like distant stars.")
#Grief seed in room 10
d1r11 = Room("This room is the size of a closet, a majority of which is used to house an opened present box. A human-sized amatureish ragdoll leans out of the box.")
#Plot-item here. Niva here. 


Room.connectRooms(d1r1, "north", d1r2, "south")
Room.connectRooms(d1r2, "east", d1r3, "west")
Room.connectRooms(d1r3, "north", d1r4, "south")
Room.connectRooms(d1r4, "north", d1r5, "south") #SPLIT
Room.connectRooms(d1r5, "north", d1r6, "south")
Room.connectRooms(d1r6, "north", d1r7, "south")#BLOCKADE OF FABRIC, NEED SCISSORS TO CUT THROUGH
Room.connectRooms(d1r7, "west", d1r8, "east") 
Room.connectRooms(d1r5, "west", d1r9, "east")
Room.connectRooms(d1r9, "west", d1r10, "east") 
Room.connectRooms(d1r10, "north", d1r11, "south") 


#Labrynth 2, 22 rooms
d2r1 = safeRoom("The starting room. This \"room\" is really just a long, tall stone hallway. Torches on the wall cut through the white fog, leading you deeper into the labrynth....")#Starting room. Saferoom. Talk to Kyuubey, Query here.
d2r2 = Room("Your steps echo as you walk along the stone floor. A giant reinforced stained glass window cuts through the fog.")
d2r3 = Room("The fog peters out, and the faint scent of smoke from abandoned pyres replaces it. The stone floor and walls are cold to the touch.")
d2r4 = Room("Pillars of marble are scattered about in this hallway with no rhyme or reason.")
d2r5 = Room("Choirs of Familiars sing music and dance endlessly. You avoid the stage in the center of the room, and the familiars pay you no mind.")
d2r6 = Room("Paintings of inhuman saints and angels leak out of their frames and onto the floor, creating a mess of colors. Whispers of confusion come from the mouths of these paintings.")
d2r7 = nightmareRoom("The room hosts a pedestal of two hands, palms reaching towards the sky. Light shines through cracks in the ceiling.") #Plot item, soul gem remains
d2r8 = Room("Windows from high above shine down sunlight. Shadows from beings moving outside sometimes block the windows.")
d2r9 = Room("Swords and weapons are plunged into the ground, cracking the stone floor and revealing the dirt underneath.")
d2r10 = Room("A large spade is broken in two, partially burried into a pit it must have had a part in digging. Other broken tools are found inside the pit, unburried.")
d2r11 = Room("A large stone gargoyle glares at you as you walk past. Stone rubble litters the ground.")
d2r12 = Room("This room has a window opened to a scene of a sunny flower field. A desk rests by the window, from which papers are scattered everywhere.") #Safe room. Plot item: rest of the note Niva was crying over.
d2r13 = safeRoom("The fog peters out. Burned confetti are stuck in the cracks between marble floor panels. Torn curtains line the walls, ushering you onwards.")
d2r14 = Room("The far wall depicts a scene of an angel, fighting off a plague of rodents. The face of the angel has been destroyed. In the area between the rats and the angel, there is a door.")
d2r15 = Room("Statues of familiars in celebration encircle the room. They all seem to be covered in a glitter that you can't remove.")
d2r16 = Room("The ceiling of this room has a chandellere, but where all the lights should be there are instead bells. It chimes as it sways in the breeze.")
d2r17 = Room("A large tree grows in far end of this room. Below it, broken toys are scattered about. ") #Query here, plot item: Musicbox explaining Niva's wish
d2r18 = Room("This room is full of blindingly bright light, brought in by stained glass windows at eye-level. The figures depicted seem to move in a mocking fashion.")
d2r19 = Room("This room is dark, pieces of shattered glass coat the floor. Torches of many colors lead onwards.")
d2r20 = Room("Towers of soggy and moldy books are scattered about the room, only enlightned by a single candle. From somewhere, you can hear water dripping in.") #Healing item here
d2r21 = Room("This room looks like an indoor garden. Flowers of all shapes, colors, and sizes grow. Vines cover the walls.")
d2r22 = BossRoom("The near and far ends of the room are connected by a long maroon carpet, the far end of which ends at the Witch, who is chained to an altar. The rest of the room houses ruined benches and broken candelabras. Occasionally, small flames and silloettes of people flicker in and out.") #Witch room

Room.connectRooms(d2r1, "north", d2r2, "south")
Room.connectRooms(d2r2, "east", d2r3, "west")#SPLIT
Room.connectRooms(d2r3, "north", d2r4, "south")
Room.connectRooms(d2r4, "north", d2r5, "south") 
Room.connectRooms(d2r5, "east", d2r6, "west")
Room.connectRooms(d2r6, "east", d2r7, "west")
Room.connectRooms(d2r6, "north", d2r8, "south") 
Room.connectRooms(d2r8, "north", d2r9, "south") 
Room.connectRooms(d2r9, "west", d2r10, "east") 
Room.connectRooms(d2r9, "north", d2r11, "south")
Room.connectRooms(d2r11, "east", d2r12, "west") 
Room.connectRooms(d2r2, "west", d2r13, "east") #Second branch of main split
Room.connectRooms(d2r13, "north", d2r14, "south")
Room.connectRooms(d2r14, "north", d2r15, "south") 
Room.connectRooms(d2r15, "west", d2r16, "east")
Room.connectRooms(d2r16, "west", d2r17, "east")
Room.connectRooms(d2r16, "north", d2r18, "south") 
Room.connectRooms(d2r18, "north", d2r19, "south") 
Room.connectRooms(d2r19, "east", d2r20, "west") 
Room.connectRooms(d2r19, "north", d2r21, "south")
Room.connectRooms(d2r21, "west", d2r22, "east")  


#Labrynth 3, 33 rooms
d3r1 = safeRoom("The starting room. The only feature is a steel door leading to stairs leading downwards. Everything else in the room is just purple brick.") #Starting room 
d3r2 = Room("A stairway leads you down, down deeper into darkness. You feel your ears pop from the change in pressure.")
d3r3 = Room("The room is an open-air alleyway. Looking up, you see a starry night sky.")
d3r4 = Room("Familiars carrying butterknives scatter as you approach. Those that can't flee glare at you from corners, but do not approach.")
d3r5 = Room("You find yourself hopping from rooftop to rooftop to chimney to semi-constructed house. The houses all look to be of poor quality.")
d3r6 = Room("The ground fades into existance one way, and in the other way it leads to a void.")
d3r7 = Room("Many smaller alleyways break off from this path. Sometimes you hear the hiss of a cat as you move past. Sometimes, the hiss sounds far more monsterous.")
d3r8 = Room("Here, the ground is shaped like a tiled and slanted rooftop. Wood creaks as you walk upon it.")
d3r9 = nightmareRoom("A projector plays a silent looping scene of a person popping up, being shot by a shadowy figure, and popping back up again. The room smells of gunpowder.") #Plot item: Paper saying Query's wish.
d3r10 = Room("Chains hang from the walls. Looking closer at the chains, you realize each link is a tiny ouroborus")
d3r11 = Room("This room contains abandoned treasures, gold, and money of all kinds. As you touch the items, they all turn into soot.")
d3r12 = Room("This dead-end room features wanted posters of varrious vague figures, all pointing to each other.")
d3r13 = Room("Chalk outlines of humanoids line the floors and walls. They seem to be paused in the middle of a dance.")
d3r14 = Room("A broken Piano plays a haunting melody as you walk past. Often keys fall out, only to float back up to their original spot.")
d3r15 = Room("Large dumpsters whisper rumors to each other. They laugh as you walk past.")
d3r16 = nightmareRoom("Garbage and trasure alike are piled on top of each other. Black cats mill about, sorting items into arbitrary categories.")
d3r17 = safeRoom("Bags of garbage line the rooms, yet there is no stench in the air. You can hear a faint singing in the distance.") #Kyuubey here. You can interrogate or even temp kill Kyuubey here. 
d3r18 = Room("In one direction, you see the lights of a city skyline at night, an ocean of distance away.")
d3r19 = Room("A large square of pure grey is painted on the ground. Your eyes start to get static if you stare at it for too long.")
d3r20 = Room("A car putters, it's engine running and it's lights on. It's so heavily damaged that it shouldn't be running.")
d3r21 = Room("An etherial, faceless woman stares at a poster on the wall of fireworks, and shakes her head. She does not pay any attention your way.")
d3r22 = Room("Two elegant stone roosters provide an archway. They alternate between glaring at you and at each other.")
d3r23 = Room("Two giant canid skulls, stacked on top of each other, take up a majority of the room. You hear a faint growling if you get too close.")
d3r24 = Room("A weather-worn sign welcomes visitors to a town, the name of which you cannot read. ")
d3r25 = Room("Thrown out evergreen trees lean against the walls. The decorations sometimes animate, but with no discernable cause.")
d3r26 = Room("Broken lightbulbs scatter the ground. One is thrown and shatters by your feet by an unseen figure.")
d3r27 = Room("A single splotlight focuses in the middle of the room, light catching the small amount of dust in the air. You cannot see the source of the light. Occasionally, it flickers.") #Safe Room
d3r28 = Room("Many abandoned or closed theatres line the road. There is only silence, and the infrequent sound of a dog or a rooster.")
d3r29 = Room("The road coils down once again, at the bottom is black marble floor with a steel door, not unlike the one you encounted at the beginning of this Labrynth.")
d3r30 = Room("A neon sign points you onwards, deeper into the labrynth. The arrow shifts into being the witches name, and back again.")
d3r31 = Room("Two shadowy bodyguards with weapons larger than a streetlamp guard the way, but run off as they see you approach.")
d3r32 = Room("You have to push through a crowd of shadowy figures, who are all whispering to each other. None of them have human-like eyes.")
d3r33 = BossRoom("Faceless crowds encircle you and the witch, whispering incompreiensible things to each other. The witch swipes at the crowds, which continuously reform after each attack.") #Witch Room

Room.connectRooms(d3r1, "north", d3r2, "south")
Room.connectRooms(d3r2, "east", d3r3, "west")
Room.connectRooms(d3r3, "east", d3r4, "west") #SPLIT 

Room.connectRooms(d3r4, "north", d3r5, "south")
Room.connectRooms(d3r5, "east", d3r6, "west")
Room.connectRooms(d3r6, "east", d3r7, "west")
Room.connectRooms(d3r7, "south", d3r8, "north")
Room.connectRooms(d3r8, "south", d3r9, "north")
Room.connectRooms(d3r8, "east", d3r10, "west")
Room.connectRooms(d3r10, "east", d3r11, "west")    
Room.connectRooms(d3r11, "north", d3r12, "south")

Room.connectRooms(d3r4, "south", d3r13, "north")
Room.connectRooms(d3r13, "south", d3r14, "north")
Room.connectRooms(d3r14, "south", d3r15, "north")#ANOTHER SPLIT
Room.connectRooms(d3r15, "east", d3r16, "west")
Room.connectRooms(d3r16, "south", d3r17, "north")

Room.connectRooms(d3r14, "east", d3r18, "west")
Room.connectRooms(d3r18, "east", d3r19, "west")#YET ANOTHER SPLIT
Room.connectRooms(d3r19, "east", d3r20, "west")
Room.connectRooms(d3r20, "east", d3r21, "west")
Room.connectRooms(d3r21, "east", d3r22, "west")

Room.connectRooms(d3r21, "south", d3r23, "north")
Room.connectRooms(d3r23, "south", d3r24, "north") #ONE MORE BRANCH

Room.connectRooms(d3r24, "west", d3r25, "east")
Room.connectRooms(d3r25, "west", d3r26, "east")
Room.connectRooms(d3r26, "south", d3r27, "north")

Room.connectRooms(d3r24, "south", d3r28, "north")
Room.connectRooms(d3r28, "east", d3r29, "west")
Room.connectRooms(d3r29, "east", d3r30, "west")
Room.connectRooms(d3r30, "north", d3r31, "south")
Room.connectRooms(d3r31, "east", d3r32, "west")
Room.connectRooms(d3r31, "north", d3r32, "south")



####
#NPC section
####
Niva = NPC("Niva", "A young female Magi, new to the world of Magi, just like you. She has navy blue hair, and an aqua blue dress. On her head, she wears a hairpin with a bird on it. She seems to specialize in light magic.", d1r1, "Light")
Niva.addConversation("Niva grins, wide eyed with excitement. She\'s hopping from foot to foot, eyeing the path into deeper into the labrynth. \n\"Ooooh man I can\'t wait! This is gonna be so fun! At least, I hope so. This is basically gonna be a daily hobby from here on… but so far so good! \nAnyhow, what\'s up?\" \n\n1.Tell me about yourself. \n2.Any advice? \n3.Why\'d you become a Magi?\n4.Good luck out there!\n","Not much to say! You know me. Query, you and I have been penpals for a while. We meet up with Kyuubey, Query and I sign up to be Magi right away while you decide to just test it out… And here we are! What a way to spend a meetup, huh? We\'re basically superheroes now! We have magic!","She taps her chin as she thinks. \"Well… I\'d be really careful about taking damage if I were you. You\'ll find some Candy and some Greif Seeds in the labyrinth, but not too many. Saferooms will heal you for some amount, but only once!\"","She sighs. \"Well… My mom is a glassworker, and a little while ago she was working on some pieces. We don\'t have that much money, and the person commissioning her would have paid a lot… but something went wrong, and the piece fell on their head. It would have been considered manslaughter… but, I made a wish with Kyuubey to have prevented that from happening.\" She looks uneasy as she finishes this story, but then holds a finger up to her mouth. \"Don\'t tell anyone!\"","She nods. \"Thanks, you too! Don\'t worry, we\'ll beat that Witch in a heartbeat and be out of there before you know it.\"")#Niva convo 0, intro 1
Niva.addConversation("Niva hardly pays you any attention. She seems distraught at something, far from the bubbly and happy person from before. \n\n1.Are you okay?. \n2.Can I do anything to help you? \n3.Stay safe, okay? \n4.I\'ll leave you alone now.\n","She slowly nods, and says nothing else. She then pauses, and shakes her head. \"No, no I\'m not okay. Just, leave me alone… alright?\"","She shakes her head. \"No, no I\'ll be fine…\"","She hardly pays you any mind as you say that.","She shoos you away.")#Niva convo 1, general1

Query = NPC("Query", "A young and inexperienced Magi. They've been your friend for a while, alongside Niva. They cover their face with a white mask of ivory, and they wear a long grey shawl. They seem to specialize in dark magic.", d1r1, "Dark")
Query.addConversation("Query leans back against a wall, looking quite satisfied with themself. They seem to enjoy their current outfit quite a bit. They\'re keeping an eye out on Niva, making sure she doesn\'t act too rashly. \"Oh, yes?\" \n\n1.Tell me about yourself. \n2.Any advice? \n3.Why\'d you become a Magi? \n4.Good luck out there!\n","\"Not too much else to say. We three were penpals, we met up, and now I have magic powers and a new life to life. Before you ask: no, I don\'t wanna take off this mask. It looks cool!\"","\"Hmm… Neutral Magic seems to be your specialty, which is nice. You hit harder with it, and it doesn\'t have any resistances. But do know it costs more mana to use.\"","\"I... had kind of a bad background as a kid. I\'m sorry I never told you, I just never really… wanted to. Um. Yeah. Well I made a wish to leave my accused hellhole behind, and here I am now… with friends and magic powers. Could be worse.\"","They nod, their expression unreadable from behind that mask. \"Thanks. You too.\"")#Query convo0, intro1
Query.addConversation("Query waves as you approach. They seem to be enjoying themselves, though they do look a little bit scratched up. \"Hello. You needed me?\" \n\n1.Find anything? \n2.How goes it? \n3.Whatcha thinking? \n4.Seeya later!\n","\"Nothing of value, really. I don\'t think anything we find in a labyrinth is that useful outside of it, sadly… it\'s a shame too, as some of the things here… it\'s something straight out of the imagination of a madman.\"","They make a brief nod. \"So far, so good. Enemies are a little tough, but nothing I can\'t handle. I\'ll probably lag behind a little when you go to fight the witch, okay? Sorry, but there are some things I still want to look at.\"","\"It really is interesting how Witches are able to form… pocket realities like this. This is an entire world just based off of sewing supplies, and who knows why it\'s like that.\"","\"Seeya around.\"") #Query convo1, general1
Query.addConversation("Query seems like they\'re barely standing on their feet. They look frazzled and stressed. They jump a little bit as you approach them \"AaaH—Ah. Yes. Yes?\" \n\n1.How are you feeling? \n2.Have you seen Niva anywhere? \n3.What just happened? \n4.Good luck out there…\n","\"Tired, hurt, anxious, terrified… But overall, could be worse. I really want to leave this place soon though. I\'m not yet cut out for the Magi life I don\'t think.\"","\"No, I…\" They falter, before taking a second. \"No, I have not. I hope she\'s okay. This is new territory for all of us.\"","\"I have no idea! You killed the witch, we were about to leave, I was going to ask Niva—\" They pause. \"… I hope we find Niva soon.”\"","They nod.\"Thanks… you too. If you find Niva, call for me okay?”\"") #Query convo2, intro2
Query.addConversation("Query is sitting on the ground. They glare at you as you approach, but restrain themselves as they realize it\'s just you. They hold a hand to their head. \n\n1.Find anything? \n2.Are you okay? \n3.Have you seen Niva anywhere? \n4.Seeya around…\n","\"Nothing beyond useless ruins. If I see one more moving statue while I\'m just trying to find Niva, I\'m going to tear this place to the ground.\"","\"No. I really need to leave this place, it\'s getting to me. I feel sick, angry, and I can\'t search for Niva like this.\" They sigh, but in a way that sounds more like a hiss. \"If you find Niva or kill the witch, call for me, okay?\"","\"No, I have not,\" they snap. \"I\'ll tell you if I have, okay? Now stop talking to me and go find her.\"","\"Goodbye,\" they say coldly.") #Query convo3, general 2


####
#ENEMY SECTION
#To save on processing for all enemies actions, enemies of labrynths 2 and 3 will be created in checkRoomMoveOn
####
#Monster("Bob the monster", 20, d1r2, 10, 10, 10, "Dark") 
#4 minions for 1st labrynth, 8 for 2nd, 16 for 3rd.
#2 familiars for 1st Labrynth, 4 for 2nd, 6 for 3rd.

#Lab 1
ribbon1=Minion("Ribbon 1", 100, d1r3, 42, 42, 10, "Neutral", "A multicolored ribbion tied such that it looks vaguely like a human.")
ribbon2=Minion("Ribbon 2", 100, d1r5, 40, 40, 10, "Neutral", "A multicolored ribbion tied such that it looks vaguely like a human.")
ribbon3=Minion("Ribbon 3", 100, d1r6, 40, 40, 10, "Neutral", "A multicolored ribbion tied such that it looks vaguely like a human.")
ribbon4=Minion("Ribbon 4", 100, d1r9, 40, 40, 10, "Neutral", "A multicolored ribbion tied such that it looks vaguely like a human.")

needle1=Familiar("Needle 1", 150, d1r10, 45, 55, 25, "Neutral", "A giant living sewing needle. It alternates between hovering and stabbing into the ground as movement.")
needle2=Familiar("Needle 2", 150, d1r2, 45, 55, 25, "Neutral", "A giant living sewing needle. It alternates between hovering and stabbing into the ground as movement.")

irene=Witch("IRENE", 250, d1r8, 60, 70, 35, "Neutral", "IRENE: The Witch Of Ribbons. \n She looks like a long silky ribbion tied around a half-opened present... if it was created in a poor 3D modeling program. She wanders her Labrynth, giftwrapping any humans unfortunate enough to encounter her.")
#self, name, health, strength, room, attackpw, magicpw, defense, typestatus, desc)
#Lab 2
statue1=Minion("Statue 1", 150, d2r2, 40, 40, 20, "Light", "A small stone statue of a cherub. Despite it being made of stone, it moves freely to attack you.")
statue2=Minion("Statue 2", 150, d2r5, 40, 40, 20, "Light", "A small stone statue of a dog. Despite it being made of stone, it moves freely to attack you.")
statue3=Minion("Statue 3", 150, d2r7, 40, 40, 20, "Light", "A small stone statue of a cherub. Despite it being made of stone, it moves freely to attack you.")
statue4=Minion("Statue 4", 150, d2r10, 40, 40, 20, "Light", "A small stone statue of a snake. Despite it being made of stone, it moves freely to attack you.")
statue5=Minion("Statue 5", 150, d2r14, 40, 40, 20, "Light", "A small stone statue of a cherub. Despite it being made of stone, it moves freely to attack you.")
statue6=Minion("Statue 6", 150, d2r21, 40, 40, 20, "Light", "A small stone statue of a cat. Despite it being made of stone, it moves freely to attack you.")

angel1=Familiar("Angel 1", 250, d2r3, 55, 55, 35, "Light", "An angelic humanoid, with no face. It wields a harp. Wherever it goes, light and choir music follows.")
angel2=Familiar("Angel 2", 250, d2r9, 55, 55, 35, "Light", "An angelic humanoid, with no face. It wields a harp. Wherever it goes, light and choir music follows.")
angel3=Familiar("Angel 3", 250, d2r12, 55, 55, 35, "Light", "An angelic humanoid, with no face. It wields a harp. Wherever it goes, light and choir music follows.")
angel4=Familiar("Angel 4", 250, d2r2, 55, 55, 35, "Light", "An angelic humanoid, with no face. It wields a harp. Wherever it goes, light and choir music follows.")

abagail=Witch("ABAGAIL", 350, d2r22, 70, 80, 45, "Light", "ABAGAIL: The Witch of Shine. \nThis witch looks as if it was made out of scraps of glass and magazine clippings. She has 6 pairs of glittery bird wings, but has the head of a cat, a snake, and a faceless human. She stays in her labrynth, preaching to her familiars endlessly.")

#Lab 3
blackcat1=Minion("BlackCat 1", 225, d3r3, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat2=Minion("BlackCat 2", 225, d3r13, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat3=Minion("BlackCat 3", 225, d3r19, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat4=Minion("BlackCat 4", 225, d3r5, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat5=Minion("BlackCat 5", 225, d3r21, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat6=Minion("BlackCat 6", 225, d3r24, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat7=Minion("BlackCat 7", 225, d3r10, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat8=Minion("BlackCat 8", 225, d3r20, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat9=Minion("BlackCat 9", 225, d3r20, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat10=Minion("BlackCat 10", 225, d3r31, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat11=Minion("BlackCat 11", 225, d3r18, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")
blackcat12=Minion("BlackCat 12", 225, d3r11, 50, 50, 40, "Dark", "A black cat, with two button eyes and a twisted grin. It has no claws, but has many angler-fish like fangs.")

crook1=Familiar("Crook 1", 350, d3r9, 65, 65, 45, "Dark", "A thick, shadowy humanoid. Hands like baseball mittens and inhuman eyes hidden under a fedora, it hits hard. It cannot speak.")
crook2=Familiar("Crook 2", 350, d3r14, 65, 65, 45, "Dark", "A thick, shadowy humanoid. Hands like baseball mittens and inhuman eyes hidden under a fedora, it hits hard. It cannot speak.")
crook3=Familiar("Crook 3", 350, d3r16, 65, 65, 45, "Dark", "A thick, shadowy humanoid. Hands like baseball mittens and inhuman eyes hidden under a fedora, it hits hard. It cannot speak.")
crook4=Familiar("Crook 4", 350, d3r27, 65, 65, 45, "Dark", "A thick, shadowy humanoid. Hands like baseball mittens and inhuman eyes hidden under a fedora, it hits hard. It cannot speak.")
crook5=Familiar("Crook 5", 350, d3r31, 65, 65, 45, "Dark", "A thick, shadowy humanoid. Hands like baseball mittens and inhuman eyes hidden under a fedora, it hits hard. It cannot speak.")
crook6=Familiar("Crook 6", 350, d3r30, 65, 65, 45, "Dark", "A thick, shadowy humanoid. Hands like baseball mittens and inhuman eyes hidden under a fedora, it hits hard. It cannot speak.")

sam=Witch("SAM", 450, d3r33, 80, 90, 50, "Dark", "SAM: The Witch of Shade. \n This witch is a giant serpent, with it's head hidden in a hood, with only it's 3 eyes visible. The outlines of this witch are thick and jagged, made worse by it's panicked and rapid movements. Some say this witch does not control it's familiars, but that they control it, using it's fear to create larger labrynths to trap humans in.")




####
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    time.sleep(0.2)
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            time.sleep(0.75)
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            time.sleep(0.75)
            print(i.name)
        print()
    if player.location.hasCharacters():
        print("This room contains the following characters:")
        for i in player.location.characters:
            time.sleep(0.75)
            print(i.name)
        print()
    if player.location.hasBarriers():
        print("This room has the following obstacles: ")
        for i in player.location.barriers:
            time.sleep(0.75)
            print(i.name)
        print()    
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()
    if player.location.typeofroom == "safeRoom":
        print("This room is a safe room! You can try to relax in here. Monsters won't follow you in here.")
        print()

def showHelp():
    clear()
    print("help -- brings up the help screen")
    print("go <direction> -- moves you in the given direction")
    print("inventory -- opens your inventory")
    print("inspect <item or npc> -- gives you a short description of the item or NPC.")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- drops item in current room")
    print("wait -- waits for 1 increment of time")
    print("relax -- heal some HP in a saferoom")
    print("status or me -- Shows your current status") 
    print("attack <monster> -- Attacks chosen monster")
    print("talk <NPC> -- talks to NPC")
    print("use <item> -- uses an item. Also works to read an item.")
    print()
    print("／人◕ ‿‿ ◕人＼ < Getting low on Health? Eat some food to heal HP!")
    print("／人◕ ‿‿ ◕人＼ < Low on Mana? Use a Grief Seed, and you'll be feeling better soon!")
    print()
    input("Press enter to continue...")

def checkRoomToMoveOn():
    if player.location == d1r8:
        if player.location.hasMonsters() == False:
            clear()
            player.location = d2r1
            kyuubey.moveTo(d2r1)
            Query.moveTo(d2r1)
            Query.changeCurrentConvo(2)
            kyuubey.moveTo(d2r1)
            kyuubey.changeCurrentConvo(3)
            print("You slay the witch, and as her ribbon form floats gently to the ground you finally catch a breath. You did it, you killed your first witch. \n Easy, right?")
            time.sleep(1)
            print("The labrynth slowly starts to fade around you, your Magi outfit along with it. Kyuubey hops onto your shoulder, seemingly satisfied with your work.")
            time.sleep(1)
            print("\nSuddenly, Query jogs over to you, looking concerned. \n\"Have you seen Niva?\" Query asks. \"I can't find her... shame, she seemed really excited to fight the wi--\"")
            time.sleep(3)
            print("\n\n\n")
            print("The dissapation halts. Before you can ask what's happening, a sound like the roar of thirty lions rings through the labrynth, freezing you in place.")
            time.sleep(1)
            print("Shortly thereafter, a bright multicolored light rushes into the room like a river, blinding you and forcing you onto the ground.")
            time.sleep(1)
            print("\nA minute passes before you're able to see again. Opening your eyes, you see that you are not back in the outside world. You're still in your Magi attire, you're still with Query, and Kyuubey is still clinging to your shoulder.")
            time.sleep(1)
            print("The only difference is that you seem to be in an entirely different labrynth, one far less ribbony and more stone than the one you were just in.")
            print("Niva still seems to be missing.")
            time.sleep(1)
            print("Query shakes their head in confusion. \"This... okay, this isn't fun anymore. We need to find the exit, and fast.\"")
            print()
            time.sleep(1)
            input("Press enter to continue...")
            
    elif player.location == d2r22:
        if player.location.hasMonsters() == False:
            clear()
            player.location = d3r1
            kyuubey.moveTo(d3r1)
            kyuubey.changeCurrentConvo(6)
            print("The witch falls, and you attack it a few more times for good measure.")
            time.sleep(2)
            print("After a bit, the labrynth once again starts to fade. You sigh, releived you can finally leave this place.")
            time.sleep(1)
            print("You call out to Query, saying it's finally time to leave. ")
            time.sleep(1)
            print("You don't get the response you would have preferred. \n\n")
            time.sleep(3)
            print("Once again the dissapation stops, and once again you're hit with a blinding force that hits you with an immense amount of force. While before the light was bright, now it's almost as if you're getting attacked by pure black ink.")
            time.sleep(1.8)
            print("\n You wake up to Kyuubey patting your face with his paw, trying to awaken you.")
            time.sleep(1)
            print("You're in a small purple room, barely larger than a broom closet. You call out to Niva and Query, and this time nither answer.")
            time.sleep(1)
            print("You stand up, dust yourself off, and rub your temples. Once again, you're stuck in another new labrynth. How long is this going to go on for?")
            print()
            input("Press enter to continue...")
    elif player.location == d3r33:
        if player.location.hasMonsters() == False:
            playing = False
            endings()
            

def endings():
    clear()
    
    if player.awarenessofplot >=5:
        time.sleep(1)
        print("You kill the final witch, and with a roar the monster falls to the ground, defeated. \n")
        time.sleep(1)
        print("All is silent as the Labrynth dissapates and you find yourself back in the normal world. \n")
        time.sleep(1)
        print("Kyuubey starts to sneak away, but before he can get too far you grab him by the neck and hold him at armslength. You yell at him, demanding he explain what just happened.")
        if kyuubey.wishopen == False: #Know what the purpose of Kyuubey/wishes are, but used wish
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"Erf... Alright. It doesn't matter much anymore, and maybe it'll be useful for you to know the full extent of your situation.\"")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"The typical lifecycle of a Magi is this: \"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"1. A human gets one wish, powerful enough to warp reality itself. In exchange, they devote a large percentage of the rest of their life to being a Magi, and the duties that follow.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"2. Magi are tasked with fighting and killing Witches, which prey on humans. To do this, they are given \"Soul Gems,\" which give them hightened resistance and the ability to cast magics.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"3. Magi are either killed in the process of fighting witches, or eventually become Witches themselves, if their Grief gets too high. There is no way to reverse this.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"Likely what happened was... your friends turned into witches while spelunking the labrynth. Not common, and somewhat unfortunate. They couldn't even kill one Witch before transformation. \"")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"4. Greif Seeds are the only things that can be used to refill the Mana of a Magi. They can only be obtained by going to a labrynth.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"Since Witches are formed by preverse human desires as well as being Magi in the past life... it makes sense to make more Magi. If one Magi can kill several Witches, we create one problem while destroying many others.\"")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"And that's where you find yourself. You used your wish, and that can't be undone.\"")
            time.sleep(2)
            print("In disgust, you violently toss kyuubey to the side in a rage. Another kyuubey brushes up against the back of your ankles a second later.")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"I suggest you calm down, else you turn into a Witch faster.\"")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"You can't undo your wish. You will turn into a Witch someday. There's no changing that. I'll be back in three days, so I hope you'll be ready to kill more Witches by then.\"")
            time.sleep(1)
            print("The kyuubey vanishes, and you are left enraged with no respite. You will turn into a Witch.")
            time.sleep(1)
            print("And in three days, you will wander more labrynths, to kill more witches.")
            time.sleep(2)
            print("*****************************************")
            print("GAME OVER. \nEnding: Contract of Remorse")
            print("*****************************************\n")
        else: #Know what the purpose of Kyuubey/wishes are, did not use wish    
            print("／人◕ ‿‿ ◕人＼ \"Erf... Alright. Since you asked, I will tell you.\"")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"The typical lifecycle of a Magi is this: \"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"1. A human gets one wish, powerful enough to warp reality itself. In exchange, they devote a large percentage of the rest of their life to being a Magi, and the duties that follow.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"2. Magi are tasked with fighting and killing Witches, which prey on humans. To do this, they are given \"Soul Gems,\" which give them hightened resistance and the ability to cast magics.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"3. Magi are either killed in the process of fighting witches, or eventually become Witches themselves, if their Grief gets too high. There is no way to reverse this.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"Likely what happened was... your friends turned into witches while spelunking the labrynth. Not common, and somewhat unfortunate. They couldn't even kill one Witch before transformation. \"")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"4. Greif Seeds are the only things that can be used to refill the Mana of a Magi. They can only be obtained by going to a labrynth.\"")
            time.sleep(3)
            print("／人◕ ‿‿ ◕人＼ \"Since Witches are formed by preverse human desires as well as being Magi in the past life... it makes sense to make more Magi. If one Magi can kill several Witches, we create one problem while destroying many others.\"")
            time.sleep(1)
            print("You say that you never used your wish, that you were just borrowing powers for the sake of killing witches. Squeezing him tighter, you demand to be released from this contract.")
            time.sleep(1)
            print("／人◕ ‿‿ ◕人＼ \"You never did use your wish, and you can't be a sustainable Magi without making a wish... Okay.\"")
            time.sleep(2)
            print("／人◕ ‿‿ ◕人＼ \"I release you from this contract. You are no longer a Magi, and so lose all magical abilities... but you will never become a witch, and you will never have to step into a Labrynth ever again.\"")
            time.sleep(2)
            print("You are hit with a wave of icey-chill, and after it passes you can confirm Kyuubey is telling the truth: you no longer have magic.")
            time.sleep(1)
            print("You sigh, and drop Kyuubey. You walk off, away from Kyuubey in silence.")
            time.sleep(1)
            print("You've survived all the laberynths, and you've saved yourself from a horrible fate...")
            time.sleep(1)
            print("As exhausting as this has been, it could have gone worse.")
            time.sleep(1)
            print("You are free.")
            time.sleep(3)
            print("*****************************************")
            print("GAME OVER. \nEnding: No more Labyrinths")
            print("*****************************************\n")

    elif player.grief >= 250 or kyuubey.wishopen == False: #Bad ending
            time.sleep(1)
            print("You kill the final witch, and with a roar the monster falls to the ground, defeated. \n")
            time.sleep(1)
            print("All is silent as the Labrynth dissapates and you find yourself back in the normal world. \n")
            time.sleep(1)
            print("Suddenly, sadness overtakes you and you fall to your knees. Your allies are still nowhere to be found. You are alone.")
            time.sleep(3)
            print("\n\n")
            print("Months later, another Labrynth forms, talored to your themes of choice. If your mind was at all together, you would have perhaps enjoyed it.")
            time.sleep(1)
            print("You have become a witch, unhuman in form. You spend your days feasting on humans and wandering lost in your own labrynth.")
            time.sleep(1)
            print("Stuck in this labrynth, with minions to serve you, you stay...")
            time.sleep(2.5)
            print("That is, until a Magi appears to face you one day. \n")
            time.sleep(1)
            print("************************************")
            print("GAME OVER. \nEnding: Become a Witch.")
            print("************************************\n")

    else: #Normal ending
        print("You kill the final witch, and with a roar the monster falls to the ground, defeated. \n")
        time.sleep(1)
        print("All is silent as the Labrynth dissapates and you find yourself back in the normal world. \n")
        time.sleep(1)
        print("You feel... like something is missing. Like you missed something important while fighting through the labrynths.")
        time.sleep(1)
        print("Kyuubey rubs his head against you. \"Ready to do that again, tomorrow?\" \n")
        time.sleep(1)
        print("You sigh, nod, and start walking. So busy... well, such is the life of a Magi.\n")
        time.sleep(1)
        print("*************************************")
        print("GAME OVER. \nEnding: Yet another day.")
        print("*************************************\n")


######
#HERE IS WHERE THE GAME STARTS
######

#createWorld()

###
#Make intro here


clear()
print("___  ___            _        _____          _ _    ______             ")
print("|  \/  |           (_)      |_   _|        ( ) |   |  ___|            ")
print("| .  . | __ _  __ _ _  ___    | | ___ _ __ |/| |_  | |_ _ __ ___  ___ ")
print("| |\/| |/ _` |/ _` | |/ __|   | |/ __| '_ \  | __| |  _| '__/ _ \/ _ \ ")
print("| |  | | (_| | (_| | | (__   _| |\__ \ | | | | |_  | | | | |  __/  __/")
print("\_|  |_/\__,_|\__, |_|\___|  \___/___/_| |_|  \__| \_| |_|  \___|\___|")
print("               __/ |                                                  ")
print("              |___/                                                   \n")
print("Welcome!")
time.sleep(0.75)
print("This game was heavily inspired by Puella Magi Madoka Magica, an anime about fighting monsters with magical powers.")
time.sleep(0.75)
print("The source material features some dark subject matter, so please be warned!")
intro=True
while intro:
    time.sleep(0.75)
    print("Would you like some character background?")
    expos = input("(Yes or No): ")
    if expos.lower() == "yes" or expos.lower() =="y":
        print("You are a \'Magi\', a person given magical powers by a being known as Kyuubey, this small cat-like thing with long ears.")
        time.sleep(0.75)
        print("Magi hunt these monsters known as  \'Witches\' which kill and eat humans by trapping them in pocket-dimension laberynths. No two witches are alike.")
        time.sleep(0.75)
        print("People become Magi by making a deal with Kyuubey. In exchange for volunteering to hunt witches, a Magi gets a single wish to do with as they please.")
        time.sleep(0.75)
        print("You've been lended powers by Kyuubey, on the promise that you'll cash in your wish soon. Until then, you have just a sampling of the magic that other Magi can do.")
        time.sleep(0.75)
        print("You've just entered a laberynth in order to try and kill a witch.")
        time.sleep(0.75)
        print("You're accompanied by two other Magi: The light-attacking Niva, and the dark-attacking Query. You are also accompanied by Kyuubey.")
        intro=False
    elif expos.lower() == "no" or expos.lower() =="n":
        print("Gotcha! No background needed.")
        intro=False
    else:
        print("Cmon, it's a yes or no question!")

time.sleep(0.75)
playername = input("Before we finally play... what is the name of your character?: ")
while playername == "" or playername == " ":
    playername = input("Please give yourself an actual name: ")

print("Alright then! Thank you so much for your patience, and please enjoy Magic Isn't Free! ／人◕ ‿‿ ◕人＼")
input("Press enter to continue...")


player = Player(playername)

#／人◕ ‿‿ ◕人＼
#\n\n for choices.
kyuubey = Kyuubey(player, "Kyuubey is a small white cat-like thing. He was the one who lended you your powers. His face never changes from beyond a slight cat-like smile, even when speaking. ／人◕ ‿‿ ◕人＼", d1r1)
kyuubey.addConversation("""Looking amused at the scene before him, Kyuubey almost pays you no mind as you walk up to him.
    ／人◕ ‿‿ ◕人＼ \"Yes, you need something?\" 

    1.Tell me about yourself.
    2.Advice? 
    3.Ask to use your wish.
    4.See you around.""","／人◕ ‿‿ ◕人＼ \"I\'m Kyuubey! Resident magical-being-giving-magical-powers. I can\'t do any attacking magic myself, which is why I strike deals with Magi! Your friends Query and Niva have already made their wishes… We don\'t normally lend out powers like this as it makes the magic unstable. However, since there\'s a witch labyrinth here, I\'ve decided to make an exception.\"","／人◕ ‿‿ ◕人＼ \"When you\'re in a fight, you can talk, attack, use items, use magic, or flee.  Using magic costs mana, but tends to do more magic… but it varies.\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼ \"No need to say that! Since I\'m useless in a fight, I\'ll probably just follow you around I think.\"") #Kyuubey Convo 0, intro1
kyuubey.addConversation("You usher Kyuubey over, and while waving his tail back and forth, he addresses you. \n／人◕ ‿‿ ◕人＼ \"Yes, you need something?\" \n\n1. Advice? \n2.So, why did you make us Magi? \n3.Ask to use your wish. \n4.How should we handle these enemies?\n","／人◕ ‿‿ ◕人＼\"The only fights you can\'t run from are witch fights. If you need to flee, flee!\"","／人◕ ‿‿ ◕人＼\"We always need more Magi in the world to help fight off Witches. Also, this Labyrinth formed really quickly, and no already-created Magi were in the area. So, we had to rely on you and your friends!\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼\"These enemies don\'t seem super strong… Just attack them however you want!\"") #Kyuubey Convo 1, general1
kyuubey.addConversation("You find Kyuubey in a corner of the room, trying to hide from the witch. \n／人◕ ‿‿ ◕人＼ \"If you need something, please be quick. If the witch notices me, I'm dead..\" \n\n1. Advice? \n2.How should I handle this witch? \n3.Ask to use your wish. \n4.Why do you want us to kill Witches?\n","／人◕ ‿‿ ◕人＼\"Witches are super powerful and strong. Be prepared for a tough fight!\"","／人◕ ‿‿ ◕人＼\"This witch seems to specialize in what I call \"Neutral\" Magic. That doesn\'t have any weaknesses to it, so… hit it for all you got!\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼\"Witches kill and feed on humans! They\'re little more than powerful, reality-warping beasts. And Magi like you are quite literally made to fight them!\"") #Kyuubey Convo 2, witch1
kyuubey.addConversation("Looking lost in thought, Kyuubey almost pays you no mind as you walk up to him.\n／人◕ ‿‿ ◕人＼ \"Yes, you need something?\" \n\n1. Advice? \n2.What just happened? \n3.Ask to use your wish. \n4.What should we do from here?\n","／人◕ ‿‿ ◕人＼\"Be aware: There are not many healing items in your average Labyrinth, and no way to get some from outside. Be careful when using items and getting hit!\"","／人◕ ‿‿ ◕人＼\"We seem to have been transported to the beginning of a new labyrinth… Odd, seeing as we just beat a witch. Perhaps a new one has just formed, right here? If so, we need to find it and kill it!\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼\"What can we really do from here besides continue exploring? Don\'t worry, after this we can leave with our heads held high, knowing that we stopped two witches today.\"") #Kyuubey Convo 3, intro2
kyuubey.addConversation("You usher Kyuubey over, and while waving his tail back and forth, he addresses you. \n／人◕ ‿‿ ◕人＼ \"Yes, you need something?\" \n\n1. Advice? \n2.How should we handle these enemies? \n3.Ask to use your wish. \n4.What are you thinking?\n","／人◕ ‿‿ ◕人＼\"Be aware: There are not many healing items in your average Labyrinth, and no way to get some from outside. Be careful when using items and getting hit!\"","／人◕ ‿‿ ◕人＼\"These enemies are of a pretty typical design for light-type enemies… if you have some dark-type magic, that\'ll maybe help defeat them.\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼\"I\'m still pondering how it\'s possible for a Witch to spawn so quickly… It takes a while normally. Something bad must have happened to cause the creation of a witch so soon.\"") #Kyuubey Convo 4, general2
kyuubey.addConversation("You find Kyuubey in a corner of the room, trying to hide from the witch. \n／人◕ ‿‿ ◕人＼ \"If you need something, please be quick. If the witch notices me, I'm dead..\" \n\n1. Advice? \n2.How should I handle this witch? \n3.Ask to use your wish. \n4.Why are witches so weird looking?\n","／人◕ ‿‿ ◕人＼\"Witches are super powerful and strong. Be prepared for a tough fight!\"","／人◕ ‿‿ ◕人＼\"This witch seems to be a master at light-type magics. If you have and dark-style magics, that\'ll hit this witch hard!\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼\"They feed on humans yes, but they are also created from and are formed after twisted desires. Aside from that, there\'s really no answer… and it\'s not like you can ask a Witch why they look the way they do.\"") #Kyuubey Convo 5, witch2
kyuubey.addConversation("Looking shocked, Kyuubey almost pays you no mind as you walk up to him.\n／人◕ ‿‿ ◕人＼ \"Yes, you need something?\" \n\n1. Advice? \n2.What just happened? \n3.Ask to use your wish. \n4.Where is everyone?\n","／人◕ ‿‿ ◕人＼\"Be aware: There are not many healing items in your average Labyrinth, and no way to get some from outside. Be careful when using items and getting hit!\"","／人◕ ‿‿ ◕人＼\"… Once again, it seems that we got transported to the beginning of a labyrinth. This time, you seem to be a lone Magi. I\'m sorry.\"","[ASKING TO USE WISH]","Kyuubey shakes his head.／人◕ ‿‿ ◕人＼\"Doesn\'t matter. We need to get out of here as soon as possible.\"") #Kyuubey Convo 6, intro3
kyuubey.addConversation("You usher Kyuubey over, and while waving his tail back and forth, he addresses you. \n／人◕ ‿‿ ◕人＼ \"Yes, you need something?\" \n\n1. Advice? \n2.How should we handle these enemies? \n3.Ask to use your wish. \n4.What are you thinking?\n","／人◕ ‿‿ ◕人＼\"The only fights you can\'t run from are witch fights. If you need to flee, flee! Be warned, as escape is not always certian, and it can leave you open for attack!\"","／人◕ ‿‿ ◕人＼\"These enemies seem pretty shady… give ‘em some light, and maybe that\'ll help?\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼\"I\'m thinking that after this, we should be able to leave these labyrinths… I should really look into how three Labyrinths can form on top of each other, one after another. I\'ve never seen this before.\"") #Kyuubey Convo 7, general3
kyuubey.addConversation("You find Kyuubey in a corner of the room, trying to hide from the witch. \n／人◕ ‿‿ ◕人＼ \"If you need something, please be quick. If the witch notices me, I'm dead..\" \n\n1. Advice? \n2.How should I handle this witch? \n3.Ask to use your wish. \n4.Will we be done after this?\n","／人◕ ‿‿ ◕人＼\"Witches are super powerful and strong. Be prepared for a tough fight!\"","／人◕ ‿‿ ◕人＼\"This witch seems to be a master at Dark magics. If you have any hard-hitting light magic, that\'ll be great against it!\"","[ASKING TO USE WISH]","／人◕ ‿‿ ◕人＼\"Yes! I\'m certain that once we finish this last fight, we will finally be able to leave these neverending labyrinths. Now go, defeat this Witch and let\'s get out of here!\"") #Kyuubey Convo 8, witchroom3
kyuubey.addConversation("Though his voice is as calm and upbeat as ever, his rigid posture gives something up. Is... is he nervous? \n\n ／人◕ ‿‿ ◕人＼ \"Yes, you wanted something from me?\" \n\n1. Advice? \n2. What is your deal, Kyuubey? \n3.Ask to use your wish. \n4.[Kill Kyuubey]\n","Kyuubey shakes his head. ／人◕ ‿‿ ◕人＼ \"… At this point, I have nothing else to say.\"","／人◕ ‿‿ ◕人＼\"What is my deal? Nothing, if you\'re implying that I\'ve lied. I did no such thing. I do make deals with Magi to handle Witches. It\'s just… different now.\"\n\nWhy is he suddenly confessing to... whatever this is, out of the blue? Is stress getting to him?","[ASKING TO USE WISH]","In a single blow, you fell Kyuubey. You pause for a moment, and another Kyuubey takes his place. He looks and acts exactly the same as the other one. This new Kyuubey cocks his head to the side. \n／人◕ ‿‿ ◕人＼\"Well, that was a waste of a body. Are you done? Nither of us can leave until you kill the witch. So, get going.\"") #Kyuubey Convo 9, saferoom3
kyuubey.addConversation("Kyuubey stares at you, unblinkingly. Does he ever blink? Ever? \nYour vision swims, and you could swear his smile grows large, larger than his face should allow. His cherry red eyes burn into you like fire. You resent him, you feel an unyielding rage at him that only grows, you reach a clawed hand out to choke him and--\n And in yet another instant, you blink and everything is back to normal. You feel no rage, you feel no anger… what were you doing again? Why is your hand outstretched? \n Kyuubey tilts his head at you. ／人◕ ‿‿ ◕人＼ \"Are you doing alright? Do you need something?\" \n\n1.Tips from here on out? \n2. No, I\'m good. \n3.Ask to use your wish. \n4. ... \n","Kyuubey stares at you for a while. After a pause that continues on for a moment too long, he responds. \n／人◕ ‿‿ ◕人＼ \"Why, use magic of course! For you, there\'s no downside. Minions are weaker than Familiars, which are weaker than Witches. There are also microwitches, which are complete wildcards.\"","Kyuubey nods. ／人◕ ‿‿ ◕人＼ \"Right. Just checking in. See if you can find some candy or greif seeds soon though, okay?\"","[ASKING TO USE WISH]","Kyuubey in turn also says nothing. ／人◕ ‿‿ ◕人＼ \"… Well, best continue onwards. Neither of us can leave this place until you kill the witch.\" You feel sick as he says this.") #Kyuubey Convo 10 USED ONLY FOR WHEN GOING TO GET BAD ENDING

#addConversation(self, prompt, resp1, resp2, resp3, resp4): #Be sure that the conversation prompt includes values!
#Every time a converation is made, it is added to a list. First convo is refrenced as 0, 2nd at 1...

###
#Now that player exists, give them things

###
#SPELLS SECTION
###
#Start out knowing blind, bash, and shrowd. Learn other spells elsewhere.


#Niva gives ray of sunshine, Query gives nightmare fuel from conversation.
#Kick into gear, your own song, angelic cacophany, and concerto of the night are all things you have to find on your own. 

blind = magicSpells(player, "Blind", 10, 1, "Light", "[Attacks the enemy with bright rays of light. Does adverage light-type damage.]")
ray_of_sunshine = magicSpells(player, "Ray of Sunshine", 20, 2, "Light", "[Attacks with a more concentrated beam of blue light. Does medium light-type damage.]")
angelic_cacophany = magicSpells(player, "Angelic Cacophany", 30, 3, "Light", "[Strikes the enemy with giant blast of pure light, painfully overloading their senses. Does heavy light-type damage.]")

bash = magicSpells(player, "Bash", 15, 1.5, "Neutral", "[Powers up your weapon to deal a devestating energetic attack. Does above-average damage.]")
kick_into_gear = magicSpells(player, "Kick into Gear", 25, 2.5, "Neutral", "[Powers up a single shot to be heavy hitting. Does a respectable amount of damage.]")
your_own_song = magicSpells(player, "Your Own Song", 40, 3.5, "Neutral", "[Your own peronally-designed heavy hitting attack. Does a lot of damage.]")

shrowd = magicSpells(player, "Shrowd", 10, 1, "Dark", "[You cover the enemy in a shrowd of darkness, painful to the touch. Does adverage dark-type damage.]")
nightmare_fuel = magicSpells(player, "Nightmare Fuel", 20, 2, "Dark", "[In the span of a second, you force the enemy though a nightmare. Does medium dark-type damage.]")
concerto_of_the_night = magicSpells(player, "Concerto of the Night", 30, 3, "Dark", "[The enemy sees illustions and feels the pain of attacks that did not actually strike it. Does heavy dark-type damage.]")


blind.learnQuiet()
bash.learnQuiet()
shrowd.learnQuiet()

####
#ITEM SECTION
####    
#i = Item("Rock", "This is just a rock.")
#i.putInRoom(d1r2)
d1seed1 = GriefSeed()
d1candy1 = Candy()

d2seed1 = GriefSeed()
d2seed2 = GriefSeed()
d2candy1 = Candy()
d2candy2 = Candy()

d3seed1 = GriefSeed()
d3seed2 = GriefSeed()
d3seed3 = GriefSeed()
d3candy1 = Candy()
d3candy2 = Candy()
d3candy3 = Candy()

scarf = important_note("Scarf","A scarf that depicts a scene of a young Magi. You found it in the labyrinth of the ribbon witch.","You hold the scarf close to yourself, and follow along with the story as best you can. \nA young girl is seen dancing to music, in front of a very large crowd. She seems to be a ballerina, and a well known one at that. The girl takes out a Dazzler ribbon, and ends the show with a colorful performance assisted by her prop. \nLittle does she know, her Dazzler has snagged onto some mechanism, which when tugged, starts a rube goldberg machine of misery. She takes a bow as the music ends, and the light fixtures above her fall, landing directly on her.\n\nThere is some space, before you see the magi again, this time depicted in a flowy silky outfit. Her outfit seems to be inspired by that of a ballerina.", player)
bell = important_note("Bell","A small golden bell, one that would fit in the palm of your hand. If you move it at a consistent tempo, after a bit voices start to sing along to the ringing of the bell.","You ring the bell slowly back and forth, and after some time you hear a voice attempting to sing along to the pace you\'re keeping. \n\n‘Glory, glory to Abagail! Glory, glory to Abagail! Glory to the goddess, glory to she!\nGlory to the sacrifice, glory to she! Bless her heads, many to free!\nCurse the rat who made me, me! May his endless world die with thee!\nGlory, glory to Abagail! Glory, glory to Abagail! Glory to the goddess, glory to she!", player)
hairpin = important_note("Hairpin","A Hairpin, much like the one Niva wears. The pin looks far too rusted, as if just holding it for too long would cause it to break.","You carefully turn over the hairpin in your palm. It really is like the one Niva wore… but where is she? Why is this pin rusted so badly? Is this even her pin?", player)
ivorymask = important_note("Ivory Mask","A mask, much like the one Query wears in their Magi outfit. It\'s cracked and dusty, as if the wearer broke it a long time ago.","Query\'s unique mask. Where have they gone? Why have they left their mask here? Questions like these and more as you rack your mind, staring into the empty eyeholes of the mask.", player)
poster = important_note("Wanted Poster","A wanted poster, looking for a white cat. The picture provided is so cartoonish and unclear, you were barely able to tell that much. There is text below it.","A wanted poster, looking for a white cat. There is a large bounty out for this creature, in a currency that doesn\'t seem to exist. \nThe crimes listed for it are: Corruption of the youth, Lying, Escaping arrest. The bounty has been placed by a \"Sam.\" ", player)

scissors = progressionItem("Scissors", "A normal pair of fabric scissors, used to cut felts of all kinds.")
hammer = progressionItem("Hammer", "A small blunt hammer with a metal head. Could be used to hit something... that isn't a monster. It's too small to be a weapon.")
flashlight = progressionItem("Flashlight", "A black flashlight like the ones night guards carry. It is surprisingly bright.")

soulgemdark2 = itemToGiveNewMagic("Smooth Gemstone","A gemstone that slides against your palm like water. If you hold it up to your ear, you hear faint whispers of the dark side of magic.", nightmare_fuel)
soulgemlight2 = itemToGiveNewMagic("Glowing Gemstone","A gemstone that feels faintly warm, like a lightbulb. If you hold it up to your ear, you hear faint whispers of the light side of magic.", ray_of_sunshine)
soulgemneutral2 = itemToGiveNewMagic("Sparkly Gemstone","A gemstone that sparkles in a way that captivates you. If you hold it up to your ear, you hear faint whispers of magic that sounds just your style.", kick_into_gear)
soulgemdark3 = itemToGiveNewMagic("Hypnotizing Gemstone","A gemstone that is an ever-changing swirl of blue, purple, and black. If you hold it up to your ear, you hear faint whispers of the dark side of magic.", concerto_of_the_night)
soulgemneutral3 = itemToGiveNewMagic("Familiar Gemstone","A gemstone that, though it does not look special, is comforting in a way that reminds you of home, of the real world. If you hold it up to your ear, you hear faint whispers of magic that sounds just your style.", your_own_song)
soulgemlight3 = itemToGiveNewMagic("Radiant Gemstone","A gemstone that shines like a small star. If you hold it up to your ear, you hear faint whispers of the light side of magic.", angelic_cacophany)

#Items in labrynth 1
d1candy1.putInRoom(d1r7)
d1seed1.putInRoom(d1r10)
scarf.putInRoom(d1r11)
scissors.putInRoom(d1r9)

soulgemdark2.putInRoom(d1r8)
soulgemlight2.putInRoom(d1r8)

#Items in labrynth 2
d2candy1.putInRoom(d2r20)
d2seed1.putInRoom(d2r15)
d2candy2.putInRoom(d2r12)
d2seed2.putInRoom(d2r5)
bell.putInRoom(d2r7)
hairpin.putInRoom(d2r17)
hammer.putInRoom(d2r10)

soulgemneutral2.putInRoom(d2r21)
soulgemdark3.putInRoom(d2r11)

#Items in labrynth 3
d3candy1.putInRoom(d3r12)
d3candy2.putInRoom(d3r15)
d3candy3.putInRoom(d3r31)
d3seed1.putInRoom(d3r10)
d3seed2.putInRoom(d3r16)
d3seed3.putInRoom(d3r29)
ivorymask.putInRoom(d3r9)
poster.putInRoom(d3r29)
flashlight.putInRoom(d3r22)

soulgemneutral3.putInRoom(d2r11)
soulgemlight3.putInRoom(d2r11)
###
#Barriers
#(self, name, desc, passedthrudesc, room1, dir1, room2, dir2, properkey):

barrier1 = Barrier("blockade of fabric", "Giant yellow, orange, red, and pink ribbons tightly coil around each other, causing a thick barracade that you can't pass through. It's blocking your way north.", "Using the scissors, you cut through the ribbons, the twin blades flying through the barracade like butter.", d1r6, "north", d1r7, "south", scissors)
barrier2 = Barrier("blockade of glass", "A giant, reinforced stained glass window of multicolored shards bears down on you, blocking the way. The glass is surprisingly thick. It's blocking your way north.", "1... 2... 3... \n\n [SMASH] \n You bring the hammer down on the stained glass window, and the window shatters into a million bright pieces. The path is cleared, and you are unharmed.", d2r18, "north", d2r19, "south", hammer)
barrier3 = Barrier("blockade of shadow", "A large whispy cube of solidified, inky-black shadow. Stepping into the cube makes you choke, and you have to exit to breathe again. The shadow is so thick, you cannot pass. It's blocking your way south.", "Turning on the flashlight and pointing it at the blockade, you hear a sound alike a pained hissing, before the shadows finally disperse. You may proceed.", d3r14, "south", d3r15, "north", flashlight)
barrier4 = Barrier("blockade of shadow", "A large whispy cube of solidified, inky-black shadow. Stepping into the cube makes you choke, and you have to exit to breathe again. The shadow is so thick, you cannot pass. It's blocking your way east.", "Turning on the flashlight and pointing it at the blockade, you hear a sound alike a pained hissing, before the shadows finally disperse. You may proceed.", d3r6, "west", d3r7, "east", flashlight)

#(self, name, desc, passedthrudesc, room1, dir1, room2, dir2, prompt, resp1, resp2, resp3, resp4, correctanswer)
#quizBarriertest = quizBarrier("placeholder quiz door", "A quiz door. It BLOCKS the east passageway.", "the quiz door opens. It no longer blocks the east passageway.", d1r2, "east", d1r3, "west", "Choose correct answer ", "this one", "not this one", "nor this one", "absolutely not", 0)
quizBarrier1 = quizBarrier("Quiz Door", "A large stone archway. A giant eye at the top stares down intensely at you. A brass phonograph with a stone microphone juts out from the door, whispering the same question over and over. It's blocking your way north.", "The eye closes, and the door rumbles open. The phonograph stops playing.", d2r14, "north", d2r15, "south", "After a moment, you can finally make sense of the whispers. They're saying: What is the name of the witch? ", "Justine", "Angel", "Hellena", "Abagail", 3)
quizBarrier2 = quizBarrier("Quiz Door", "A large linked-chain fence blocks the path. A flower coils through the chains, and turns to look at you. It looks back and forth, as if confused. It's blocking your way west.", "Satisfied with this answer, the flower nods... and nods... and wilts away, opening the gate just before it turns a complete dried out brown, and falls to the ground.", d3r24, "west", d3r25, "east", "The flower asks: Where do witches come from?", "From the misery of humanity", "From other witches", "From Magi", "From the natural world", 2)
quizBarrier3 = quizBarrier("Quiz Door", "A rusted iron door, with an ouroborus on it. From a slot in the door, a pair of yellow eyes stare down at you. They ask a question. It's blocking your way east.", "The figure sighs, and closes the slot. A moment later, the door slams open, letting you pass. Whatever figure was there has since left.", d3r29, "east", d3r30, "west", "What is the name of the Witch?", "Sam", "Mike", "Rae", "Carmen", 0)

###

player.location = d1r1


playing = True
while playing and player.alive:
    if player.location == d1r8 or player.location == d2r22 or player.location == d3r33:
        checkRoomToMoveOn()
    #Put all of this in an if statment to prevent a final action after killing last boss?
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        while command == "" or command == " ":
            command = input("What now? ")
        commandWords = command.split()
        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            #If killedwitch1, switch npc dialogue to convo2
            #If killedwitch1 and location == d2r1, switch npc dialogue to convo3
            #If killedwitch2, switch npc dialogue to convo4
            #Doesn't seem to like capital letters?
            player.goDirection(commandWords[1].lower()) 
            timePasses = True
        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                player.pickup(target)
                timePasses = True
            else:
                print("No such item.")
                commandSuccess = False
        elif commandWords[0].lower() == "drop":
            targetName = command[5:]
            target = player.getItemByName(targetName)

            if target in player.items:
                player.dropoff(target)
            else:
                print("You don't have that item!")
                commandSuccess = False
        elif commandWords[0].lower() == "inventory":
            player.showInventory()
        elif commandWords[0].lower() == "relax":
            if player.location.typeofroom == "safeRoom":
                player.location.pause(player)
                timePasses = True
            else:
                print("You can't relax in this room, it's too dangerous!")
                commandSuccess = False
                input("Press enter to continue...")
        elif commandWords[0].lower() == "inspect":
            targetName = command[8:] 
            description = player.inspectThing(targetName)#Checking if item exists in room, inventory, or in room as a person
            if description: 
                description(targetName)
            elif description == False:
                print("That is not in this room.")
                commandSuccess = False
                input("Press enter to continue...")
        elif commandWords[0].lower() == "talk": 
            targetName = command[5:]
            target = player.location.getCharacterByName(targetName)
            if target == kyuubey:
                #start dialogue
                if player.grief >= 150:
                    target.changeCurrentConvo(10)
                    target.talkToMe()
                elif player.location == d1r1:
                    target.talkToMe()
                    target.changeCurrentConvo(1)
                elif player.location == d1r8:
                    target.changeCurrentConvo(2)
                    target.talkToMe()
                elif player.location == d2r1:
                    target.talkToMe()
                    target.changeCurrentConvo(4)
                elif player.location == d2r22:
                    target.changeCurrentConvo(5)
                    target.talkToMe()
                elif player.location == d3r1:
                    target.talkToMe()
                    target.changeCurrentConvo(7)
                elif player.location == d3r17:#Convo for just in the saferoom 
                    target.changeCurrentConvo(9)
                    target.talkToMe()
                    target.changeCurrentConvo(7)
                elif player.location == d3r33:
                    target.changeCurrentConvo(8)
                    target.talkToMe() #9 is saferoom, 10 is greif seed
                else:
                    target.talkToMe()
            elif target == Niva:
                if player.location == d1r1:
                    target.talkToMe()
                    print("\"Okay, well I'm gonna run on in. Seeya!!!!\"")
                    target.moveTo(d1r11)
                    target.changeCurrentConvo(1)
                    input("Press enter to continue...")
                else:
                    target.talkToMe()
            elif target == Query:
                if player.location == d1r1:
                    target.talkToMe()
                    print("\"Alright, well... I'll go exploring then. Seeya.\"")
                    target.moveTo(d1r6)
                    target.changeCurrentConvo(1)
                    input("Press enter to continue...")
                elif player.location == d2r1:
                    target.talkToMe()
                    print("\"... I'll be off, trying to find an exit. See you around.\"")
                    target.moveTo(d2r17)
                    target.changeCurrentConvo(3)
                    input("Press enter to continue...")
                else: 
                    target.talkToMe()
            elif target:#Target isn't any of the NPCs above, but is in room?
                target.talk()
            else:
                print("That character is not in this room!")
                commandSuccess = False
                input("Press enter to continue...")
            
        elif commandWords[0].lower() == "use":
            targetName = command[4:]
            target = player.getItemByName(targetName)
            if target in player.items:
                player.useitem(target)
                timePasses = True
            else:
                print("You don't have that item in your inventory!")
                commandSuccess = False
        elif commandWords[0].lower() == "wait":
            timePasses= True
        elif commandWords[0].lower() == "powerup": ##For pure testing purposes
            player.health = 999
            player.healthmax = 999
            player.mana = 999
            player.manamax = 999
            player.strength = 999
            player.strengthMagic = 999
            player.defense = 999
        elif commandWords[0].lower() == "powerdown": ##For pure testing purposes
            player.health = 10
            player.healthmax = 10
            player.mana = 1
            player.manamax = 1
            player.strength = 9
            player.strengthMagic = 9
            player.defense = 9
        elif commandWords[0].lower() == "damageoneself": ##For pure testing purposes
            choice = input("How much would you like to damage yourself for? ")
            choice = int(choice)
            player.health -= choice
            print("Ow. Your health is currently at " + str(player.health))
            input("Press enter to continue...")

        elif commandWords[0].lower() == "status" or commandWords[0].lower() == "me":
            player.showStatus()
        elif commandWords[0].lower() == "help":
            showHelp()
        elif commandWords[0].lower() == "exit":
            playing = False
        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("That monster is not here.")
                commandSuccess = False
        else:
            print("Not a valid command. Type help if you need help.")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()

    


