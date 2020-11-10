# Importing our testing modules and the class we are testing
from checker import Checker
import unittest
import pytest


# Creating our testing class that will inherit from the unittest Testcase framework
class TestChecker(unittest.TestCase):
    # Instantiating an object of the Checker class
    test = Checker()

    # Our test to check if the correct boolean is returned when a number is and isn't cleanly divisible by the other
    def test_clean_div(self):
        self.assertEqual(self.test.clean_div(10, 5), True)
        self.assertEqual(self.test.clean_div(10, 4), False)

    # Our test to check if the correct boolean is returned when a positive and negative number are provided
    def test_positive(self):
        self.assertEqual(self.test.positive(-5), False)
        self.assertEqual(self.test.positive(8), True)

