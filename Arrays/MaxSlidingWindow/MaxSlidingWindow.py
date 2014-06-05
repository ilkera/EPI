# Problem: Find maximum sliding window
#The array is [1 3 -1 -3 5 3 6 7], and w is 3.

#   Window position                Max
#   ---------------               -----
#   [1  3  -1] -3  5  3  6  7       3
#    1 [3  -1  -3] 5  3  6  7       3
#    1  3 [-1  -3  5] 3  6  7       5
#    1  3  -1 [-3  5  3] 6  7       5
#    1  3  -1  -3 [5  3  6] 7       6
#    1  3  -1  -3  5 [3  6  7]      7

# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]

def maxSlidingWindow(list, window):
    if not list:
        return []

    queue, result = [], []
    current = 0

    while current < len(list):
        if len(queue) != window:
            queue.append(list[current])
            current += 1
            continue

        max_in_window = max(queue)
        result.append(max_in_window)
        queue.pop(0)

    max_in_window = max(queue)
    result.append(max_in_window)

    return result

# Main program
input = [1, 3, -1, -3, 5, 3, 6, 7]
output = maxSlidingWindow(input, 3)
print(output)

