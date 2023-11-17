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

       def test_reagent_refine(self):
        self.herb1.refine()
        self.assertFalse(self.herb1.get_grimy())
        self.assertNotEqual(self.herb1.get_potency(), 3.5)

        self.catalyst1.refine()
        self.assertGreaterEqual(self.catalyst1.get_quality(), 1.0)

       def test_laboratory_mix_potion(self):
        potion_result = self.laboratory.mix_potion("Super Defense", "Super", "Defense", self.herb1, self.catalyst1)
        self.assertIsInstance(potion_result, SuperPotion)

       def test_alchemist_mix_potion(self):
        recipe = ["Extreme Magic", "Ground Mud Rune", "Super Magic"]
        self.alchemist.mix_potion(recipe)

       def test_alchemist_drink_potion(self):
        self.super_potion1.calculate_boost()
        boost_before = self.super_potion1.get_boost()
        self.alchemist.drink_potion(self.super_potion1)
        boost_after = self.super_potion1.calculate_boost()
        self.assertGreater(boost_after, boost_before)

       def test_alchemist_collect_reagent(self):
        self.alchemist.collect_reagent(self.herb1, 5)
        self.assertEqual(len(self.alchemist.get_laboratory()._herbs), 5)

       def test_alchemist_refine_reagents(self):
        refine_result = self.alchemist.refine_reagents()

if __name__ == '__main__':
    unittest.main()