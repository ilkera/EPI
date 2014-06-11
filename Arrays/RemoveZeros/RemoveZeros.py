# Problem: Remove zeros in integer array

# Functions
def removeZeros(array):
    if not array:
        return array

    current, lastNonZeroIndex = 0, 0
    while current < len(array):
        if array[current] == 0:
            current += 1
            continue

        array[lastNonZeroIndex] = array[current]
        lastNonZeroIndex += 1
        current += 1

    return array[0:lastNonZeroIndex]

# Main program
array = [1, 0, 0, 3, 4, 2, 8]
print(array)
result = removeZeros(array)
print(result)

