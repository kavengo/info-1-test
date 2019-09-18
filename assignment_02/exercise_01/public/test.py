import importlib
import unittest
import os
from unittest import TestCase
from unittest.mock import patch

devnull = open(os.devnull, 'w')

# Load once to enable reloading
# Patch input to pass input() values
# Path stdout and stderr to suppress writing to console for the tests
with patch('builtins.input', side_effect=[0]):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            from public import script as task_1_solution


def reload_module(user_input):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            with patch('builtins.input', side_effect=user_input):
                return importlib.reload(task_1_solution)


class Task1Test(TestCase):
    """
    Task 1: Test case with 20% promotion (promotion = 20)
    """

    def setUp(self):
        user_input = [20]
        self.exercise = reload_module(user_input)

    def test_subtotal(self):
        """20% Promotion - Test subtotal """
        self.assertTrue(hasattr(self.exercise, "subtotal_price"), "You must declare 'subtotal_price'")
        self.assertEqual(self.exercise.subtotal_price, 10, "'subtotal_price' value seems wrong")

    def test_savings(self):
        """20% Promotion - Test savings """
        self.assertTrue(hasattr(self.exercise, "savings"), "You must declare 'savings'")
        self.assertEqual(self.exercise.savings, 2, "'savings' value seems wrong")

    def test_total_price(self):
        """20% Promotion - Test total price """
        self.assertTrue(hasattr(self.exercise, "total_price"), "You must declare 'total_price'")
        self.assertEqual(self.exercise.total_price, 8, "'total_price' value seems wrong")

    def test_number_balls(self):
        """No Promotion - Test number of balls """
        self.assertTrue(hasattr(self.exercise, "number_of_balls"), "You must declare 'number_of_balls'")
        self.assertEqual(self.exercise.number_of_balls, 9, "'number_of_balls' value seems wrong")


if __name__ == '__main__':
    unittest.main(verbosity=0)
