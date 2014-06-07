# Problem: Flatten a list that has nested collection
# e.g. [1, 2, [3, [4, 5], 6], 8, [9, [10]]]

# Function
def flatten(list):
    return flatten_helper(list, [])

def flatten_helper(list, result):
    for item in list:
        if isinstance(item, type([])):
            flatten_helper(item, result)
        else:
            result.append(item)

    return result


import collections
def flatten_iterative(list):
    if not list:
        return []

    result, stack = [], []
    iterator = iter(list)

    while True:
        try:
            value = next(iterator)
        except StopIteration:
            if not stack:
                return result
            iterator = stack.pop()
        else:
            if isinstance(value, collections.Iterable):
                stack.append(iterator)
                iterator = iter(value)
            else:
                result.append(value)
    return result

# Main program
list = [1, 2, [3, [4, 5], 6], 7, 8, [9, [10]]]
result = flatten(list)
print(result)

result = flatten([[[[[[[[[[[[1]]]]]]]]]]]])
print(result)

result = flatten_iterative(list)
print(result)
