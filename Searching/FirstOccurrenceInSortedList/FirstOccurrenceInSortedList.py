# Problem: Search a first occurrence in a sorted list.
# e.g. [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 9] Search 6 => returns 7 (first index)

# Functions

def search(array, target):
    if not array:
        return -1

    if array[0] == target:
        return 0

    low, high = 0, len(array) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        if array[mid] == target:
            if mid > 0 and array[mid - 1] != target:
                return mid
            else:
                high = mid - 1
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# Main program
array = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 9]
print("Searching for %d - Index: %d" %(6, search(array, 6)))
print("Searching for %d - Index: %d" %(2, search(array, 2)))
print("Searching for %d - Index: %d" %(3, search(array, 3)))
print("Searching for %d - Index: %d" %(12, search(array, 12)))
