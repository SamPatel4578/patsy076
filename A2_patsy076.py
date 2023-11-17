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
    """
    Abstract base class for potions.

    Attributes:
    - name (str): The name of the potion.
    - stat (str): The stat affected by the potion.
    - boost (float): The boost value of the potion.

    Methods:
    - calculate_boost(): Abstract method to calculate the boost of the potion.
    - get_name(): Returns the name of the potion.
    - get_stat(): Returns the stat affected by the potion.
    - get_boost(): Returns the boost value of the potion.
    - set_boost(new_boost): Sets a new boost value for the potion.
    """
    def __init__(self, name, stat, boost):
        self.__name = name 
        self.__stat = stat
        self.__boost = boost

    def get_name(self):
        return self.__name

    def get_stat(self):
        return self.__stat

    def get_boost(self):
        return self.__boost

    def set_boost(self, new_boost):
        self.__boost = new_boost

    @abstractmethod
    def calculate_boost(self):
        pass


class SuperPotion(Potion):
    """
    Class for SuperPotion, a type of Potion.

    Attributes:
    - name (str): The name of the potion.
    - stat (str): The stat affected by the potion.
    - boost (float): The boost value of the potion.
    - herb (Herb): The primary ingredient herb.
    - catalyst (Catalyst): The secondary ingredient catalyst.

    Methods:
    - calculate_boost(): Calculates the boost of the SuperPotion.
    - get_herb(): Returns the primary ingredient herb.
    - get_catalyst(): Returns the secondary ingredient catalyst.
    """
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst
        self.calculate_boost()

    def calculate_boost(self):
        boost = round(self.__herb.get_potency() + (self.__catalyst.get_potency() * self.__catalyst.get_quality()) * 1.5, 2)
        self.set_boost(boost)

    def get_herb(self):
        return self.__herb

    def get_catalyst(self):
        return self.__catalyst


class ExtremePotion(Potion):
    """
    Class for ExtremePotion, a type of Potion.

    Attributes:
    - name (str): The name of the potion.
    - stat (str): The stat affected by the potion.
    - boost (float): The boost value of the potion.
    - reagent (Reagent): The primary ingredient reagent.
    - potion (Potion): The secondary ingredient potion.

    Methods:
    - calculate_boost(): Calculates the boost of the ExtremePotion.
    - get_reagent(): Returns the primary ingredient reagent.
    - get_potion(): Returns the secondary ingredient potion.
    """
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
    """
    Abstract base class for reagents.

    Attributes:
    - name (str): The name of the reagent.
    - potency (float): The potency value of the reagent.

    Methods:
    - refine(): Abstract method to refine the reagent.
    - get_name(): Returns the name of the reagent.
    - get_potency(): Returns the potency value of the reagent.
    - set_potency(new_potency): Sets a new potency value for the reagent.
    """
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
    """
    Class for Herb, a type of Reagent.

    Attributes:
    - name (str): The name of the herb.
    - potency (float): The potency value of the herb.
    - grimy (bool): Indicates if the herb is grimy or not.

    Methods:
    - refine(): Refines the herb, doubling its potency.
    - get_grimy(): Returns True if the herb is grimy, False otherwise.
    - set_grimy(grimy): Sets the grimy status of the herb.
    """
    def __init__(self, name, potency, grimy=True):
        super().__init__(name, potency)
        self.__grimy = grimy

    def refine(self):
        self.set_grimy()
        self.set_potency(self.get_potency() * 2.5)
        print(f"The herb is not grimy, and its potency is 2.5 times its original.")

    def get_grimy(self):
        return self.__grimy

    def set_grimy(self, grimy=False):
        self.__grimy = grimy

class Catalyst(Reagent):
    """
    Class for Catalyst, a type of Reagent.

    Attributes:
    - name (str): The name of the catalyst.
    - potency (float): The potency value of the catalyst.
    - quality (float): The quality value of the catalyst.

    Methods:
    - refine(): Refines the catalyst, increasing its quality.
    - get_quality(): Returns the quality value of the catalyst.
    """
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

    def set_quality(self, new_quality):
        self.__quality = new_quality

class Laboratory:
    """
    Class for Laboratory.

    Attributes:
    - potions (list): List to store potions.
    - herbs (list): List to store herbs.
    - catalysts (list): List to store catalysts.

    Methods:
    - mix_potion(name, type, stat, primary_ingredient, secondary_ingredient): Mixes a potion in the laboratory.
    - add_reagent(reagent, amount): Adds reagent(s) to the laboratory.
    """
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mix_potion(self, name, type, stat, primary_ingredient, secondary_ingredient):
        if type == "Super" and (isinstance(primary_ingredient, Herb) or isinstance(primary_ingredient, Catalyst)) and (isinstance(secondary_ingredient, Herb) or isinstance(secondary_ingredient, Catalyst)): 
            potion = SuperPotion(name, stat, 0, primary_ingredient, secondary_ingredient)
            potion.calculate_boost()
        elif type == "Extreme" and (isinstance(primary_ingredient, Herb) or isinstance(primary_ingredient, Catalyst)) and (isinstance(secondary_ingredient, SuperPotion)):
            potion = ExtremePotion(name, stat, 0, primary_ingredient, secondary_ingredient)
        self.__potions.append(potion)
        return potion

    
    def add_reagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            for _ in range(amount):
                self.__herbs.append(reagent)
        elif isinstance(reagent, Catalyst):
            for _ in range(amount):
                self.__catalysts.append(reagent)
        return f"The reagent {reagent} was added successfully."

class Alchemist:
    """
    Class for Alchemist.

    Attributes:
    - attributes (dict): Dictionary to store alchemist attributes.
    - laboratory (Laboratory): Laboratory object.
    - recipes (dict): Dictionary to store potion recipes.

    Methods:
    - get_laboratory(): Returns the alchemist's laboratory.
    - get_recipes(): Returns the alchemist's potion recipes.
    - mix_potion(recipe): Mixes a potion using a recipe.
    - drink_potion(potion): Attempts to drink a potion.
    """
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
        recipe_tuple = tuple(recipe)

        if recipe_tuple in self.__recipes:
            primary_ingredient = self.__recipes[recipe_tuple][0]
            secondary_ingredient = self.__recipes[recipe_tuple][1]
            stat = None

            if "Super" in recipe_tuple:
                type = "Super"
            else:
                type = "Extreme"

            potion = self.__laboratory.mix_potion(recipe_tuple, type, stat, primary_ingredient, secondary_ingredient)
            print(f"The potion {recipe_tuple} was successfully created.")
        
            return potion
        else:
            print(f"Invalid recipe.")
            return None

    def drink_potion(self, potion):
        if isinstance(potion, Potion):
            boost = potion.calculate_boost()


# arbuck = Herb("Arbuck", 2.6)
# eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)

# alchemist = Alchemist(0, 0, 0, 0, 0, 0)

# alchemist.collectReagent(arbuck, 5)
# alchemist.collectReagent(eye_of_newt, 3)

# super_attack_potion = SuperPotion("Super Attack", "Super", "Attack", arbuck, eye_of_newt)
# mix_result = alchemist.mixPotion(super_attack_potion)
# print(mix_result)