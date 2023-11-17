import unittest
from A2_patsy076 import *

class TestPotionClasses(unittest.TestCase):

    def test_super_potion_creation(self):
        herb = Herb("Irit", 5.0)
        catalyst = Catalyst("Eye of Newt", 3.0, 7.0)

        super_potion = SuperPotion("Super Attack", "Attack", 0, herb, catalyst)

        self.assertEqual(super_potion.get_name(), "Super Attack")
        self.assertEqual(super_potion.get_stat(), "Attack")
        self.assertEqual(super_potion.get_herb(), herb)
        self.assertEqual(super_potion.get_catalyst(), catalyst)

    def test_extreme_potion_creation(self):
        herb = Herb("Avantoe", 8.0)
        super_potion = SuperPotion("Super Attack", "Attack", 0, herb, Catalyst("Eye of Newt", 3.0, 7.0))

        extreme_potion = ExtremePotion("Extreme Attack", "Attack", 0, herb, super_potion)

        self.assertEqual(extreme_potion.get_name(), "Extreme Attack")
        self.assertEqual(extreme_potion.get_stat(), "Attack")
        self.assertEqual(extreme_potion.get_reagent(), herb)
        self.assertEqual(extreme_potion.get_potion(), super_potion)

    def test_herb_refine(self):
        herb = Herb("Irit", 5.0)
        herb.refine()

        self.assertEqual(herb.get_grimy(), False)
        self.assertAlmostEqual(herb.get_potency(), 12.5, places=2)

    def test_catalyst_refine(self):
        catalyst = Catalyst("Eye of Newt", 3.0, 7.0)
        catalyst.refine()

        self.assertAlmostEqual(catalyst.get_quality(), 8.1, places=2)



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
        self.reagent = Herb("TestReagent", 2.0, grimy=False)
        self.potion = SuperPotion("TestPotion", "TestStat", 1.0, Herb("TestHerb", 2.0), Catalyst("TestCatalyst", 2.0, 5.0))

        self.extreme_potion = ExtremePotion("TestExtremePotion", "TestStat", 0, self.reagent, self.potion)

    def test_calculate_boost(self):
        self.extreme_potion.calculate_boost()
        expected_boost = round((self.reagent.get_potency() * self.potion.get_boost()) * 3.0, 2)
        self.assertEqual(self.extreme_potion.get_boost(), expected_boost)

    def test_get_reagent(self):
        self.assertEqual(self.extreme_potion.get_reagent(), self.reagent)

    def test_get_potion(self):
        self.assertEqual(self.extreme_potion.get_potion(), self.potion)

class TestReagent(unittest.TestCase):
    class ConcreteReagent(Reagent):
        def refine(self):
            raise NotImplementedError("ConcreteReagent subclass must implement refine method")

    def setUp(self):
        self.reagent = self.ConcreteReagent("Test Reagent", 10.0)

    def test_get_name(self):
        self.assertEqual(self.reagent.get_name(), "Test Reagent")

    def test_get_potency(self):
        self.assertEqual(self.reagent.get_potency(), 10.0)

    def test_set_potency(self):
        self.reagent.set_potency(20.0)
        self.assertEqual(self.reagent.get_potency(), 20.0)

    def test_refine(self):
        with self.assertRaises(NotImplementedError):
            self.reagent.refine()



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


class TestLaboratory(unittest.TestCase):

    def setUp(self):
        self.laboratory = Laboratory()

    def test_mix_super_potion(self):
        herb = Herb("Irit", 5.0)
        catalyst = Catalyst("Eye of Newt", 3.0, 7.0)

        potion = self.laboratory.mix_potion("Super Attack", "Super", "Attack", herb, catalyst)

        self.assertIsInstance(potion, SuperPotion)
        self.assertEqual(potion.get_name(), "Super Attack")
        self.assertEqual(potion.get_stat(), "Attack")

    def test_mix_extreme_potion(self):
        herb = Herb("Avantoe", 8.0)
        super_potion = SuperPotion("Super Attack", "Attack", 0, herb, Catalyst("Eye of Newt", 3.0, 7.0))

        potion = self.laboratory.mix_potion("Extreme Attack", "Extreme", "Attack", herb, super_potion)

        self.assertIsInstance(potion, ExtremePotion)
        self.assertEqual(potion.get_name(), "Extreme Attack")
        self.assertEqual(potion.get_stat(), "Attack")

    def test_add_herbs(self):
        herb = Herb("Irit", 5.0)

        self.laboratory.add_reagent(herb, 3)

        self.assertEqual(len(self.laboratory._Laboratory__herbs), 3)

    def test_add_catalysts(self):
        catalyst = Catalyst("Eye of Newt", 3.0, 7.0)

        self.laboratory.add_reagent(catalyst, 2)

        self.assertEqual(len(self.laboratory._Laboratory__catalysts), 2)


class TestAlchemist(unittest.TestCase):

    def setUp(self):
        # Initialize an Alchemist object with sample attributes
        self.alchemist = Alchemist(10, 15, 20, 25, 30, 35)

    def test_get_laboratory(self):
        # Test the get_laboratory method
        laboratory = self.alchemist.get_laboratory()
        self.assertIsInstance(laboratory, Laboratory)

    def test_get_recipes(self):
        # Test the get_recipes method
        recipes = self.alchemist.get_recipes()
        self.assertIsInstance(recipes, dict)
        self.assertGreater(len(recipes), 0)


    def test_drink_invalid_potion(self):
        # Test drinking an invalid potion
        invalid_potion = "Invalid Potion"  # Replace this with an invalid Potion object
        boost = self.alchemist.drink_potion(invalid_potion)
        self.assertIsNone(boost)

if __name__ == '__main__':
    unittest.main()

