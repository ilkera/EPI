# You are given a linked list and an integer k.
# Reverse every alternative k nodes of the given linked list.
# E.g: List 1->2->3->4->5->6->7->8->9->NULL   k=3
# Result: 3->2->1->4->5->->6->9->8->7->NULL

# List definition
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# Functions
def reverseAlternateNodes(list, groupSize):
    if not list:
        return

    should_reverse = True
    iterator = list
    current_group_size = 0
    begin, end = list, None
    newHead, previous, reversed, previous_group_end = None, None, None, None

    while iterator:
        if not current_group_size == groupSize:
            current_group_size += 1
            previous = iterator
            iterator = iterator.next
            continue

        if should_reverse:
            end = iterator
            reversed = reverseNodes(previous_group_end, begin, end)

            if not newHead:
               newHead = reversed

            if previous_group_end:
                previous_group_end.next = reversed

            should_reverse = False
        else:
            should_reverse = True
            begin = iterator

        current_group_size = 1
        previous_group_end = previous
        previous = iterator
        iterator = iterator.next

    reversed = reverseNodes(previous_group_end, begin, None)
    previous_group_end.next = reversed

    return newHead

def printList(head):
    if not head:
        print("Empty list")
        return

    iterator = head

    while iterator:
        print("%d -" % iterator.value, end="")
        iterator = iterator.next

    print("")

def reverseNodes(preNode, begin, end):

    if not begin:
        return None

    iterator = begin
    previous = preNode

    while iterator and iterator != end:
        next = iterator.next
        iterator.next = previous
        previous = iterator
        iterator = next

    reverse_begin = previous
    begin.next = end

    return reverse_begin

# Main Program
list = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))
printList(list)
result = reverseAlternateNodes(list, 3)
printList(result)





