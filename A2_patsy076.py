"""
File: A2_patsy076.py
Description: This assignment is for Assignment 2 of Object-Oriented Programming.
Author: Saumya Patel
StudentID: 110402464
EmailID: patsy076@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
"""


from abc import ABC, abstractmethod

class Potion(ABC):
    def _init_(self, name, stat, boost):
        self.__name = name 
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        pass

    def getStat(self):
        pass

    def getBoost(self):
        pass 

    def setBoost(self, boost):
        pass

class SuperPotion(Potion):
    def _init_(self, name, stat, boost, herb, catalyst):
        super()._init_(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        pass

    def getHerb(self):
        pass

    def getCatalyst(self):
        pass


class ExtremePosition(Potion):
    def _init_(self, name, stat, boost, reagent, potion):
        super()._init_(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        pass

    def getReagent(self):
        pass

    def getPotion(self):
        pass

class Reagent(ABC):
    def _init_(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self):
        pass

    def setPotency(self, potency):
        pass

class Herb(Reagent):
    def _init_(self, name, potency, grimy = True):
        super()._init_(name, potency)
        self.__grimy = grimy

    def refine(self):
        pass

    def getGrimy(self):
        pass

    def setGrimy(self, grimy):
        pass

class Catalyst(Reagent):
    def _init_(self, name, potency, quality):
        super()._init_(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self):
        pass

class Laboratory:
    def _init_(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagent(self, reagent, amount):
        pass

class Alchemist:
    def _init_(self, attack, strength, defense, magic, ranged, necromancy):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = Laboratory(self)
        self.__recipes = {}

    def getLaboratory(self):
        pass

    def getRecipes(self):
        pass

    def mixPotion(self, recipe):
        pass

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagents(self):
        pass