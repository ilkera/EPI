# Problem: Interweave linked list
# Input: A->B->C->D->E Output: A->E->B->D->C

# Node definition

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


# Functions
class ListUtils:
    def interweave(self, list):
       left, right = self.divideList(list)
       right_reversed = self.reverse(right)
       result = self.merge(left, right_reversed)

       return result

    def divideList(self, list):
        left_begin, right_begin = list, None
        previous, iterator_slow, iterator_fast = None, list, list

        while iterator_fast and iterator_fast.next:
            iterator_fast = iterator_fast.next.next
            previous = iterator_slow
            iterator_slow = iterator_slow.next

        # Handle left end
        previous.next = None

        right_begin = iterator_slow

        return left_begin, right_begin

    def reverse(self, list):
        if not list:
            return

        iterator, previous = list, None
        while iterator:
            next = iterator.next
            iterator.next = previous
            previous = iterator
            iterator = next

        return previous

    def merge(self, first, second):
        if not first and not second:
            return None

        if not first:
            return second

        if not second:
            return first

        merged_head = first
        iterator_merged, iterator_first, iterator_second = merged_head, first, second

        iterator_first = iterator_first.next
        merge_from_second = True

        while iterator_first and iterator_second:
            if merge_from_second:
                iterator_merged.next = iterator_second
                iterator_second = iterator_second.next
            else:
                iterator_merged.next = iterator_first
                iterator_first = iterator_first.next

            merge_from_second = not merge_from_second
            iterator_merged = iterator_merged.next

        if iterator_first:
            iterator_merged.next = iterator_first

        if iterator_second:
            iterator_merged.next = iterator_second

        return merged_head

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

# Main program

list = Node(1, Node(2, Node(3, Node(4, Node(5)))))
utils = ListUtils()
result = utils.interweave(list)
printList(result)




