# Problem: Climb tree
# Function to compute the number of ways to climb a flight of n steps.
# Taking 1, 2, or 3 steps at a time. Do it in Linear time and constant space.
#  Example: n = 3. 1 1 1 1 2 2 1 3 Ans = 4

# Functions
def climb(number):
    if number < 0:
        return 0

    if number == 1 or number == 0:
        return 1

    return climb(number - 1) + climb(number -2) + climb(number-3)

def climb_iterative(number):
    if number < 0:
        return 0

    if number == 1 or number == 0:
        return 1

    one_step, two_step, three_step = 0, 1, 1
    current = 2

    while current <= number:
        result = one_step + two_step + three_step
        one_step = two_step
        two_step = three_step
        three_step = result
        current += 1

    return result

# Main program

for index in range(0,10):
    print("Climbing %d stairs in %d ways (recursive) %d ways (iterative)" %(index, climb(index), climb_iterative(index)))

