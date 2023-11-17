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
        self._name = name 
        self._stat = stat
        self._boost = boost

    @abstractmethod
    def calculate_boost(self):
        pass

    def get_name(self):
        return self._name

    def get_stat(self):
        return self._stat

    def get_boost(self):
        return self._boost

    def set_boost(self, new_boost):
        self._boost = new_boost

class SuperPotion(Potion):
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self._herb = herb
        self._catalyst = catalyst
        self.calculate_boost()

    def calculate_boost(self):
        self.set_boost(round(self._herb.get_potency() + (self._catalyst.get_potency() * self._catalyst.get_quality()) * 1.5, 2))

    def get_herb(self):
        return self._herb

    def get_catalyst(self):
        return self._catalyst

class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self._reagent = reagent
        self._potion = potion

    def calculate_boost(self):
        self.set_boost(round((self._reagent.get_potency() * self._potion.get_boost()) * 3.0, 2))

    def get_reagent(self):
        return self._reagent

    def get_potion(self):
        return self._potion
    
class Reagent(ABC):
    def __init__(self, name, potency):
        self._name = name
        self._potency = potency

    @abstractmethod
    def refine(self):
        pass

    def get_name(self):
        return self._name

    def get_potency(self):
        return self._potency

    def set_potency(self, new_potency):
        self._potency = new_potency


class Herb(Reagent):
    def __init__(self, name, potency, grimy=True):
        super().__init__(name, potency)
        self._grimy = grimy

    def refine(self):
        self.set_grimy()
        self._potency = self._potency * 2.5 
        print(f"The herb is not grimy, and its potency is 2.5 times its original.")

    def get_grimy(self):
        return self._grimy

    def set_grimy(self, grimy=False):
        self._grimy = grimy

class Catalyst(Reagent):
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self._quality = quality

    def refine(self):
        if self._quality < 8.9:
            self._quality += 1.1
            print(f"Quality of the herb has increased by 1.1. The new quality is {self._quality}")

        elif self._quality >= 8.9:
            self._quality = 10
            print(f"The quality of the herb is at its maximum: {self._quality}. It cannot be refined any further.")

    def get_quality(self):
        return self._quality

class Laboratory:
    def __init__(self):
        self._potions = []
        self._herbs = []
        self._catalysts = []

    def mix_potion(self, name, type, stat, primary_ingredient, secondary_ingredient):
        if type == "Super" and (isinstance(primary_ingredient, Herb) or isinstance(primary_ingredient, Catalyst)) and (isinstance(secondary_ingredient, Herb) or isinstance(secondary_ingredient, Catalyst)): 
            potion = SuperPotion(name, stat, 0, primary_ingredient, secondary_ingredient)
            potion.calculate_boost
        elif type == "Extreme" and (isinstance(primary_ingredient, Herb) or isinstance(primary_ingredient, Catalyst)) and (isinstance(secondary_ingredient, SuperPotion)):
            potion = ExtremePotion(name, stat, 0, primary_ingredient, secondary_ingredient)
        self._potions.append(potion)
        return potion 

    def add_reagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            for herb in range(0, amount-1):
                self._herbs.append(reagent)
        elif isinstance(reagent, Catalyst):
            for catalyst in range(0, amount-1):
                self._catalysts.append(reagent)
        return f"The reagent {reagent} was added successfully."


class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy):
        self._attributes = {"attack": attack, "strength": strength, "defense": defense, "magic": magic, "ranged": ranged, "necromancy": necromancy}
        self._laboratory = Laboratory()
        self._recipes = {"Super Attack" : ["Irit", "Eye of Newt"], "Super Strength" : ["Kwuarm", "Limpwurt Root"], "Super Defense" : ["Cadantine", "White Berries"], 
                          "Super Magic" : ["Lantadyme, Potato Cactus"],"Super Ranging" : ["Dwarf Weed", "Wine of Zamorak"], "Super Necromancy" : ["Arbuck", "Blood of Orcus"], 
                          "Extreme Attack" : ["Avantoe", "Super Attack"], "Extreme Strength" : ["Dwarf Weed", "Super Strength"],
                          "Extreme Defense" : ["Lantadyme", "Super Defense"], "Extreme Magic" : ["Ground Mud Rune", "Super Magic"], 
                          "Extreme Ranging" : ["Grenwall Spike", "Super Ranging"], "Extreme necromancy" : ["Ground Miasma Rune", "Super Necromancy"]}

    def get_laboratory(self):
        return self._laboratory

    def get_recipes(self):
        return self._recipes
    
    def mix_potion(self, recipe):
        if recipe in self._recipes:
            primary_ingredient = recipe[0]
            secondary_ingredient = recipe[1]
            stat = None

            if "Super" in recipe:
                type = "Super"
            else:
                type = "Extreme"

            potion = self._laboratory.mix_potion(recipe, type, stat, primary_ingredient, secondary_ingredient)
            print(f"The potion {recipe} was successfully created.")

        else:
            print(f"Invlaid recipe.")

            

    def drink_potion(self, potion):
        if isinstance(potion, Potion):
            boost = potion.calculate_boost()