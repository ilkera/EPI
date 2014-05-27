# Problem: Binary Search

# Function - Search (Iterative)
def search(array, target):
    if not array:
        print("Empty array")

    high = len(array) - 1
    low = 0

    while low <= high:
        mid = int(low + (high - low) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Main Program

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Searching 2 in array found at index: %d" % (search(array, 2)))  # random
print("Searching 5 in array found at index: %d" % (search(array, 5)))  # mid
print("Searching 10 in array found at index: %d" % (search(array, 10)))  # last
print("Searching 14 in array found at index: %d" % (search(array, 14)))  # max
print("Searching 1 in array found at index: %d" % (search(array, 1)))  # first
print("Searching 0 in array found at index: %d" % (search(array, 0)))  # min
