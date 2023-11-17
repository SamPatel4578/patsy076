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
    def __init__(self, name, stat, boost):
        self.__name = name 
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculate_boost(self):
        pass

    def get_name(self):
        return self.__name

    def get_stat(self):
        return self.__stat

    def get_boost(self):
        return self.__boost

    def set_boost(self, new_boost):
        self.__boost = new_boost

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


class ExtremePotion(Potion):
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
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, newPotency):
        self.__potency = newPotency

class Herb(Reagent):
    def _init_(self, name, potency, grimy = True):
        super()._init_(name, potency)
        self.__grimy = grimy

    def refine(self):
        self.setGrimy()
        self.__potency = self.__potency * 2.5
        print(f"The herb potency will increase 2.5 times its original and its not grimy")

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy):
        self.__grimy = False

class Catalyst(Reagent):
    def _init_(self, name, potency, quality):
        super()._init_(name, potency)
        self.__quality = quality

    def refine(self):
       if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"Quality of the herb has increased by 1.1 The new quality is {self.__quality}")

       elif self.__quality >= 8.9:
           self.__quality = 10
           print(f"The quality of the herb is at its maximum: {self.__quality}. It cannot be refined any furthur.")

    def getQuality(self):
       return self.__quality

class Laboratory:
    def _init_(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        if type == "Super":
            potion = SuperPotion(name, stat, primaryIngredient, secondaryIngredient)
        elif type == "Extreme":
            potion = ExtremePotion(name, stat, primaryIngredient, secondaryIngredient)
        self.__potions.append(potion)
        return potion 

    def addReagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            for herb in range(0, amount-1):
                self.__herbs.append(reagent)
        elif isinstance(reagent, Catalyst):
            for catalyst in range(0, amount-1):
                self.__catalysts.append(reagent)
        return f"The reagent {reagent} was added successfully."


class Alchemist:
       def _init_(self, attack, strength, defense, magic, ranged, necromancy):
        self.__attributes = {"attack":attack, "strength":strength, "defense":defense, "magic":magic, "ranged":ranged, "necromancy":necromancy}
        self.__laboratory = Laboratory()
        self.__recipes = {}

        def getLaboratory(self):
            return self.__laboratory

        def getRecipes(self):
            return self.__recipes
    
        def addRecipe(self, potion, firstIngredient, secondIngredient):
            for key, value in self.__attributes.items():
                self.__recipes[potion] = (firstIngredient, secondIngredient)
                print(f"The recipe for {potion} was added successfully")
    
        def mixPotion(self, recipe):
            recipe.mixPotion()

        def drinkPotion(self, potion):
            pass

        def collectReagent(self, reagent, amount):
            pass

        def refineReagents(self):
            pass