from checker import Checker
import unittest
import pytest


class TestChecker(unittest.TestCase):
    test = Checker()

    def test_clean_div(self):
        self.assertEqual(self.test.clean_div(10, 5), True)

    def test_positive(self):
        self.assertEqual(self.test.positive(-5), False)
        self.assertEqual(self.test.positive(8), True)

