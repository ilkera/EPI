# Problem: Find intersection point of two connected linked lists

# Linked List Definition

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


def findLength(list):
    if not list:
        return 0

    iterator, length = list, 0

    while iterator:
        length += 1
        iterator = iterator.next

    return length

def getNode(list, index):
    if not list:
        return None

    iterator = list
    step_taken = 0
    while iterator and step_taken < index:
            step_taken += 1
            iterator = iterator.next

    return iterator

# Functions
def findIntersection(first_list, second_list):
    if not first_list or not second_list:
        return None

    first_list_length, second_list_length = findLength(first_list), findLength(second_list)
    diff = abs(second_list_length-first_list_length)

    first_iterator, second_iterator = first_list, second_list

    if diff > 0:
        if first_list_length > second_list_length:
            first_iterator = getNode(first_list, diff)
        else:
            second_iterator = getNode(second_list, diff)

    while first_iterator and second_iterator and first_iterator != second_iterator:
        first_iterator = first_iterator.next
        second_iterator = second_iterator.next

    if first_iterator == second_iterator:
        return first_iterator
    else:
        return None

# Main Program

intersection = Node(9, Node(10, Node(11)))
first = Node(1, Node(2,Node(5, Node(7, Node(8, intersection)))))
second = Node(6, Node(4, intersection))

result = findIntersection(first, second)
print("Intersection value is %d" %result.value)

# No intersection case
first = Node(1, Node(2, Node(3)))
second = Node(5, Node(6, Node(7)))

result = findIntersection(first, second)
if not result:
    print("No intersection")
