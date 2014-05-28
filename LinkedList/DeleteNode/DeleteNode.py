# Problem: Delete node in a linked list

# Node definition

class Node:
    nodeValue = None
    nextNode = None

    def __init__(self, value, next = None):
        self.nodeValue = value
        self.nextNode = next

# Functions

# e.g. 1, 2, 3, 4, 5  - delete 5 => 1, 2, 3, 4

def createList(list):
    if not list or len(list) < 1:
        return None

    head = Node(list[0])
    iterator = head

    for index in range(1, len(list)):
        iterator.nextNode = Node(list[index])
        iterator = iterator.nextNode

    return head

def printList(head):
    if not head:
        print("Empty list")
        return

    iterator = head

    while iterator:
        print("%d -" % iterator.nodeValue, end="")
        iterator = iterator.nextNode

    print("")

def deleteNode(head, nodeValue):
    if not head:
        print("Can't delete from Empty/null list")
        return None

    # delete duplicates in the beginning
    while head.nextNode and head.nodeValue == nodeValue:
        head = head.nextNode

    # All duplicates case
    if not head.nextNode:
        if head.nodeValue == nodeValue:
            return None
        else:
            return head

    iterator = head
    previous = None

    while iterator.nextNode:
        if iterator.nodeValue == nodeValue:
            previous.nextNode = iterator.nextNode
            iterator = iterator.nextNode
            continue

        previous = iterator
        iterator = iterator.nextNode

    # delete if node is at the end
    if iterator.nodeValue == nodeValue:
        previous.nextNode = None

    return head

# Main program

# Case 1: Node doesn't exist - Ok
print("CASE 1")
case1 = createList([1, 2, 3, 4, 5])
printList(case1)
case1 = deleteNode(case1, 6)
printList(case1)

# Case 2: Node is at head - Ok
print("CASE 2")
case2 = createList([1, 2, 3, 4, 5])
printList(case2)
case2 = deleteNode(case2, 1)
printList(case2)
# Case 3: Node is in the middle - Ok
print("CASE 3")
case3 = createList([1, 2, 3, 4, 5])
printList(case3)
case3 = deleteNode(case3, 3)
printList(case3)
# Case 4: Node is at the end - Ok
print("CASE 4")
case4 = createList([1, 2, 3, 4, 5])
printList(case4)
case4 = deleteNode(case4, 5)
printList(case4)

# Case 5: Remove a duplicate item (DUP in mid) (1, 1, 2 : remove 1)
print("CASE 5")
case5 = createList([1, 2, 3, 3, 5])
printList(case5)
case5 = deleteNode(case5, 3)
printList(case5)

# Case 6: All duplicates
print("CASE 6")
case6 = createList([1, 1, 1, 1, 1])
printList(case6)
case6 = deleteNode(case6, 1)
printList(case6)

# Case 7: None/Empty list - Ok
print("CASE 7")
case7 = createList([])
printList(case7)
case7 = deleteNode(case7, 1)
printList(case7)

# Case 8: Remove a duplicate item (DUP in end) (1, 2, 2, 2 : remove 2)
print("CASE 8")
case8 = createList([1, 2, 2, 2])
printList(case8)
case8 = deleteNode(case8, 2)
printList(case8)

# Case 9: Remove a duplicate item (DUP in random) (1, 2, 2, 3, 4, 6, 2, 2, 8 : remove 2)
print("CASE 9")
case9 = createList([1, 2, 2, 3, 4, 6, 2, 2, 8])
printList(case9)
case9 = deleteNode(case9, 2)
printList(case9)

# Case 10: One item list
print("CASE 10")
case10 = createList([6])
printList(case10)
case10 = deleteNode(case10, 5)
printList(case10)