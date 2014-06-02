# Problem: Shuffle an array
# Solution: Knutt Yates Shuffle

#  Functions
import random
def shuffle(array):
    if not array:
        return

    for index in range(len(array) - 1, 0, -1):
        random_index = random.randint(0, index)
        swap(array, index, random_index)

def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp

# Main Program

input = [1, 2, 3, 4, 5]
print("Shuffling... %s" %input)
shuffle(input)
print("Output %s" %input)
