# Problem: Reverse digits
# e.g. 123 =? 321

# Functions
def reverseDigits(number):
    if number > -10 and number < 10:
        return number

    is_negative = number < 0
    if is_negative:
        number = abs(number)

    result = 0

    while number:
        result = (10 * result) + (number  % 10)
        number = int(number / 10)

    if is_negative:
        result *= -1

    return result

# Main program
print(reverseDigits(123))
print(reverseDigits(10))
print(reverseDigits(-123))
print(reverseDigits(5))
print(reverseDigits(-5))
