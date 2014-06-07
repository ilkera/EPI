# Problem : Add two integers
# Integer representation in list Number: 123 as [3, 2, 1]
# So 123 + 109 = 232
# e.g. [3, 2, 1] and [9, 0, 1] = [2, 3, 2]
# Assumption: all positive

# Linked List Definition
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


# Functions
def printList(head):
    if not head:
        print("Empty list")
        return

    iterator = head

    while iterator:
        print("%d " % iterator.value, end="")

        if iterator.next != None:
            print(" - ", end ="")
        iterator = iterator.next

    print("")

def add(intOne, intTwo):
    if not intOne:
        return intTwo

    if not intTwo:
        return intOne

    result = Node(0)
    iterator_one, iterator_two, iterator_result = intOne, intTwo, result
    carry = 0

    while iterator_one or iterator_two:
        if iterator_one and iterator_two:
            current_sum = iterator_one.value + iterator_two.value + carry
            iterator_one, iterator_two = iterator_one.next, iterator_two.next
        elif iterator_one:
            current_sum = iterator_one.value + carry
            iterator_one = iterator_one.next
        else:
            current_sum = iterator_two.value + carry
            iterator_two = iterator_two.next

        carry = int(current_sum / 10)
        iterator_result.next = Node(current_sum % 10)
        iterator_result = iterator_result.next

    if carry > 0:
        iterator_result.next = Node(carry)

    return result.next

# Main program
print("123 + 109")
first = Node(3, Node(2, Node(1)))
second = Node(9, Node(0, Node(1)))
result = add(first, second)
printList(result)

print("\n99 + 1")
first = Node(9, Node(9))
second = Node(1)
result = add(first, second)
printList(result)

print("\n999 + 101")
first = Node(9, Node(9, Node(9)))
second = Node(1, Node(0, Node(1)))
result = add(first, second)
printList(result)

print("\n64957 + 48")
first = Node(7, Node(5, Node(9, Node(4, Node(6)))))
second = Node(8, Node(4))
result = add(first, second)
printList(result)
