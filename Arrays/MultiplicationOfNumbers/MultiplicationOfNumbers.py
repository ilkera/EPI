# Problem: Multiplication of numbers
#There is an array A[N] of N numbers.
# You have to compose an array Output[N] such that Output[i] will be equal to multiplication of all the elements of A[N] except A[i].
#  Solve it without division operator and in O(n).

# For example Output[0] will be multiplication of A[1] to A[N-1]
#  and Output[1] will be multiplication of A[0] and from A[2] to A[N-1].

#Example:
#A: {4, 3, 2, 1, 2}
#OUTPUT: {12, 16, 24, 48, 24}

def multiply(array):
    if not array:
        return None

    result = [1] * len(array)
    left, right = 1, 1
    length = len(array)

    for index in range(0, len(array)):
        result[index] *= left
        result[length - index -1] *= right
        left *= array[index]
        right *= array[length - index-1]

    return result

# Main program
print(multiply([4, 3, 2, 1, 2]))
print(multiply([4, 3, 2, 0, 2]))