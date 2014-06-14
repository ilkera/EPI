# Problem: Add two integer arrays
# e.g. [1,2,3] + [2,4,0] = [3,6,3]
# Assume numbers are positive

def sumInteger(first, second):
    if not first and not second:
        return None
    if not first:
        return second
    if not second:
        return first

    result = []
    carry = 0
    index_first, index_second = len(first) - 1, len(second) - 1

    while index_first >= 0 or index_second >= 0:
        if index_first >= 0 and index_second >= 0:
            current = first[index_first] + second[index_second] + carry
            index_first, index_second = index_first - 1, index_second - 1
        elif index_first >= 0:
            current = first[index_first] + carry
            index_first -= 1
        elif index_second >= 0:
            current = second[index_second] + carry
            index_second -= 1

        result.append(current % 10)
        carry = int(current / 10)

    if carry > 0:
        result.append(carry)

    return result[::-1]

print(sumInteger([1, 2, 3],  [2, 4, 0]))
print(sumInteger([1],  [9]))
print(sumInteger([9,9],  [3,2]))
print(sumInteger([1,0,0],  [5]))