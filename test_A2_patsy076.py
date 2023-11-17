import unittest
from A2_patsy076 import *

class TestPotionClass(unittest.TestCase):
    def setUp(self):
        self.potion = Potion("TestPotion", "TestStat", 5)

    def test_get_name(self):
        self.assertEqual(self.potion.get_name(), "TestPotion")

    def test_get_stat(self):
        self.assertEqual(self.potion.get_stat(), "TestStat")

    def test_get_boost(self):
        self.assertEqual(self.potion.get_boost(), 5)

    def test_set_boost(self):
        self.potion.set_boost(10)
        self.assertEqual(self.potion.get_boost(), 10)

    def test_calculate_boost(self):
        with self.assertRaises(NotImplementedError):
            self.potion.calculate_boost()

class TestSuperPotionClass(unittest.TestCase):
    def setUp(self):
        self.herb = Herb("TestHerb", 3.0)
        self.catalyst = Catalyst("TestCatalyst", 4.0, 1.5)

        self.super_potion = SuperPotion("TestSuperPotion", "TestStat", 0, self.herb, self.catalyst)

    def test_calculate_boost(self):
        self.super_potion.calculate_boost()
        expected_boost = round(self.herb.get_potency() + (self.catalyst.get_potency() * self.catalyst.get_quality()) * 1.5, 2)
        self.assertEqual(self.super_potion.get_boost(), expected_boost)

    def test_get_herb(self):
        self.assertEqual(self.super_potion.get_herb(), self.herb)

    def test_get_catalyst(self):
        self.assertEqual(self.super_potion.get_catalyst(), self.catalyst)


class TestExtremePotionClass(unittest.TestCase):
    def setUp(self):
        self.reagent = Reagent("TestReagent", 2.0)
        self.potion = Potion("TestPotion", "TestStat", 1.0)

        self.extreme_potion = ExtremePotion("TestExtremePotion", "TestStat", 0, self.reagent, self.potion)

    def test_calculate_boost(self):
        self.extreme_potion.calculate_boost()
        expected_boost = round((self.reagent.get_potency() * self.potion.get_boost()) * 3.0, 2)
        self.assertEqual(self.extreme_potion.get_boost(), expected_boost)

    def test_get_reagent(self):
        self.assertEqual(self.extreme_potion.get_reagent(), self.reagent)

    def test_get_potion(self):
        self.assertEqual(self.extreme_potion.get_potion(), self.potion)

class TestReagentClass(unittest.TestCase):
    def setUp(self):
        self.reagent = Reagent("TestReagent", 2.0)

    def test_get_name(self):
        self.assertEqual(self.reagent.get_name(), "TestReagent")

    def test_get_potency(self):
        self.assertEqual(self.reagent.get_potency(), 2.0)

    def test_set_potency(self):
        self.reagent.set_potency(3.5)
        self.assertEqual(self.reagent.get_potency(), 3.5)


class TestHerbClass(unittest.TestCase):
    def setUp(self):
        self.herb = Herb("TestHerb", 3.0, True)

    def test_get_name(self):
        self.assertEqual(self.herb.get_name(), "TestHerb")

    def test_get_potency(self):
        self.assertEqual(self.herb.get_potency(), 3.0)

    def test_get_grimy(self):
        self.assertTrue(self.herb.get_grimy())

    def test_set_grimy(self):
        self.herb.set_grimy(False)
        self.assertFalse(self.herb.get_grimy())

    def test_refine(self):
        self.herb.refine()
        self.assertEqual(self.herb.get_potency(), 3.0 * 2.5)
        self.assertFalse(self.herb.get_grimy())

class TestCatalystClass(unittest.TestCase):
    def setUp(self):
        self.catalyst = Catalyst("TestCatalyst", 5.0, 7.0)

    def test_get_name(self):
        self.assertEqual(self.catalyst.get_name(), "TestCatalyst")

    def test_get_potency(self):
        self.assertEqual(self.catalyst.get_potency(), 5.0)

    def test_get_quality(self):
        self.assertEqual(self.catalyst.get_quality(), 7.0)

    def test_refine_quality_increase(self):
        self.catalyst.refine()
        self.assertEqual(self.catalyst.get_quality(), 7.0 + 1.1)

    def test_refine_quality_maximum(self):
        self.catalyst.set_quality(9.0)
        self.catalyst.refine()
        self.assertEqual(self.catalyst.get_quality(), 10.0)


class TestLaboratoryClass(unittest.TestCase):
    def setUp(self):
        self.laboratory = Laboratory()
        self.herb = Herb("TestHerb", 4.0)
        self.catalyst = Catalyst("TestCatalyst", 5.0, 7.0)

    def test_mix_super_potion(self):
        super_potion = self.laboratory.mix_potion("SuperTestPotion", "Super", "Attack", self.herb, self.catalyst)
        self.assertIsInstance(super_potion, SuperPotion)

    def test_mix_extreme_potion(self):
        extreme_potion = self.laboratory.mix_potion("ExtremeTestPotion", "Extreme", "Defense", self.herb, self.catalyst)
        self.assertIsInstance(extreme_potion, ExtremePotion)

    def test_add_herbs(self):
        result = self.laboratory.add_reagent(self.herb, 3)
        self.assertEqual(result, "The reagent TestHerb was added successfully.")
        self.assertEqual(len(self.laboratory._herbs), 3)

    def test_add_catalysts(self):
        result = self.laboratory.add_reagent(self.catalyst, 2)
        self.assertEqual(result, "The reagent TestCatalyst was added successfully.")
        self.assertEqual(len(self.laboratory._catalysts), 2)

class TestAlchemistClass(unittest.TestCase):
    def setUp(self):
        self.alchemist = Alchemist(10, 20, 30, 40, 50, 60)
        self.laboratory = Laboratory()
        self.herb = Herb("TestHerb", 4.0)
        self.catalyst = Catalyst("TestCatalyst", 5.0, 7.0)
        self.laboratory.add_reagent(self.herb, 3)
        self.laboratory.add_reagent(self.catalyst, 2)

    def test_mix_super_potion(self):
        recipe = ["Super Attack", "Irit", "Eye of Newt"]
        self.alchemist.mix_potion(recipe)
        self.assertEqual(len(self.alchemist.get_laboratory()._potions), 1)

    def test_mix_extreme_potion(self):
        recipe = ["Extreme Defense", "Dwarf Weed", "Super Defense"]
        self.alchemist.mix_potion(recipe)
        self.assertEqual(len(self.alchemist.get_laboratory()._potions), 1)

    def test_drink_potion(self):
        super_potion = SuperPotion("TestSuperPotion", "Attack", 0, self.herb, self.catalyst)
        super_potion.calculate_boost()
        self.alchemist.drink_potion(super_potion)
        self.assertEqual(self.alchemist._attributes['attack'], 10 + super_potion.get_boost())

unittest.main()