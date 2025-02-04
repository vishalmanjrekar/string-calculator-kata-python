import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(self.calculator.add("5"), 5)

    def test_two_numbers_comma_delimited(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers_comma_delimited(self):
        self.assertEqual(self.calculator.add("1,2,3,4"), 10)


if __name__ == "__main__":
    unittest.main()
