'''
To run test:
    From local directory
        python test_re-match_unittest.py
        python test_re-match_unittest.py -v

    From top directory (w/ discovery)
        python -m unittest discover -v tests/
    
'''

import unittest
from re_match import input_valid

class TestRe_Match(unittest.TestCase):

    def setUp(self):
        pass

    def test_leading_single_0(self):
        self.assertIsNone(input_valid('0d8'))

    def test_trailing_single_0(self):
        self.assertIsNone( input_valid('10d0'))

    def test_trailing_0(self):
        self.assertIsNone(input_valid('10d01'))

    def test_valid_leading_single_0(self):
        self.assertIsNotNone (input_valid('10d8'))

if __name__ == '__main__':
    unittest.main()