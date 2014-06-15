# Problem: String permutation
# e.g. In: ['a', 'b', 'c']
# out ['a','b','c'] , ['a'.'c','b'] , ['b','a','c'] , ['b','c','a'] , ['c','a','b'] , ['c','b','a']

def permute(current):
    if not current:
        return []

    result = []
    permute_helper(current, 0, result)

    return result

def swap(array, source, dest):
    temp = array[source]
    array[source] = array[dest]
    array[dest] = temp

def permute_helper(current, index, result):
    if index == len(current):
        result.append(current[:])
        return

    for current_index in range(index, len(current)):
        swap(current, index, current_index)
        permute_helper(current, index + 1, result)
        swap(current, index, current_index)

# Main program
print(permute(['a','b','c']))



