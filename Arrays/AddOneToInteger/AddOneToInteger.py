# Problem : Add one to integer which is represented by an array
# e.g. [1, 2, 3] = 123  + 1 , Output: [1, 2, 4]

def addOne(integer):
    if not integer:
        return [1]

    carry = 1

    for index in range(len(integer) - 1, -1, -1):
        current_sum = integer[index] + carry
        integer[index] = current_sum % 10
        carry = int(current_sum / 10)

    if carry > 0:
        integer.insert(0, carry)

    return integer


# Main program
import unittest
class AddOneUnitTests(unittest.TestCase):

    def convertToNumber(self, number):
        result = []

        while True:
            result.append(number % 10)
            number = int(number / 10)

            if number == 0:
                break

        return list(reversed(result))

    def test_AddOne(self):
        for number in range(0, 1001):
            input = self.convertToNumber(number)
            print(input)
            self.assertEqual(addOne(input), self.convertToNumber(number + 1))
