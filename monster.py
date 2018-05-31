import random
import updater

class Monster:
    species = "Familiar"
    def __init__(self, name, health, room, attackpw, magicpw, defense, typestatus, desc): #Enemy types: "Dark" , "Light" , "Neutral"
        self.name = name
        self.health = health
        self.room = room
        self.attackpw = attackpw
        self.magicpw = magicpw
        self.defense = defense
        self.type = typestatus
        self.desc = desc
        room.addMonster(self)
        updater.register(self)
    def update(self):
        if random.random() < .3: #MAKE SURE THEY CAN'T GO INTO SAFEROOM ROOMS
            newroom = self.room.randomNeighbor()
            if newroom.typeofroom == "nightmareRoom" and newroom.enemytofight == True:
                return
            if newroom.typeofroom != "safeRoom" and newroom.typeofroom != "BossRoom":
                self.moveTo(newroom)
    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)
    def die(self):
        self.room.removeMonster(self)
        self.room.update()
        updater.deregister(self)

class Witch(Monster):
    """Witches are boss monsters, with a LOT more health and do a lot more damage. They do not leave their room."""
    species = "Witch"
    willUseMagic = True
    magicLikelyhood = 0.75
    def __init__(self, name, health, room, attackpw, magicpw, defense, typestatus, desc):
        self.name = name
        self.health = health
        self.room = room
        self.desc = desc
        self.attackpw = attackpw
        self.magicpw = magicpw
        self.defense = defense
        self.type = typestatus
        room.addMonster(self)
        updater.register(self)

    def update(self):
        pass
    def moveTo(self):
        pass

class Minion(Monster):
    species = "Familiar"
    willUseMagic = False
    magicLikelyhood = 0.25
    """docstring for Minion. Simple attacker, does not often use magic. Not very smart or strong. Lots of them."""


class Familiar(Monster):
    species = "Familiar"
    willUseMagic = True
    magicLikelyhood = 0.5

    """docstring for Familiar. Will use magic, is stronger. Fewer in number."""

class TrapMonster(Monster):
    species = "TrapFamiliar"
    willUseMagic = True
    magicLikelyhood = 0.6
    def __init__(self, name, health, room, attackpw, magicpw, defense, typestatus, desc):
        self.name = name
        self.health = health
        self.room = room
        self.attackpw = attackpw
        self.magicpw = magicpw
        self.defense = defense
        self.type = typestatus
        self.desc = desc
        self.room = room
    """Will do a TON of damage, not required to beat... but can give a lot of EXP. Overall though not worth it"""
    def discovered(self):
        print("[S L A M] ")
        print("\n A monster slams down into the room from seemingly nowhere! It roars, and charges at you!")
        print("[Note: You will not be able to leave until you attack this monster.]")
        self.room.addMonster(self)
        updater.register(self)
        pass
    def update(self):
        pass
    def moveTo(self):
        pass
        
        
        
        
