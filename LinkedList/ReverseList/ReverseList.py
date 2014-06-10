# Problem: Reverse a linked list

# Function
def reverse(list):
    current = list
    previous = None

    while current != None:
        next = current.nextNode
        current.nextNode = previous
        previous = current
        current = next

    return previous

def reverse_recursive_helper(current, previous):
    if not current:
        return previous

    next = current.nextNode
    current.nextNode = previous

    return reverse_recursive_helper(next, current)

def reverse_recursive(list):
    if not list:
        return None

    new_head = reverse_recursive_helper(list, None)

    return new_head

def printList(list):
    iterator = list
    while iterator != None:
        print("%d -" %iterator.nodeValue, end="")
        iterator = iterator.nextNode
    print("")

# Node definition
class Node:
    nodeValue = None
    nextNode = None

    def __init__(self, value, nextNode=None):
        self.nodeValue = value
        self.nextNode = nextNode

# Main program
print("Iterative version")
list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
printList(list)
reversed = reverse(list)
printList(reversed)

# Recursive version
print("Recursive version")
input = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
printList(input)
reversed = reverse_recursive(input)
printList(reversed)