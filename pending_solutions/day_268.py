""" Write unit tests using unittest. """

import unittest

class TestExample(unittest.TestCase):
    def test_example_function(self):
        # Arrange
        input_value = 5
        expected_result = 10
        
        # Act
        result = input_value * 2
        
        # Assert
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()