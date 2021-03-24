import math
import unittest


class BasicCalculator:
    def validate_input(self, *args):
        """validates if paramaters are number or not

        Raises:
            ValueError: if all args are not numbers (int/float)
        """
        for num in args:
            if type(num) not in [int, float]:
                raise ValueError("Inputs have to be numbers")

    def add(self, a, b):
        self.validate_input(a, b)
        return a + b

    def substract(self, a, b):
        self.validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        self.validate_input(a, b)
        return a * b

    def divide(self, a, b):
        self.validate_input(a, b)
        if b == 0:
            raise ValueError("divisor must be non zero")
        return a / b


class ScientificCalculator(BasicCalculator):
    """Extends the BasicCalculator class to provide additional sin,cos and tan funtions"""

    def sin(self, rad):
        """returns sin of a number

        Args:
            d (int): radian

        Returns:
            int: sin of the input
        """
        self.validate_input(rad)
        return math.sin(rad)

    def cos(self, rad):
        """returns cos of a number

        Args:
            d (int): radian

        Returns:
            int: cos of the input
        """
        self.validate_input(rad)
        return math.cos(rad)

    def tan(self, rad):
        """returns tan of a number

        Args:
            d (int): radian

        Returns:
            int: tan of the input
        """
        self.validate_input(rad)
        return math.tan(rad)


class TestBasicCalculator(unittest.TestCase):
    def setUp(self):
        self.b = BasicCalculator()

    def test_add(self):
        self.assertEqual(self.b.add(1, 2), 3)
        self.assertEqual(self.b.add(-1, 2), 1)

    def test_substract(self):
        self.assertEqual(self.b.substract(1, 2), -1)
        self.assertEqual(self.b.substract(-1, 2), -3)

    def test_multiply(self):
        self.assertEqual(self.b.multiply(1, 2), 2)
        self.assertEqual(self.b.multiply(-1, 2), -2)

    def test_divide(self):
        self.assertEqual(self.b.divide(1, 2), 0.5)
        self.assertEqual(self.b.divide(-1, 2), -0.5)
        self.assertRaises(ValueError, self.b.divide, 2, 0)


class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        self.s = ScientificCalculator()

    def test_sin(self):
        self.assertAlmostEqual(self.s.sin(math.radians(0)), 0.0)
        self.assertAlmostEqual(self.s.sin(math.radians(90)), 1.0)
        self.assertRaises(ValueError, self.s.sin, '100')

    def test_cos(self):
        self.assertAlmostEqual(self.s.cos(math.radians(0)), 1.0)
        self.assertAlmostEqual(self.s.cos(math.radians(90)), 0.0)
        self.assertRaises(ValueError, self.s.cos, '100')

    def test_tan(self):
        self.assertAlmostEqual(self.s.tan(math.radians(0)), 0.0)
        self.assertAlmostEqual(self.s.tan(math.radians(45)), 1.0)
        self.assertAlmostEqual(self.s.tan(math.radians(180)), 0.0)
        self.assertRaises(ValueError, self.s.tan, '100')


if __name__ == "__main__":
    unittest.main()