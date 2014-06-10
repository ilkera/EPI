# Problem: Factorial

# Functions
def factorial(number):
    if number < 0:
        raise ValueError
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)

def factorial_iterative(number):
    if number < 0:
        raise ValueError

    if number == 0 or number == 1:
        return 1

    result = 1
    current = 2

    while current <= number:
        result *= current
        current += 1

    return result

# Main program
print("Fact of %d is %d" %(5, factorial(5)))
print("Fact of %d is %d" %(5, factorial_iterative(5)))

