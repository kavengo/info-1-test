import importlib
import os
import unittest
from unittest import TestCase, mock
from unittest.mock import patch

devnull = open(os.devnull, 'w')
# Load once to enable reloading
# Patch input to pass input() values
# Path stdout and stderr to suppress writing to console for the tests
with patch('builtins.input', side_effect=[0]):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            from public import script as task_2_a_solution


def reload_module(module, user_input=''):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            with patch('builtins.input', side_effect=user_input):
                return importlib.reload(module)


class Task2(TestCase):
    """
    Task 2
    """

    # Reloads the module with the same user input each time
    def setUp(self):
        self.exercise = reload_module(task_2_a_solution)


    def test_task_2_a(self):
        self.assertTrue(hasattr(self.exercise, "task_2_a"), "You must declare 'task_2_a'")
        self.assertEqual(self.exercise.task_2_a, 11, "'task_2_a' value seems wrong")

    def test_task_2_b(self):
        self.assertTrue(hasattr(self.exercise, "task_2_b"), "You must declare 'task_2_b'")
        self.assertEqual(self.exercise.task_2_b, 3, "'task_2_b' value seems wrong")


if __name__ == '__main__':
    unittest.main(verbosity=0)
