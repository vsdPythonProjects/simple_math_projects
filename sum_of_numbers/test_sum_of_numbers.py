import pytest
import unittest
from unittest.mock import patch
from simple_math_projects.sum_of_numbers.sum_of_numbers import get_sum_of_two_numbers

class TestGetSumOfTwoNumbers(unittest.TestCase):

    @pytest.mark.run(order=1)
    @patch('builtins.input', side_effect=['5', '10'])
    def test_sum_positive_numbers(self, mock_input):
        self.assertEqual(get_sum_of_two_numbers(), 15)

    @pytest.mark.run(order=2)
    @patch('builtins.input', side_effect=['-5', '-10'])
    def test_sum_negative_numbers(self, mock_input):
        self.assertEqual(get_sum_of_two_numbers(), -15)

    @pytest.mark.run(order=3)
    @patch('builtins.input', side_effect=['5.5', '4.5'])
    def test_sum_floats(self, mock_input):
        self.assertEqual(get_sum_of_two_numbers(), 10.0)

    @pytest.mark.run(order=4)
    @patch('builtins.input', side_effect=['abc', '10'])
    def test_invalid_input(self, mock_input):
        self.assertIsNone(get_sum_of_two_numbers())

    @pytest.mark.run(order=5)
    @patch('builtins.input', side_effect=['5', 'abc'])
    def test_partial_invalid_input(self, mock_input):
        self.assertIsNone(get_sum_of_two_numbers())

if __name__ == '__main__':
    unittest.main()