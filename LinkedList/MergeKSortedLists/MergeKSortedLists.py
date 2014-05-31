# Problem: Merge k sorted linked lists.

# e.g.
# list1 [1, 4, 7]
# list2 [2, 6, 9[
# list3 [3, 5, 8]
# Output = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Linked List
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


# Functions

import heapq

# Print Linked list
def printList(head):
    if not head:
        print("Empty")
        return

    iterator = head

    while iterator:
        print("%d - " %iterator.value, end="")
        iterator = iterator.next
    print("")


def merge(lists):
    if not lists:
        return None

    heap = []
    for list in lists:
        heapq.heappush(heap, (list.value, list))

    iterator = heapq.heappop(heap)[1]
    result = iterator

    if iterator.next:
        heapq.heappush(heap, (iterator.next.value, iterator.next))

    while heap:
        current = heapq.heappop(heap)[1]
        iterator.next = current

        if current.next:
            heapq.heappush(heap, (current.next.value, current.next))
        iterator = iterator.next

    return result

# Main Program
list1 = Node(1, Node(4, Node(7, Node(11))))
list2 = Node(2, Node(6, Node(9)))
list3 = Node(3, Node(5, Node(8)))

printList(list1)
printList(list2)
printList(list3)

lists = [list1, list2, list3]
merged = merge(lists)
printList(merged)

