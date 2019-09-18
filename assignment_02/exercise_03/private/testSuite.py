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
            from public import script as task_2_b_solution


def reload_module(module, user_input=''):
    with patch('sys.stdout', devnull):
        with patch('sys.stderr', devnull):
            with patch('builtins.input', side_effect=user_input):
                return importlib.reload(module)


class Task3(TestCase):
    """
    Task 3
    """

    # Reloads the module with the same user input each time
    def setUp(self):
        user_input = ['heisenberg']
        self.exercise = reload_module(task_2_b_solution, user_input)

    def test_task_3_1(self):
        self.assertTrue(hasattr(self.exercise, "task_1"), "You must declare 'task_1'")
        self.assertTrue(self.exercise.task_1, "'task_1' value seems wrong")

    def test_task_3_2(self):
        self.assertTrue(hasattr(self.exercise, "task_2_p1"), "You must declare 'task_2_p1'")
        self.assertTrue(hasattr(self.exercise, "task_2_p2"), "You must declare 'task_2_p2'")
        self.assertEqual(self.exercise.task_2_p1, "he", "'task_2_p1' value seems wrong")
        self.assertEqual(self.exercise.task_2_p2, "rg", "'task_2_p2' value seems wrong")

    def test_task_3_3(self):
        self.assertTrue(hasattr(self.exercise, "task_3"), "You must declare 'task_3'")
        self.assertTrue(self.exercise.task_3, "'task_3' value seems wrong")

    def test_task_3_4(self):
        self.assertTrue(hasattr(self.exercise, "task_4"), "You must declare 'task_4'")
        self.assertTrue(self.exercise.task_4, "'task_4' value seems wrong")

    def test_task_3_5(self):
        self.assertTrue(hasattr(self.exercise, "task_5"), "You must declare 'task_5'")
        self.assertEqual(self.exercise.task_5, 'Python is cool!Python is cool!Python is cool!',
                         "'task_5' value seems wrong")
    def test_task_3_6(self):
        self.assertTrue(hasattr(self.exercise, "task_6"), "You must declare 'task_6'")
        self.assertEqual(self.exercise.task_6, '0.33', "'task_6' value seems wrong")


if __name__ == '__main__':
    unittest.main(verbosity=0)
