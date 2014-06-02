# Problem: Find a fibonacci sequence
# e.g. 0 1 1 2 3 5 8 13 21 ....

# Functions
def fibo_recursive(number):
    if number < 0:
        raise BaseException("Fibonacci starts from 1")

    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibo_recursive(number - 1) + fibo_recursive(number - 2)

def fibo_recursive_cache(number):
    if number < 0:
        raise BaseException("Fibonacci starts from 1")

    if number == 0:
        return 0

    if number == 1:
        return 1

    cache = [0] * (number + 1)
    cache[0] = 0
    cache[1] = 1

    return fibo_recursive_cache_helper(number, cache)

def fibo_recursive_cache_helper(number, cache):
    if number < 1:
        return 0

    if cache[number]:
        return cache[number]

    computed_fibo = fibo_recursive_cache_helper(number - 1, cache) + fibo_recursive_cache_helper(number - 2, cache)
    cache[number] = computed_fibo

    return cache[number]


def fibo_iterative(number):
    if number < 0:
        raise BaseException("Fibonacci starts from 1")

    if number == 0:
        return 0
    if number == 1:
        return 1

    current, first, second = 1, 0, 1

    while current < number:
       sum = first + second
       first = second
       second = sum
       current += 1
    return second

# Main function

import time

number = 32
print("Fibonacci recursive")
start_time = time.time()
print("Fibo of %d is %d" %(number, fibo_recursive(number)))
end_time = time.time()
print("Elapsed time: %.gs" %(end_time - start_time))

print("Fibonacci recursive with cache")
start_time = time.time()
print("Fibo of %d is %d" %(number, fibo_recursive_cache(number)))
end_time = time.time()
print("Elapsed time: %.gs" %(end_time - start_time))

print("Fibonacci iterative")
start_time = time.time()
print("Fibo of %d is %d" %(number, fibo_iterative(number)))
end_time = time.time()
print("Elapsed time: %.gs" %(end_time - start_time))
