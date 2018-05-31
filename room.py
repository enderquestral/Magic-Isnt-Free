from monster import Monster
from monster import TrapMonster
import updater
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Room:
    typeofroom = "normalRoom"
    def __init__(self, description):
        self.desc = description
        self.monsters = []
        self.characters = []
        self.exits = []
        self.items = []
        self.barriers = []
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])
    def removeExit(self, exitName, destination):
        self.exits.remove([exitName, destination])
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]
        return None
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
    def partialConnectRooms(room1, dir1, room2):
        #Creates a one way connection from room1 to room 2, blocking any method of escape.
        room1.addExit(dir1, room2)

    def removeConnection(room1, dir1, room2, dir2):
        room1.removeExit(dir1, room2)
        room2.removeExit(dir2, room1)
        pass
    def exitNames(self):
        return [x[0] for x in self.exits]
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def addMonster(self, monster):
        self.monsters.append(monster)
    def removeMonster(self, monster):
        self.monsters.remove(monster)
    def addCharacter(self, npc):
        self.characters.append(npc)
    def removeCharacter(self, npc):
        self.characters.remove(npc)
    def hasBarriers(self):
        return self.barriers != []
    def getBarrierByName(self, name):
        for i in self.barriers:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasMonsters(self):
        return self.monsters != []
    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasCharacters(self):
        return self.characters != []
    def getCharacterByName(self,name):
        for i in self.characters:
            if i.name.lower() == name.lower():
                return i
        return False
    def randomNeighbor(self):
        return random.choice(self.exits)[1]

    def update(self):
        pass

class BossRoom(Room):
    typeofroom = "BossRoom"

class introRoom(object):
    """docstring for introRoom"""
    typeofroom = "introRoom"
    def __init__(self, description):
        Room.__init__(self, description)
        

class safeRoom(Room):
    """docstring for safeRoom"""
    typeofroom = "safeRoom"
    def __init__(self, description):
        Room.__init__(self, description)
        self.giveRespite = True

    def pause(self, player):
        if self.giveRespite == True:
            expos = input("Would you like take a small break in this room? (Yes or No) ")
            if expos.lower() == "yes" or expos.lower() == "y":
                if player.health == player.healthmax:
                    print("You are at full hp, so you did not heal any HP.")
                elif player.health +50 > player.healthmax:
                    self.giveRespite= False
                    print("You decided to take a break in this room, and gained "+ str(player.healthmax - player.health) +" hp.")
                    player.health = player.healthmax
                else:
                    self.giveRespite= False
                    player.health += 50 
                    print("You decided to take a break in this room, and gained 50 hp.")
                input("Press enter to continue...")
            else:
                print("You did not decide to take a break.")
                input("Press enter to continue...")
        else:
            print("You can't stay in this room again, or else monsters will catch up on you. Best keep moving on...")
            input("Press enter to continue...")

class nightmareRoom(Room):
    typeofroom = "nightmareRoom"
    def __init__(self, description):
        Room.__init__(self,description)
        self.enemytofight = False
        self.roomDone = False
        self.residentmonster = None
        updater.register(self)
        #if player takes item in room, they are FORCED to fight a familiar/Put into an encounter with a trap monster.
    
    def itemTakenEnemySpawn(self):
        #check if item has been taken?
        #For each update, (items being picked up passes time,) check if item is still in room?
        self.enemytofight = True
        self.roomDone= True
        possibletypes = ["Neutral", "Dark", "Light"]
        possiblehealth = random.randint(1,3)
        possibleattack = random.randint(2,4)
        possibledef = random.randint(3,6)
        self.residentmonster = TrapMonster("Microwitch", 70*possiblehealth, self, 30*possibleattack, 30*possibleattack, 20*possibledef, random.choice(possibletypes), "The microwitch is a medium-sized creature, not subserviant to the reigning witch but not an equal either. This one, like many others, is an amorphous blob that sometimes manifests identifiable appendages. Microwitches, being not powerful enough to create their own labrynths, steal prey from other witches. They are highly hostile.")
        self.residentmonster.discovered()
        print("\n[Note: The microwitch is a miniboss, of random type and of random strengths. You cannot leave the room until you kill it and all other monsters in the room.]")
        input("Press enter to continue...")

    def update(self):
        if self.items == [] and self.enemytofight == False and self.roomDone == False:
            self.itemTakenEnemySpawn()
        elif self.items == [] and self.roomDone == True and self.monsters == []:
            self.enemytofight = False

class Barrier:
    """docstring for Barrier"""
    def __init__(self, name, desc, passedthrudesc, room1, dir1, room2, dir2, properkey):
        #Room1 is the room player can be in, room2 is the room the barrier is blocking
        self.name = name
        self.desc = desc
        self.passedthrudesc = passedthrudesc
        self.room1 = room1
        self.room2 = room2
        self.dir1 = dir1
        self.dir2 = dir2
        self.keyneeded = properkey
        self.hasbeenpassed = False
        self.room1.barriers.append(self)
        self.room2.barriers.append(self)
        self.type = "normalBarrier"

    def describe(self):
        clear()
        print()
        print(self.desc)
        print()
        input("Press enter to continue...")

    def barrierPassed(self):
        self.hasbeenpassed = True
        #self.room1.connectRooms(self.room1, self.dir1, self.room2, self.dir2)
        #
        print(str(self.passedthrudesc))
        print("[Note: You can now pass. The Barrier has been removed.]")
        input("Press enter to continue...")
        self.room1.barriers.remove(self)
        self.room2.barriers.remove(self)
        del self
        pass

class quizBarrier(Barrier):
    """docstring for quizBarrier"""
    def __init__(self, name, desc, passedthrudesc, room1, dir1, room2, dir2, prompt, resp1, resp2, resp3, resp4, correctanswer):
        self.name = name
        self.desc = desc
        self.passedthrudesc = passedthrudesc
        self.room1 = room1
        self.room2 = room2
        self.dir1 = dir1
        self.dir2 = dir2
        self.hasbeenpassed = False
        self.room1.barriers.append(self)
        self.room2.barriers.append(self)
        self.type = "quizBarrier"

        placeholderconvo1 = []
        placeholderconvo2 = [prompt]
        placeholderconvo1.extend(["1. " + resp1, "2. " + resp2, "3. " + resp3, "4. " + resp4])
        placeholderconvo2.append(placeholderconvo1)
        self.question = placeholderconvo2
        self.correctanswer = correctanswer

    def askQuestion(self, player):
        quizingplayer = True
        while quizingplayer == True:
            print(self.question[0])
            print("\n".join(map(str, self.question[1])))
            choice = input("What is your answer? [1-4. Press 5 to escape] ")
            while choice.isnumeric() == False:
                print(self.question[0])
                print("\n".join(map(str, self.question[1])))
                choice = input("What is your answer? [1-4. Press 5 to escape] ")
            while int(choice) <1 or int(choice) >5:
                print(self.question[0])
                print("\n".join(map(str, self.question[1])))
                choice = input("What is your answer? [1-4. Press 5 to escape] ")
            actualchoice = int(choice) -1
            if actualchoice == 4:
                quizingplayer = False
                return
            elif actualchoice == self.correctanswer:
                print()
                print("You say what you think is the correct answer, and.... \n The door opens! That was the correct answer, and you are now able to proceed.")
                self.barrierPassed()
                quizingplayer = False
            else:
                print()
                print("You say what you think is the correct answer, and.... \n Nothing. Not a sound.")
                print("The room you're in rumbles, and rubble falls on your head. You take 5 damage!")
                player.health -=5
                player.checkifdead()
                input("Press enter to continue...")
                quizingplayer = False
