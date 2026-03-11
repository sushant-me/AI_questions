""" Perform code coverage testing. """

import unittest
from your_module import your_function

class TestYourFunction(unittest.TestCase):
    def test_case_1(self):
        result = your_function(1, 2)
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = your_function(-1, 1)
        self.assertEqual(result, 0)

    def test_case_3(self):
        result = your_function(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()