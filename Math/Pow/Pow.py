# Problem: Pow() - Implement Math.Pow()
# e.g. Pow(2,4) = 16

# Req
# Base can be negative (base < 0)
# Power can not be negative as well (power >= 0)

# Functions

class MathPower:
    def pow(self,base, power):

        if base == 0:
            if power == 0:
                return 1
            else:
                return 0

        if power == 0:
            return 1

        result = 1
        temp = base;

        while power != 0:
            if power % 2 == 1:
                result *= temp
            temp *= temp
            power = int(power / 2)

        return result


import unittest

class PowUnitTests(unittest.TestCase):
    def test_ReturnZeroWhenBaseIsZero(self):
        m = MathPower()
        self.assertEqual(0, m.pow(0,5))

    def test_ReturnOneWhenPowerIsZero(self):
        m = MathPower()
        self.assertEqual(1, m.pow(3,0))

    def test_ReturnOneWhenBaseAndPowerAreZero(self):
        m = MathPower()
        self.assertEqual(1, m.pow(0,0))

    def test_ReturnsBaseToPower(self):
        m = MathPower()
        base = 2
        powers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for power in powers:
             self.assertEqual(pow(2,power), m.pow(2,power))

    def test_NegativeBase(self):
         m = MathPower()
         self.assertEqual(-8, m.pow(-2,3))
         self.assertEqual(16, m.pow(-2,4))