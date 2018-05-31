import os
import random
import monster

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self, name):
        self.name = name
        self.location = None
        self.lastspot = None
        self.items = [] 
        self.health = 100
        self.healthmax = 100
        self.mana = 100
        self.manamax = 100
        self.strength = 50
        self.strengthMagic = 50
        self.defense = 30
        self.grief = 0
        self.alive = True
        self.level = 1
        self.expneedednextlevel = 1
        self.untilnextlevel = 1
        self.magicknown = []
        self.awarenessofplot = 0

    def goDirection(self, direction):
        #Stop player if there is a barrier blocking their way
        #if place you're going to has a barrier, block it. Say it's name, say what is blocking, in what direction

        if self.location.getDestination(direction) == None:
            print("It is not possible to go that way.")
            input("Press enter to continue...")
            return
        if self.location.barriers != [] and self.location.getDestination(direction).barriers != []:
            if self.location.barriers[0].type == "quizBarrier":
                self.location.barriers[0].askQuestion(self)
                #pass
            else:
                print("You cannot go that way, there is an obstacle blocking the way.")
                input("Press enter to continue...")
            return
        if self.location.getDestination(direction).typeofroom == "BossRoom":
            clear()
            print(direction +"<\n")
            print("Halt!")
            print("If you enter this room, you will be unable to leave it until you kill the boss.")
            print("This is a one-way trip, you will not be able to return to this labrynth.")

            loopthru = True
            while loopthru:
                print("Do you want to enter the room of the Witch?")
                choice = input("(Yes or No): ")
                if choice.lower() == "yes" or choice.lower() == "y":
                    self.lastspot = self.location
                    self.location = self.location.getDestination(direction)
                    loopthru = False
                elif choice.lower() == "no" or choice.lower() == "n":
                    loopthru = False
                else:
                    print("Cmon, it's a yes or no question!")
        elif self.location.typeofroom == "nightmareRoom" and self.location.enemytofight == True:
            print("You cannot leave this room until you kill the enemy!")
            input("Press enter to continue...")
        else:
            self.lastspot = self.location
            self.location = self.location.getDestination(direction)
    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)
    def dropoff(self,item):
        item.loc = self.location
        self.items.remove(item) #remove an item from inventory
        self.location.addItem(item) #Need to addItem to location
    def checkifdead(self):
        if self.health<=0:
            print("And with that, you have died!!!")
            self.alive =False
            print("   ______       _       ____    ____  ________     ___   ____   ____  ________  _______     ")
            print(" .' ___  |     / \     |_   \  /   _||_   __  |  .'   `.|_  _| |_  _||_   __  ||_   __ \    ")
            print("/ .'   \_|    / _ \      |   \/   |    | |_ \_| /  .-.  \ \ \   / /    | |_ \_|  | |__) |   ")
            print("| |   ____   / ___ \     | |\  /| |    |  _| _  | |   | |  \ \ / /     |  _| _   |  __ /    ")
            print("\ `.___]  |_/ /   \ \_  _| |_\/_| |_  _| |__/ | \  `-'  /   \ ' /     _| |__/ | _| |  \ \_  ")
            print(" `._____.'|____| |____||_____||_____||________|  `.___.'     \_/     |________||____| |___| ")

    def showStatus(self):
        clear()
        print("Your current status:\n")
        print(str(self.name) + ", Level: " + str(self.level))
        print("EXP til next level:\t" + str(self.expneedednextlevel))
        print("Health:\t" + str(self.health) + "/" + str(self.healthmax))
        print("Mana:\t" + str(self.mana) + "/" + str(self.manamax))
        print("Grief:\t" + str(self.grief) + "\n")
        print("Stregth:\t" + str(self.strength))
        print("Magic Stregth:\t" + str(self.strengthMagic))
        print("Defense: \t" +str(self.defense))
        print()
        if self.health <= 40:
            print("／人◕ ‿‿ ◕人＼ < Your health is getting low. See if you can find some food to heal yourself.")
        elif self.mana <= 30:
            print("／人◕ ‿‿ ◕人＼ < Your mana is getting low. Without it, you can't use magic. Be sure to use a grief seed soon!")
        elif self.grief >= 100:
            print("／人◕ ‿‿ ◕人＼ < ........")
        else:
            print("／人◕ ‿‿ ◕人＼ < Good luck!") #Standard. Should make comments if HP/Mana is low, if Grief is high.
        input("Press enter to continue...")

    def inspectThing(self,subject): #Subject ideally could be an item or NPC
        subjectininventory = self.getItemByName(subject)

        subjectinroomitem = self.location.getItemByName(subject)#If subject is an ITEM in room
        subjectinroomperson = self.location.getCharacterByName(subject)#If subject is an NPC in room
        subjectisbarrierinroom = self.location.getBarrierByName(subject)
        if subjectininventory or subjectinroomitem or subjectinroomperson or subjectisbarrierinroom:
            def checkAll(subject, opt1, opt2, opt3, opt4):
                if opt1: #Subject is an ITEM in INVENTORY
                    opt1.describe()
                elif opt2: #Subject is an ITEM in ROOM
                    opt2.describe()
                elif opt3: #Subject is an NPC in ROOM
                    opt3.describe()
                elif opt4:
                    opt4.describe()
                print()
            return checkAll(subject,subjectininventory,subjectinroomitem,subjectinroomperson,subjectisbarrierinroom)
        else:
            return False
        pass

    def useitem(self, subject): #Item should be in inventory. Use should depend on if it's a healing item, a note, or a key
        if subject.type == "healingItem":
            subject.heal(self)
        elif subject.type == "note":
            subject.read()#Item is not removed from inventory.
        elif subject.type == "key":
            subject.use(self.location)
            pass
        elif subject.type == "imbewedItem":
            subject.use(self)
            pass
        else:
            print("ERROR: Item attempted to be used seems to not exist!")
            input("Press enter to continue...")        

    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()
        input("Press enter to continue...")

    def showSpellsYouKnow(self):
        print("The magic spells you currently know are: ")
        placeholder = ""
        for i in self.magicknown:
            placeholder += i.name + ", "
        print(placeholder)

    def getItemByName(self, requesteditem):
        for i in self.items:
            if i.name.lower() == requesteditem:
                return i


    def getMagicSpellByName(self, name):
        for i in self.magicknown:
            if i.name == name.upper():
                return i
        return None

    def levelUp(self):
        self.level +=1
        self.expneedednextlevel +=3
        self.untilnextlevel = 0

        self.health += 10
        self.healthmax +=10
        self.mana += 10
        self.manamax += 10
        self.strength += 10
        self.strengthMagic += 10
        self.defense += 10
        print("\nCongrats! You have leveled up to level " + str(self.level) + "!!!!!!")

    def attackMonster(self, mon):
        #Keep this going, have monsters survive multiple hits and do their own actions.
        #Battles take multiple turns.
        #Options: Attack (STR), Magic (List of magic options), Talk (Gives description of monster, what they're saying/doing. Debuffs them?), Flee (End battle, you take some damage.)
        clear()
        print("You are attacking " + mon.name)
        print()

        def chancemonsterattackmagic():
            if random.randint(0,100) < (100*mon.magicLikelyhood): #Chance for monsters to respond by using magic
                monsterattack = mon.magicpw - self.defense
                if monsterattack < 0:
                    monsterattack = 0
                self.health -= monsterattack
                print("Casting a spell, the " +mon.name+ " hits you for "+ str(int(monsterattack)) + " Damage...")
            else:
                monsterattack = mon.attackpw - self.defense
                if monsterattack < 0:
                    monsterattack = 0
                self.health -= monsterattack
                print("The " +mon.name+ " hits you for "+ str(int(monsterattack)) + " Damage...")
            #self.checkifdead()



        def attackPhysical():
            #print("Your health is " + str(self.health) + ".")
            #print(mon.name + "'s health is " + str(mon.health) + ".")
            #print()
            
            playerattack = (self.strength - mon.defense) + random.randint(-10,10)
            if playerattack < 0:
                playerattack = 0

            print("[Attack]< \n\n")
            print("You hit " + mon.name + " for " +str(playerattack) + " Damage!")
            mon.health -= playerattack
            
            if mon.health <=0:
                print("You defeated the " + mon.name + "!!!!")
                mon.die()
            else:
                chancemonsterattackmagic()
            input("Press enter to continue...")

        def choicesinbattle():
            if self.alive == True:
                clear()
                print("Your health is now " + str(self.health) +"/"+str(self.healthmax))
                print("Your mana is now " + str(self.mana) +"/"+str(self.manamax))
                print(mon.name + "'s health is " + str(mon.health) + ".")
                print()

                choice = input("What will you do? \n\n[Attack]\n[Magic]\n[Item]\n[Talk]\n[Flee]\n\n>>> ")
                
                if choice.lower() == "attack":
                    attackPhysical()
                elif choice.lower() == "flee" or choice.lower() == "run":            #Coin flip if you get away or not. Flat out cannot run from witch fight
                    if mon.species == "Witch":
                        print("You can't run from a fight with a witch!!!")
                    elif mon.species == "TrapFamiliar":
                        print("You cannot flee from this fight!!!")
                    else:
                        print("[Flee]< \n\n")
                        if random.randint(0,1) == 1:
                            print("You were able to run from the fight!")
                            input("Press enter to continue...")
                            self.location = self.lastspot
                            return None
                        else:
                            print("You were unable to run!!!")
                            self.health -= 10
                            print("The " +mon.name+" hits you for 10 damage!!")
                            if self.health <=0:
                                print("And with that final minor attack, all your HP is gone! You've died!")
                                self.alive = False
                                return None
                    choicesinbattle()
                elif choice.lower() == "magic" or choice.lower == "spell":
                    print("[Magic]< \n\n")
                    self.showSpellsYouKnow()
                    print("Magic time! Type back if you'd rather not cast a spell.")
                    spellchoice = False
                    while not spellchoice:
                        spell = input("Which spell do you cast? ")
                        spellchoice =True
                        if spell.lower() == "" or spell.lower() == " ":
                            spellchoice = False
                            print("Please choose an actual spell to cast.")
                        elif spell.lower() == "back":
                            spellchoice = False
                            choicesinbattle()
                        else:
                            usespell = self.getMagicSpellByName(spell.lower())
                            if usespell != None:
                                if usespell.cost > self.mana:
                                    print("You are too low in mana to cast that spell!")
                                    input("Press enter to continue...")
                                    spellchoice = False
                                else:
                                    usespell.useMagic(mon)
                                    if mon.health <=0:
                                        print("You defeated the " + mon.name + "!!!!")
                                        mon.die()
                                    else:
                                        chancemonsterattackmagic()
                                    input("Press enter to continue...")
                            else:
                                print("That is not a spell you can cast.")
                                input("Press enter to continue...")
                                spellchoice = False
                elif choice.lower() == "item": 
                    print("[ITEM]< \n\n")
                    if self.items != []:
                        print("You are currently carrying:")
                        print()
                        for i in self.items:
                            print(i.name)
                        print()
                        target = input("What would you like to use?(Type \'exit\' to not use an item): ")
                        if target == "exit":
                            input("Press enter to continue...")
                        else:
                            target = self.getItemByName(target)
                            while target not in self.items and target != "exit":
                                target = input("Answer not possible. What would you like to use?(Type \'exit\' to not use an item): ")
                                if target == "exit":
                                    input("Press enter to continue...")
                                else:
                                    target = self.getItemByName(target)


                        if target == "exit":
                            input("Press enter to continue...")
                        else: 
                            if target.type == "healingItem":
                                self.useitem(target)
                                chancemonsterattackmagic()
                            else:
                                print("You can only use healing items in battle!")
                            input("Press enter to continue...")
                    else:
                        print("You do not have any items!")
                        input("Press enter to continue...")

                elif choice.lower() == "talk":
                    print("[TALK]< \n\n")
                    print(mon.name)
                    print(mon.desc + "\n")
                    if mon.species == "Witch":
                        print("As you try and talk to " +mon.name+", it starts to... Sob?")
                        mon.attackpw -=20
                        mon.magicpw -=20
                        mon.defense -=20
                        print("-20 to "+mon.name+" \'s Defense, Attack, and Magic Attack!!")
                        input("Press enter to continue...")
                        chancemonsterattackmagic()
                    else:#enemy fighting is NOT a witch
                        print("The monster does not seem to understand what you are saying...")
                        if random.randint(0,1) == 1:
                            mon.defense -=10
                            print("The monster laughs! It seems more relaxed around you. It's defense drops by 10!")
                        else:
                            print("The monster screeches at you, cutting you off mid sentence! It didn't seem to like what you had to say...")
                        input("Press enter to continue...")
                        chancemonsterattackmagic()

                else:
                    print("Invalid command. Please type something else.")
                    input("Press enter to continue...")
                    choicesinbattle()
        print(mon.desc)
        while self.health > 0 and mon.health >0 and self.location == mon.room:
            choicesinbattle()
        print()
        if mon.health <=0:
            print("You win!!!")
            print("Your health is now " + str(self.health) +"/"+str(self.healthmax))
            print("Your mana is now " + str(self.mana) +"/"+str(self.manamax))
            self.expneedednextlevel -=1
            if self.expneedednextlevel == 0:
                self.levelUp()
        elif self.health <=0:
            self.checkifdead()
        else:
            print("Your health is now " + str(self.health) +"/"+str(self.healthmax))
            print("Your mana is now " + str(self.mana) +"/"+str(self.manamax))

        input("Press enter to continue...")

        #Ask what sort of magic?
        #commandSuccess = False

        #while not commandSuccess:
            #commandSuccess = True
            #command = input("What sort of magic will you use? \n \n 
            #[Blind] \n [Ray of Sunshine] \n [Angelic Cacophany] #Light damage, effective against dark-type enemies
            #[Bash] \n [Kick into Gear] \n [Your Own Song] #Neutral damage, slightly more damage
            #[Shrowd] \n [Nightmare fuel] \n [Concerto of the Night]") #Dark damage, effective against light-type enemies
            #commandSplit = command.split()


