# Problem: Given a sorted array, write a program to decide if two elements sum up to a third

def twoSum(array, left, right, target,  result):
    while left < right:
        sum = array[left] + array[right]
        if sum == target:
            result.append((array[left], array[right], target))
            left += 1
            right -= 1
        elif sum > target:
            right -= 1
        else:
            left += 1


def twoSumToThird(array):
    if not array:
        return []

    result = []
    current_index = len(array) - 1

    while current_index > 1:
        twoSum(array, 0, current_index - 1, array[current_index], result)
        current_index -= 1
    return result



# Main program
list = [1, 2, 3, 4, 5, 6, 7, 12, 19]
print(twoSumToThird(list))
