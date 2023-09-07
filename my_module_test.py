import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_mixed_numbers(self):
        result = add(2, -3)
        self.assertEqual(result, -1)

    def test_subtract_positive_numbers(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtract_negative_numbers(self):
        result = subtract(-5, -3)
        self.assertEqual(result, -2)

    def test_subtract_mixed_numbers(self):
        result = subtract(5, -3)
        self.assertEqual(result, 8)

    def test_multiply_positive_numbers(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_multiply_negative_numbers(self):
        result = multiply(-2, -3)
        self.assertEqual(result, 6)

    def test_multiply_mixed_numbers(self):
        result = multiply(2, -3)
        self.assertEqual(result, -6)

    def test_divide_positive_numbers(self):
        result = divide(6, 2)
        self.assertEqual(result, 3)

    def test_divide_negative_numbers(self):
        result = divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_mixed_numbers(self):
        result = divide(6, -2)
        self.assertEqual(result, -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
