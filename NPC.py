import random
import updater
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class NPC:
    """docstring for NPC"""
    def __init__(self, name, description, room, typestatus):
        self.name = name
        self.description = description
        self.room = room
        self.type = typestatus
        self.possibleconversations = []
        self.currentConversation = None
        self.convoitshouldbenum = 0
        self.possiblerooms = [room]
        room.addCharacter(self)
        updater.register(self)

    def update(self):
        pass

    def addConversation(self, prompt, resp1, resp2, resp3, resp4): #Be sure that the conversation prompt includes values!
        #Every time a converation is made, it is added to a list. First convo is refrenced as 0, 2nd at 1...
        #Every conversation will always have 4 options because I am lazy. 
        placeholderconvo1 = []
        placeholderconvo2 = [prompt]
        placeholderconvo1.extend([resp1, resp2, resp3, resp4])
        placeholderconvo2.append(placeholderconvo1)
        self.possibleconversations.append(placeholderconvo2)
        self.currentConversation = self.possibleconversations[0]

    def changeCurrentConvo(self, convonumber): #convo number should range from 0 to whatever their number of convos is -1
        self.currentConversation = self.possibleconversations[convonumber]

    def talkToMe(self):

        talkingtoplayer = True
        prompt = self.currentConversation[0]
        #choice1 = self.currentConversation[1][0]
        #choice2 = self.currentConversation[1][1]
        #choice3 = self.currentConversation[1][2]
        #choice4 = self.currentConversation[1][3]
        while talkingtoplayer == True:
            clear()
            print(prompt)
            choice = input("What do you say? [1-4. Press 5 to escape] ")
            while choice.isnumeric() == False:
                clear()
                print(prompt)
                choice = input("What do you say? [1-4. Press 5 to escape] ")
            while int(choice) <1 or int(choice) >5:
                clear()
                print(prompt)
                choice = input("What do you say? [1-4. Press 5 to escape] ")
            actualchoice = int(choice)-1
            if int(actualchoice) == 4:
                talkingtoplayer = False
            elif self.currentConversation[1][actualchoice] != None:
                print("\n"+self.currentConversation[1][actualchoice])
                print()
                input("Press enter to continue...")
            else:
                print("ERROR, CONVERSATION DOES NOT EXIST.")
                talkingtoplayer = False

    def describe(self):
        clear()
        print()
        print(self.description)
        print()
        input("Press enter to continue...")

    def moveTo(self, room):
        self.room.removeCharacter(self)
        self.room = room
        room.addCharacter(self)

    #Differing convos depending on context: tips
    #When you use a talk command, what you get back depends on: who you're 
    #Lookup table for each character, string differing depending on context (item, location..)
    #Lookup table can get chaotic with more variables, be warned. 

class Kyuubey:
    """Kyuubey should be able to answer questions. Kyuubey should be able to give insight into weaknesses of Enemies.
    Kyuubey should be able to USE YOUR WISH to buff you and fully heal you, but only once. """
    def __init__(self, player, description, roomstart):
        self.name = "Kyuubey"
        self.wishopen = True
        self.player = player
        self.description = description
        self.room = roomstart
        self.possibleconversations = []
        self.currentConversation = 0
        roomstart.addCharacter(self)
        updater.register(self)

    def addConversation(self, prompt, resp1, resp2, resp3, resp4): #Be sure that the conversation prompt includes values!
        #Every time a converation is made, it is added to a list. First convo is refrenced as 0, 2nd at 1...
        #Every conversation will always have 4 options because I am lazy. 
        placeholderconvo1 = []
        placeholderconvo2 = [prompt]
        placeholderconvo1.extend([resp1, resp2, resp3, resp4])
        placeholderconvo2.append(placeholderconvo1)
        self.possibleconversations.append(placeholderconvo2)
        self.currentConversation = self.possibleconversations[0]

    def changeCurrentConvo(self, convonumber): #convo number should range from 0 to whatever their number of convos is -1
        self.currentConversation = self.possibleconversations[convonumber]

    def talkToMe(self):

        talkingtoplayer = True
        prompt = self.currentConversation[0]
        while talkingtoplayer == True:
            clear()
            print(prompt)
            choice = input("What do you say? [1-4. Press 5 to escape] ")
            while choice.isnumeric() == False:
                clear()
                print(prompt)
                choice = input("What do you say? [1-4. Press 5 to escape] ")
            while int(choice) <1 or int(choice) >5:
                clear()
                print(prompt)
                choice = input("What do you say? [1-4. Press 5 to escape] ")
            actualchoice = int(choice)-1

            if actualchoice == 2: #3 will ALWAYS be the option to use your wish.
                self.useWish()
                talkingtoplayer = False
            elif actualchoice == 4:
                talkingtoplayer = False
            elif self.currentConversation[1][actualchoice] != None:
                print("\n"+self.currentConversation[1][actualchoice])
                print()
                input("Press enter to continue...")
            else:
                print("ERROR, CONVERSATION DOES NOT EXIST.")
                talkingtoplayer= False

    def describe(self):
        clear()
        print()
        print(self.description)
        print()
        input("Press enter to continue...")

    def update(self):
        self.room.removeCharacter(self)
        self.room = self.player.location
        self.room.addCharacter(self)

    def moveTo(self, room):
        self.room.removeCharacter(self)
        self.room = room
        room.addCharacter(self)

    def useWish(self):
        if self.wishopen:
            clear()
            print("Warning! Using up your wish will fully heal you and give you buffs to your stats...")
            print("... But you'll only be able to use it once, and there may be some side-effects later on.")
            expos = input("Would you like to use your wish? (Yes or No):")
            if expos.lower() == "yes" or expos.lower() == "y":
                self.wishopen = False
                #Do something here to heal your stats/buff
                self.player.healthmax += 100
                self.player.manamax += 100
                self.player.health = self.player.healthmax
                self.player.mana = self.player.manamax
                self.player.strength += 50
                self.player.strengthMagic += 50
                self.player.defense += 80
                self.player.awarenessofplot +=1
                print("You whisper your wish to Kyuubey, and in the blink of an eye you feel energized! \n Your wounds are all gone, and you feel stronger than ever!")
                print("Kyuubey nods approvingly. ／人◕ ‿‿ ◕人＼ \"Good to have you as a proper Magi,\" he says. ")
                input("Press enter to continue...")
            else:
                print("Kyuubey nods. You don't need to use your wish right now. Take your time.")
                input("Press enter to continue...")
        else:
            print("Sorry! You already used your wish to fully heal yourself. You don't get multiple wishes!")
            input("Press enter to continue...")
        
        
        
        