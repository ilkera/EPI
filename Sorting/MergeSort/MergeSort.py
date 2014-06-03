# Sorting : Merge Sort

# Functions
def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    left_size, right_size = len(left) , len(right)

    while left_index < left_size and right_index < right_size:
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    if left:
            merged.extend(left[left_index:])

    if right:
            merged.extend(right[right_index:])

    return merged

def mergeSort(array):
    if len(array) < 2:
        return array

    mid_index = int(len(array) / 2)
    left = array[:mid_index]
    right = array[mid_index:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

# Main program
array = [6, 7, 4, 10, 3, 8, 1, 0, 9, 2, 5]
print("Printing: %s" %array)
merged = mergeSort(array)
print("Sorted: %s" %merged)


