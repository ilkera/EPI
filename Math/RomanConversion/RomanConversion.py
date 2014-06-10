# Problem: Roman to Integer, Integer to Roman conversion

# I = 1, IV = 4, V = 5, IX = 9, X =10, XL = 40, L = 50, XC = 90, C = 100, CD=400, D = 500, CM=900, M= 1000

# Functions

class RomanUtils:
    def __init__(self):
        self.roman_to_number_map = {
            "I":1 , "IV":4, "V":5, "IX":9, "X":10,
            "XL":40, "L":50, "XC":90, "C":100,
            "CD":400, "D":500, "CM":900, "M": 1000}

        self.number_to_roman_map = {
            1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X",
            40:"XL", 50:"L", 90:"XC", 100:"C",
            400:"CD", 500:"D", 900:"CM", 1000:"M"}

    def toRoman(self, number):
        if number < 1:
            raise ValueError

        result = []
        while number != 0:
            for current_roman_value in reversed(sorted(self.number_to_roman_map.keys())):
                while current_roman_value <= number:
                    result.append(self.number_to_roman_map[current_roman_value])
                    number -= current_roman_value

        return "".join(result)

    def toInteger(self, roman):
        if not roman:
            raise Exception("invalid/empty roman number")

        index, result = 0, 0

        while index < len(roman):
            if not roman[index] in self.roman_to_number_map:
                raise Exception("Invalid character")

            current_with_next = roman[index:index+2]
            if current_with_next in self.roman_to_number_map:
                result += self.roman_to_number_map[current_with_next]
                index += 2
            else:
                result += self.roman_to_number_map[roman[index]]
                index += 1

        return result


# Main program
romanUtil = RomanUtils()

for current in range(1, 1001):
    print(romanUtil.toRoman(current))

print(romanUtil.toInteger("XLIII"))  # 43
print(romanUtil.toInteger("DCCCXC"))  # 890
print(romanUtil.toInteger("XLVI"))  # 46
print(romanUtil.toInteger("LVIII"))  # 58
print(romanUtil.toInteger("XCII")) # 92
print(romanUtil.toInteger("IXX")) # 19




