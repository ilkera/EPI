# Problem: Interconvert strings to integers

# Function
def toString(number):
    if not isinstance(number, int ):
        raise Exception("not an integer")

    isNegative = number < 0
    if isNegative:
        number = abs(number)

    buffer = []

    while True:
        remainder = number % 10
        buffer.append(chr(int(ord('0') + remainder)))
        number /= 10

        if int(number) == 0:
            break

    result = "".join(reversed(buffer))

    if isNegative:
            result = "-" + result

    return result

def toInteger(str):
    if not str:
        raise Exception("empty/null string")

    # Strip out whitespaces
    current_index = 0
    while current_index < len(str) and str[current_index] == " ":
        current_index += 1

    if current_index == len(str):
        raise Exception("Invalid string")

    isNegative = str[current_index] == "-"

    if isNegative:
        current_index += 1

    result = 0
    while current_index < len(str):

        if str[current_index] == " ":
            current_index += 1
            continue

        if ord(str[current_index]) < ord('0') or ord(str[current_index]) > ord('9'):
            raise Exception("Invalid character")

        result = (10 * result) + ord(str[current_index]) - ord('0')
        current_index += 1

    if isNegative:
        result *= -1

    return result


# Main program
print("To string")
print("%s " %toString(123))
print("%s " %toString(-123))
print("%s " %toString(1))
print("%s " %toString(0))
print("%s " %toString(-4))

try:
    print("%s " %toString("aa"))
except:
    pass

print("\nTo integer")
print("%s " %toInteger("123"))
print("%s " %toInteger("-123"))
print("%s " %toInteger("1"))
print("%s " %toInteger("0"))
print("%s " %toInteger("-4"))
print("%s " % toInteger("  123"))
print("%s " % toInteger("  123  "))

try:
    print("%s " % toInteger("  123 ab "))
except:
    pass