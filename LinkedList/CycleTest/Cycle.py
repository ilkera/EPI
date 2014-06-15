# Problem: Check if linked list has cycle

# Linked list definition
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def hasCycle(head):
    if not head:
        return False

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Main program
root = Node(0)
cycled = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, root))))))
root.next = cycled

print(hasCycle(root))
print(hasCycle(Node(1)))
print(hasCycle(Node(1, Node(2))))

# special case
root = Node(1)
cycled = Node(2, root)
root.next = cycled
print(hasCycle(root))