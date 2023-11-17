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
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst
        self.calculate_boost()

    def calculate_boost(self):
        self.set_boost(round(self.__herb.get_potency() + (self.__catalyst.get_potency() * self.__catalyst.get_quality()) * 1.5, 2))

    def get_herb(self):
        return self.__herb

    def get_catalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculate_boost(self):
        self.set_boost(round((self.__reagent.get_potency() * self.__potion.get_boost()) * 3.0, 2))

    def get_reagent(self):
        return self.__reagent

    def get_potion(self):
        return self.__potion

class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def get_name(self):
        return self.__name

    def get_potency(self):
        return self.__potency

    def set_potency(self, new_potency):
        self.__potency = new_potency

class Herb(Reagent):
    def __init__(self, name, potency, grimy=True):
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        self.set_grimy()
        self.__potency = self.__potency * 2.5 
        print(f"The herb is not grimy, and its potency is 2.5 times its original.")

    def get_grimy(self):
        return self.__grimy

    def set_grimy(self, grimy=False):
        self.__grimy = grimy

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"Quality of the herb has increased by 1.1. The new quality is {self.__quality}")

        elif self.__quality >= 8.9:
            self.__quality = 10
            print(f"The quality of the herb is at its maximum: {self.__quality}. It cannot be refined any further.")

    def get_quality(self):
        return self.__quality

class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mix_potion(self, name, type, stat, primary_ingredient, secondary_ingredient):
        if type == "Super" and (isinstance(primary_ingredient, Herb) or isinstance(primary_ingredient, Catalyst)) and (isinstance(secondary_ingredient, Herb) or isinstance(secondary_ingredient, Catalyst)): 
            potion = SuperPotion(name, stat, 0, primary_ingredient, secondary_ingredient)
            potion.calculate_boost
        elif type == "Extreme" and (isinstance(primary_ingredient, Herb) or isinstance(primary_ingredient, Catalyst)) and (isinstance(secondary_ingredient, SuperPotion)):
            potion = ExtremePotion(name, stat, 0, primary_ingredient, secondary_ingredient)
        self.__potions.append(potion)
        return potion 

    def add_reagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            for herb in range(0, amount-1):
                self.__herbs.append(reagent)
        elif isinstance(reagent, Catalyst):
            for catalyst in range(0, amount-1):
                self.__catalysts.append(reagent)
        return f"The reagent {reagent} was added successfully."

class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy):
        self.__attributes = {"attack": attack, "strength": strength, "defense": defense, "magic": magic, "ranged": ranged, "necromancy": necromancy}
        self.__laboratory = Laboratory()
        self.__recipes = {"Super Attack" : ["Irit", "Eye of Newt"], "Super Strength" : ["Kwuarm", "Limpwurt Root"], "Super Defense" : ["Cadantine", "White Berries"], 
                          "Super Magic" : ["Lantadyme, Potato Cactus"],
                          "Super Ranging" : ["Dwarf Weed", "Wine of Zamorak"], "Super Necromancy" : ["Arbuck", "Blood of Orcus"], "Extreme Attack" : ["Avantoe", "Super Attack"], "Extreme Strength" : ["Dwarf Weed", "Super Strength"],
                          "Extreme Defense" : ["Lantadyme", "Super Defense"], "Extreme Magic" : ["Ground Mud Rune", "Super Magic"], 
                          "Extreme Ranging" : ["Grenwall Spike", "Super Ranging"], "Extreme necromancy" : ["Ground Miasma Rune", "Super Necromancy"]}

    def get_laboratory(self):
        return self.__laboratory

    def get_recipes(self):
        return self.__recipes
    
    def mix_potion(self, recipe):
        if recipe in self.__recipes:
            primary_ingredient = recipe[0]
            secondary_ingredient = recipe[1]
            stat = None

            if "Super" in recipe:
                type = "Super"
            else:
                type = "Extreme"

            potion = self.__laboratory.mix_potion(recipe, type, stat, primary_ingredient, secondary_ingredient)
            print(f"The potion {recipe} was successfully created.")

        else:
            print(f"Invlaid recipe.")

    def drink_potion(self, potion):
        if isinstance(potion, Potion):
            boost = potion.calculate

arbuck = Herb("Arbuck", 2.6)
eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

alchemist = Alchemist(0, 0, 0, 0, 0, 0)

alchemist.collectReagent(arbuck, 5)
alchemist.collectReagent(eye_of_newt, 3)

super_attack_potion = SuperPotion("Super Attack", "Super", "Attack", arbuck, eye_of_newt)
mix_result = alchemist.mixPotion(super_attack_potion)
print(mix_result)