class magicSpells():
    """docstring for magicSpells"""
    def __init__(self, player, name, minusmana, damage, element, description):
        self.name = str(name).upper()
        self.cost = minusmana
        self.user = player
        self.damage = damage
        self.element = element
        self.description = description
    def learnQuiet(self):
        #self.user.magicknown[self.name] = self
        self.user.magicknown.append(self)
    def learn(self):
        self.user.magicknown.append(self)
        print("You've learned how to use " +self.name + "!!!")
        input("Press enter to continue...")

    def isEffective(self, enemyType):
        #Enemy types: "Dark" , "Light" , "Neutral"
        #Return 0 if the spell is neutral, 1 if spell is effective, 2 if spell should be resisted
        if self.element == "Neutral":
            return 0
        elif self.element == "Dark" and enemyType == "Light":
            return 1
        elif self.element == "Light" and enemyType == "Dark":
            return 1
        elif self.element == "Dark" and enemyType == "Dark":
            return 2
        elif self.element == "Light" and enemyType == "Light":
            return 2
        else:
            return 0

    def useMagic(self, enemy):
        hurtsmonsterbad = self.isEffective(enemy.type)

        self.user.mana -= self.cost
        self.user.grief += 10
        print("You used " + self.name + "...")
        print(self.description)
        if hurtsmonsterbad == 1:
            damagedelt = int(((self.damage*self.user.strengthMagic) - enemy.defense)*1.5)
        elif hurtsmonsterbad ==2:
            damagedelt = int(((self.damage*self.user.strengthMagic) - enemy.defense)*0.5)
        else:
            damagedelt = (self.damage*self.user.strengthMagic) - enemy.defense
        enemy.health -= damagedelt
        print("\nYour spell did "+ str(int(damagedelt)) + " damage to the " +str(enemy.name)+ "!" )
        

