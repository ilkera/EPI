# Problem: Remove duplicates from linked list
# In: 12->11->12->21->41->43->21
# Out: 12->11->21->41->43

# Linked list definition
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# Functions

def printList(list):
    iterator = list
    while iterator != None:
        print("%d" %iterator.value, end="")

        if iterator.next:
           print("->", end="")

        iterator = iterator.next
    print("")

def removeDuplicates(list):
    if not list:
        return None

    seen_nodes = set()
    iterator = list
    previous = None

    while iterator:
        if iterator.value in seen_nodes:
            previous.next = iterator.next
        else:
            seen_nodes.add(iterator.value)
            previous = iterator

        iterator = iterator.next

    return list

# Main program
list = Node(12, Node(11, Node(12, Node(21, Node(41, Node(43, Node(21)))))))
printList(list)
result = removeDuplicates(list)
printList(result)

list = Node(1, Node(1, Node(1, Node(2, Node(2, Node(2, Node(1)))))))
printList(list)
result = removeDuplicates(list)
printList(result)