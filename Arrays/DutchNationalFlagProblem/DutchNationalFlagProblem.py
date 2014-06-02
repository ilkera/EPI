# Problem: Dutch National Flag Problem
# e.g. {1, 3, 1, 2, 3, 2, 1, 2} => {2, 2, 2, 1, 1, 1, 3, 3}

# Functions

def swap(list, first, second):
    temp = list[first]
    list[first] = list[second]
    list[second] = temp

def arrange(list):
    if not list:
        print("Nothing to arrange")

    left = 0
    current = 0
    right = len(list) - 1

    while current <= right:
        if list[current] == 2:
            swap(list, current, left)
            left += 1
            current += 1
        elif list[current] == 3:
            swap(list, current, right)
            right -= 1
        elif list[current] == 1:
            current += 1

# Main Program
input = [1, 3, 1, 2, 3, 2, 1, 2]
print("%s" %input)

arrange(input)
print("%s" %input)