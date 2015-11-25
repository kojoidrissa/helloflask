'''
To run test:
    python test_re-match_unittest.py
    python test_re-match_unittest.py -v
'''

import unittest
from re_match import input_valid

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual( multiply(3,4), 12)

    def test_strings_a_3(self):
        self.assertEqual( multiply('a',3), 'aaa')

if __name__ == '__main__':
    unittest.main()