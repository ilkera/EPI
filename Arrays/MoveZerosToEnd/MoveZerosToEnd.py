# Problem: Move zeros to end of array
# e.g. { 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}  -> {1, 9 , 8, 4, 2, 7, 6, 0, 0, 0, 0}

# Function
def pushZerosToEnd(list):
    if not list:
        print("Empty array")

    lastNonZeroIndex = 0
    for index in range(len(list)):
        if list[index] != 0:
            list[lastNonZeroIndex] = list[index]
            lastNonZeroIndex += 1

    while lastNonZeroIndex < len(list):
        list[lastNonZeroIndex] = 0
        lastNonZeroIndex += 1

    return list
# Main Program

list = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print("%s" %list)

result = pushZerosToEnd(list)
print("%s " %result)