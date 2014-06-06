# Problem: Find duplicate item(s) in an array where array contains integers range from 1 to N+1

# Let's say you have a list of N+1 integers between 1 and N. You know there's at least one duplicate,
# but there might be more.
# For example, if N=3, your list might be 3, 1, 1, 3 or it might be 1, 3, 2, 2.
# Print out a number that appears in the list more than once.
# (That is, in the first example, you can print '1' or '3' -- you don't have to print both.)

def find_duplicates_viaSorting(list):
    if not list:
        return []

    sorted_list = sorted(list)
    duplicates = set()
    index = 1

    while index < len(sorted_list):
        if sorted_list[index - 1] == sorted_list[index]:
            if not sorted_list[index] in duplicates:
                duplicates.add(sorted_list[index])
            index += 1
            continue

        index += 1

    return duplicates

def find_duplicates_viaSorting_WithoutSet(list):
    if not list:
        return []

    sorted_list = sorted(list)
    duplicates = []
    index = 1

    while index < len(sorted_list):
         if sorted_list[index - 1] == sorted_list[index]:
             if duplicates[:-1] != sorted_list[index]:
                 duplicates.append(sorted_list[index])
         index += 1

    return duplicates

def find_duplicates_viaSet(list):
    if not list:
        return []

    number_set = set()
    duplicates = []

    for item in list:
        if not item in number_set:
            number_set.add(item)
        else:
            duplicates.append(item)

    return duplicates

# Main program
print("Find duplicates via sorting")
print(find_duplicates_viaSorting([3, 1, 1, 3]))
print(find_duplicates_viaSorting([2, 1, 3, 2]))

print("Find duplicates via sorting without set")
print(find_duplicates_viaSorting_WithoutSet([3, 1, 1, 3]))
print(find_duplicates_viaSorting_WithoutSet([2, 1, 3, 2]))

print("Find duplicates via set")
print(find_duplicates_viaSet([3, 1, 1, 3]))
print(find_duplicates_viaSet([2, 1, 3, 2]))


