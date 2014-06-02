# Problem: Find the nth node from last
# e.g. {1, 2, 3, 4, 5} n= 4, return 2

# Linked list definition
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

# Functions

class ListUtils:
    def returnNthNode(self, list, n):
        if not list:
            raise Exception("List is empty/null")
        if n < 1:
            raise Exception("N must me greater than 0")

        slow_iterator, fast_iterator = list, list

        while fast_iterator:
            if n == 0:
                slow_iterator = slow_iterator.next
            else:
                n -= 1
            fast_iterator = fast_iterator.next

        if n != 0:
            raise Exception("n is greater than the length of list")

        return slow_iterator

import unittest

class LinkedListTests(unittest.TestCase):
    def test_EmptyList(self):
        node = None
        utils = ListUtils()
        try:
            utils.returnNthNode(node, 0)
        except Exception as inst:
            self.assertEqual(type(inst), type(Exception("empty")))

    def test_NLessThanOrEqualToZero(self):
        node = Node(1, Node(2))
        utils = ListUtils()
        try:
            utils.returnNthNode(node, 0)
        except Exception as inst:
            self.assertEqual(type(inst), type(Exception("empty")))

    def test_NthFromLast(self):
        node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        utils = ListUtils()
        self.assertEqual(5,utils.returnNthNode(node, 1).value)
        self.assertEqual(4,utils.returnNthNode(node, 2).value)
        self.assertEqual(3,utils.returnNthNode(node, 3).value)
        self.assertEqual(2,utils.returnNthNode(node, 4).value)
        self.assertEqual(1,utils.returnNthNode(node, 5).value)

    def test_NIsGreaterThanListLength(self):
        node = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        utils = ListUtils()

        try:
            utils.returnNthNode(node, 10)
        except Exception as inst:
            self.assertEqual(type(inst), type(Exception("n is greater than list")))