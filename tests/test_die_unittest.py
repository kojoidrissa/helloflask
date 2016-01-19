'''
To run test:
    From local directory
        python test_re-match_unittest.py
        python test_re-match_unittest.py -v

    From top directory (w/ discovery)
        python -m unittest discover -v tests/

'''
import unittest
import random as rnd
from dice import Die

class TestDie(unittest.TestCase):
    def test_die_roll_in_range(self):
        die = Die(rnd.randint(1,100)) 
        self.assertIn(die.roll(), range(1, die.sides))

if __name__ == '__main__':
    unittest.main()