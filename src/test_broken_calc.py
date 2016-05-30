import unittest
from broken_calc import *

class AddTestCase(unittest.TestCase):
    """Tests for add"""

    #def test_is_five_prime(self):
    #    """Is five successfully determined to be prime?"""
    #    self.assertTrue(is_prime(5))
    def test_add_scenario_1(self):
        self.assertEqual(5,broken_add(3,3))
    def test_add_scenario_2(self):
        self.assertEqual(10,broken_add(5,6))
    def test_add_scenario_3(self):
        self.assertEqual(15,broken_add(2,3))
  

#if __name__ == '__main__':
#    unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(AddTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)

