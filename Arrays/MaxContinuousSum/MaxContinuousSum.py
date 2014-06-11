# Problem: Find the contiguous subsequence of integers in an integer array with the largest sum

# Functions
def maxContinuousSum(array):
    if not array:
        return 0

    current_sum, max_so_far = 0, 0

    for number in array:
        current_sum = max(number, current_sum + number)
        max_so_far = max(current_sum, max_so_far)

    return max_so_far

def get_maxContinuousSumElements(array):
    if not array:
        return []

    begin, end = 0, 0
    current_sum, previous_sum, max_so_far = 0, 0, 0

    for index, number in enumerate(array):
        current_sum = max(number, current_sum + number)

        if current_sum > 0:
           if current_sum > previous_sum and previous_sum <= 0:
               begin = index

           if current_sum > max_so_far:
               end = index
               max_so_far = current_sum

        previous_sum = current_sum

    return array[begin:end + 1]

# Main program
array = [4, 1, -5, 0, 3, 4, -2, 3, -5, 2]
print(maxContinuousSum(array))
print(get_maxContinuousSumElements(array))
