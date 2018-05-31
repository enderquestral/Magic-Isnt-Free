import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Candy(Item):
    """docstring for Healing_Item"""
    def __init__(self):
        self.name = "Piece of Candy"
        self.desc = "A small piece of fruit-flavored hard candy. Gives you enough energy to get back into fighting shape! Heals 50 hp."
        self.loc = None
        self.willHealHealth = True
        self.willHealMana = False
        self.type = "healingItem"

    def heal(self, player):
        if (player.health + 50) > player.healthmax:
            player.health += abs(player.maxhealth-player.health)
        else:
            player.health += 50

        player.items.remove(self)
        print("You healed for 50 HP!")
        print("You tossed away the wrapper...")
        input("Press enter to continue...")

class GriefSeed(Item):
    """docstring for GriefSeed"""
    def __init__(self):
        self.name = "Grief Seed"
        self.desc = "A metal sphere with a needle pointing out of one end. If you use it, you'll heal 50 mana"
        self.loc = None
        self.willHealHealth = False
        self.willHealMana = True
        self.type = "healingItem"
        
    def heal(self, player):
        if (player.mana + 50) > player.manamax:
            player.mana += abs(player.manamax-player.mana)
        else:
            player.mana += 50

        player.items.remove(self)
        print("You healed 50 Mana!")
        print("You tossed away the used up grief seed...")
        input("Press enter to continue...")

class important_note(Item):
    """docstring for important_note"""
    #First time they read an important note, their awareness of plot value goes up by 1
    def __init__(self, name, desc, importantmessage, player):
        Item.__init__(self,name,desc)
        self.importantmessage = importantmessage
        self.user = player
        self.hasBeenReadBefore = False
        self.type = "note"


    def read(self):
        if self.hasBeenReadBefore: #Note has been read before, plot value does not go up
            clear()
            print("You read through the note again. The note says... \n\n\n")
            print("*************************************************** \n")
            print(self.importantmessage)
            print("*************************************************** \n")
            input("Press enter to continue...")
        else:
            self.user.awarenessofplot +=1
            self.hasBeenReadBefore = True
            clear()
            print("You read through the note. The note says... \n\n\n")
            print("*************************************************** \n")
            print(self.importantmessage)
            print("*************************************************** \n")
            input("Press enter to continue...")

class progressionItem(Item):
    """docstring for progressionItem"""
    def __init__(self, name, desc):
        Item.__init__(self,name,desc)
        self.type = "key"

    def use(self, location):
        #If a location has a barrier and if this is the right key for it, unlock it.
        #DO NOT TOSS OUT KEY.
        if location.barriers !=[]:
            #there is a barrier here
            if self.name == location.barriers[0].keyneeded.name:
                #Key is proper key
                location.barriers[0].barrierPassed()
            else:
                #Key is not proper key
                print("You attempt to use the " + self.name +", but it does not work. The obstacle is still there.")
                input("Press enter to continue...")

class itemToGiveNewMagic(Item):
    """docstring for itemToGiveNewMagic"""
    def __init__(self, name, desc, magicImbewed):
        Item.__init__(self,name,desc)
        self.knownmagic = magicImbewed
        self.type = "imbewedItem"

    def use(self, player):
        self.knownmagic.learn()
        if self.knownmagic.element == "Neutral":
            player.awarenessofplot +=1 #Magic is "your" form of magic. Should maybe prompt you to question stuff.
        player.items.remove(self)
        
        

        
        