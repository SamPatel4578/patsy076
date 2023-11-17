import unittest
from A2_patsy076 import *

class TestPotionFunctions(unittest.TestCase):
       def setUp(self):
        self.herb1 = Herb("Irit", 3.5)
        self.catalyst1 = Catalyst("Eye of Newt", 4.3, 1.0)
        self.super_potion1 = SuperPotion("Super Attack", "Attack", 0, self.herb1, self.catalyst1)
        self.extreme_potion1 = ExtremePotion("Extreme Defense", "Defense", 0, self.herb1, self.super_potion1)

        self.laboratory = Laboratory()
        self.alchemist = Alchemist(0, 0, 0, 0, 0, 0)

       def test_potion_attributes(self):
        self.assertEqual(self.super_potion1.get_name(), "Super Attack")
        self.assertEqual(self.super_potion1.get_stat(), "Attack")
        self.assertEqual(self.super_potion1.get_boost(), 0)
        self.assertEqual(self.extreme_potion1.get_name(), "Extreme Defense")
        self.assertEqual(self.extreme_potion1.get_stat(), "Defense")
        self.assertEqual(self.extreme_potion1.get_boost(), 0)

       def test_potion_calculate_boost(self):
        self.super_potion1.calculate_boost()
        self.assertNotEqual(self.super_potion1.get_boost(), 0)
        self.extreme_potion1.calculate_boost()
        self.assertNotEqual(self.extreme_potion1.get_boost(), 0)


       def test_reagent_attributes(self):
        self.assertEqual(self.herb1.get_name(), "Irit")
        self.assertEqual(self.herb1.get_potency(), 3.5)
        self.assertEqual(self.catalyst1.get_name(), "Eye of Newt")
        self.assertEqual(self.catalyst1.get_potency(), 4.3)
        self.assertEqual(self.catalyst1.get_quality(), 1.0)