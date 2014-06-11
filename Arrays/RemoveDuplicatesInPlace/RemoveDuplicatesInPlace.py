# Problem: Remove duplicates in-place

# Functions
# Removes duplicates and returns the new length

def removeDuplicates(array):
    if not array:
        return 0

    current, lastCopyIndex = 1, 1
    sorted_array = sorted(array)

    while current < len(sorted_array):
        if sorted_array[current] == sorted_array[current-1]:
            current += 1
            continue

        sorted_array[lastCopyIndex] = sorted_array[current]
        lastCopyIndex += 1
        current += 1

    return lastCopyIndex

# Main program
array = [1]
print(removeDuplicates(array))

array = [1, 1]
print(removeDuplicates(array))

array = [1, 2, 1]
print(removeDuplicates(array))

array = [3, 1, 2]
print(removeDuplicates(array))

array = [5, 5, 5, 5, 5, 5]
print(removeDuplicates(array))

array = [3, 2, 1, 4, 2, 4, 5, 1]
print(removeDuplicates(array))





