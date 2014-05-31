# Problem: 2Sum Problem
# e.g. Input: {1, -2, 3, 7, 2, 4, -3, 5, 12, 0}
# 2SUM(input, k=12)
# Result = {5,7}, {12,0}

# Functions

def twoSum(list, target):
    if not list:
        raise BaseException("list is empty")

    result = []
    seen = set()

    for number in list:
        if target - number in seen:
            result.append((number, target - number))
        else:
            seen.add(number)
    return result

def twoSum_v2(list, target):
    if not list:
        raise BaseException("list is empty")

    sorted_list = sorted(list)
    result = []
    low = 0;
    high = len(sorted_list) - 1

    while low < high:
        currentSum = sorted_list[low] + sorted_list[high]
        if currentSum == target:
            result.append((sorted_list[low], sorted_list[high]))
            low += 1
            high -= 1
        elif currentSum > target:
            high -= 1
        else:
            low += 1
    return result

# Main Program

input = [1, -2, 3, 7, 2, 4, -3, 5, 12, 0]
print("TwoSum V1")
print("%s" %twoSum(input, 12))
print("%s" %twoSum(input, 15))
print("%s" %twoSum(input, 20))

print("TwoSum V2")
print("%s" %twoSum_v2(input, 12))
print("%s" %twoSum_v2(input, 15))
print("%s" %twoSum_v2(input, 20))
