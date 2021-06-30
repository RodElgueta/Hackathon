# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 18:49:05 2021

@author: rofun
"""
#Cardlist = []
class Card:
    
    def __init__(self, name, cost, player):
        self.name = name
        self.cost = cost
        self.player = player
        #Cardlist.append(self)
        
    
        
        
        
class Creature(Card):
    
    def __init__(self, name, cost, power, hp, player):
        super().__init__(name, cost, player)
        self.power = power
        self.hp = hp

    
    def Attack(self, target):

        if isinstance(target, Creature):
            target.hp -= self.power
        else:
            raise Exception( "Target must be a unit!")
            
    '''def Dead(self):
        Cardlist.remove(self)'''



class Spell(Card):
    
    def __init__(self, name, cost, stat, magnitude, player):
        super().__init__(name, cost, player)   
        self.stat = stat
        self.magnitude = magnitude
        self.lasttarget = None
    
    def PlaySpell(self, target):
        self.lasttarget = target
        if isinstance(target, Creature):
            if self.stat == "hp":
                target.hp += self.magnitude
            else:
                target.power += self.magnitude
        else:
            raise Exception( "Target must be a unit!")

        
