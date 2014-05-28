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
list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

# Iterate main list
printList(list)

# Reverse the list
reversed = reverse(list)

print("List is reversed")

printList(reversed)