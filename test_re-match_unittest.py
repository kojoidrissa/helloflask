'''
To run test:
    python test_re-match_unittest.py
    python test_re-match_unittest.py -v
'''

import unittest
from re_match import input_valid

class TestRE_match(unittest.TestCase):

    def setUp(self):
        pass

    def test_leading_single_0(self):
        self.assertEqual( input_valid('0d8'), None)

    def test_trailing_single_0(self):
        self.assertEqual( input_valid('10d0'), None)

    def test_trailing_0(self):
        self.assertEqual(input_valid('10d01'), None)

if __name__ == '__main__':
    unittest.main()