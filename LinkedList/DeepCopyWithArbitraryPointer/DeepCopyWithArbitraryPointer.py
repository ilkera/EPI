# Problem: Deep copy with arbitrary pointer

# Node definition
class Node:
    def __init__(self, value, next = None, random = None):
        self.value = value
        self.next = next
        self.random = random

# functions
def deepCopy(head):
    if not head:
        return None

    clone = Node(0)  # sentinel
    clone_iterator, main_iterator = clone, head
    random_lookup = {}

    # First clone the next pointers
    while main_iterator:
        clone_iterator.next = Node(main_iterator.value)
        clone_iterator = clone_iterator.next
        random_lookup[main_iterator] = clone_iterator
        main_iterator = main_iterator.next

    main_iterator = head

    # Second Copy random pointers
    while main_iterator:
        random_lookup[main_iterator].random = random_lookup[main_iterator.random]
        main_iterator = main_iterator.next

    return clone.next

def printNode(head):
    if not head:
       return

    iterator = head

    while iterator:
        print("Value: %d Random: %d" %(iterator.value, iterator.random.value))
        iterator = iterator.next

# Main program

fifth = Node(5, next =None)
fourth = Node(4, next = fifth)
third = Node(3, next = fourth)
second = Node(2, next = third)
first = Node(1, next = second)

first.random = third
second.random = fourth
third.random = fifth
fourth.random = first
fifth.random = third

printNode(first)

print("Clone...")
clone = deepCopy(first)
printNode(clone)

