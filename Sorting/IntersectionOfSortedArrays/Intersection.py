# Problem: Compute the intersection of two sorted arrays

# Given sorted arrays A and B of lengths n and m respectively, return
# an array C containing elements common to A and B. The array C should be free of
# duplicates. How would you perform this intersection if—(1.) n  m and (2.) n  m?

# Functions

# Where n ~ m
# 1. Loop through the lists
# 2. When first == second, add to the hash set
# 2.1 If first > second, increment second
# 2.2 Else increment first
def intersection_v1(listFirst, listSecond):
    if not listFirst or not listSecond:
        return None

    intersection = set()

    len_first = len(listFirst)
    len_second = len(listSecond)
    index_first = 0
    index_second = 0

    while index_first < len_first and index_second < len_second:
        if listFirst[index_first] == listSecond[index_second]:
            intersection.add(listFirst[index_first])
            index_first += 1
            index_second += 1
        elif listFirst[index_first] > listSecond[index_second]:
            index_second += 1
        else:
            index_first += 1

    return intersection

# n <= m
# We can leverage binary search here. For each item in n (first list),
# we call binary search in the second list
# Running time: O(nlogm)

def search(number , list):
    if not list:
        return False

    high = len(list)
    low = 0

    while low <= high:
        mid = int(low + (high - low) / 2)
        if list[mid] == number:
            return True
        elif list[mid] > number:
            high = mid - 1
        else:
            low = mid + 1

    return False

def intersection_v2(listFirst, listSecond):
    intersection = set()
    for number in listFirst:
        if search(number, listSecond) and number not in intersection:
            intersection.add(number)
    return intersection

# Main Program

first = [1, 4, 7, 8, 8, 10, 12, 15]
second = [2, 4, 8, 11, 12, 16, 17]

result = intersection_v1(first, second)
print("%s" %result)

short =  [2, 3, 12]
long = [0, 1, 3, 7, 8, 9, 10, 11, 12 , 13, 14]

result = intersection_v2(short, long)
print("%s " %result)