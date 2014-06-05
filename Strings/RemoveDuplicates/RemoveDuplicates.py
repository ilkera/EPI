# Problem: Remove duplicates in a string (in-place)
# e.g. In: "aabadcdc" => "abdc" -

# Functions

# aaabccdd

def removeDuplicates_OrderDoesNotMatter(str):
    if not str:
        return ""

    sorted_str = sorted(list(str))
    index = 1
    index_last_copy = 0

    while index < len(sorted_str):
        if sorted_str[index] == sorted_str[index - 1]:
            index += 1
            continue

        index_last_copy += 1
        sorted_str[index_last_copy] = sorted_str[index]
        index += 1

    for index in range(index_last_copy + 1, len(sorted_str)):
        sorted_str[index] =" "

    return "".join(sorted_str)

def removeDuplicates_OneLiner_OrderDoesNotMatter(str):
    return "".join(set(str))

def removeDuplicates_OrderMatters(str):
    if not str:
        return ""

    unique = set(str)
    result = []

    for char in str:
        if char in unique:
            result.append(char)
            unique.remove(char)

    return "".join(result)


# Main program
print("\nOrder does not matter")
print("Input: %s  Output: %s" %("aabadcdc", removeDuplicates_OrderDoesNotMatter("aabadcdc")))
print("Input: %s  Output: %s" %("a", removeDuplicates_OrderDoesNotMatter("a")))
print("Input: %s  Output: %s" %("abc", removeDuplicates_OrderDoesNotMatter("abc")))
print("Input: %s  Output: %s" %("aaabbbaaabbccaa", removeDuplicates_OrderDoesNotMatter("aaabbbaaabbccaa")))
print("Input: %s  Output: %s" %("aaa", removeDuplicates_OrderDoesNotMatter("aaa")))

print("\nOrder does not matter - One Liner")
print("Input: %s  Output: %s" %("aabadcdc", removeDuplicates_OneLiner_OrderDoesNotMatter("aabadcdc")))
print("Input: %s  Output: %s" %("a", removeDuplicates_OneLiner_OrderDoesNotMatter("a")))
print("Input: %s  Output: %s" %("abc", removeDuplicates_OneLiner_OrderDoesNotMatter("abc")))
print("Input: %s  Output: %s" %("aaabbbaaabbccaa", removeDuplicates_OneLiner_OrderDoesNotMatter("aaabbbaaabbccaa")))
print("Input: %s  Output: %s" %("aaa", removeDuplicates_OneLiner_OrderDoesNotMatter("aaa")))

print("\nOrder does matter")
print("Input: %s  Output: %s" %("aabadcdc", removeDuplicates_OrderMatters("aabadcdc")))
print("Input: %s  Output: %s" %("a", removeDuplicates_OrderMatters("a")))
print("Input: %s  Output: %s" %("abc", removeDuplicates_OrderMatters("abc")))
print("Input: %s  Output: %s" %("aaabbbaaabbccaa", removeDuplicates_OrderMatters("aaabbbaaabbccaa")))
print("Input: %s  Output: %s" %("aaa", removeDuplicates_OrderMatters("aaa")))


