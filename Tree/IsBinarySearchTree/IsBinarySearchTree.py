# Problem: Validate a binary tree is a binary search tree

# Binary Tree
class BinaryTree:
    def __init__(self, value, left = None, right=None):
        self.value = value
        self.left = left
        self.right = right

import sys
class BinarySearchTree:
    @staticmethod
    def isBst(tree):
        if not tree:
            return True

        if not tree.left and not tree.right:
            return True

        min = -sys.maxsize - 1
        max = sys.maxsize
        return BinarySearchTree.isBstHelper(tree, min, max)

    @staticmethod
    def isBstHelper(tree, min, max):
        if not tree:
            return True

        if tree.value < min or tree.value > max:
            return False

        return BinarySearchTree.isBstHelper(tree.left, min, tree.value) and\
               BinarySearchTree.isBstHelper(tree.right, tree.value, max)

import unittest
class BinarySearchTreeTests(unittest.TestCase):
    def test_EmptyTreeIsBst(self):
        tree = None
        self.assertEqual(True, BinarySearchTree.isBst(tree))

    def test_SingleNodeTreeIsBst(self):
        tree = BinaryTree(1)
        self.assertEqual(True, BinarySearchTree.isBst(tree))

    def test_ParentIsGreaterThanLeftAndSmallerThanRightChild(self):
        tree = BinaryTree(4, BinaryTree(2), BinaryTree(5))
        self.assertEqual(True, BinarySearchTree.isBst(tree))

    def test_ParentIsEqualToLeftAndSmallerThanRightChild(self):
        tree = BinaryTree(4, BinaryTree(4), BinaryTree(5))
        self.assertEqual(True, BinarySearchTree.isBst(tree))

    def test_ParentIsGreaterThanLeftChildButNotGrandChildren(self):
        tree = BinaryTree(10, BinaryTree(6, BinaryTree(8), BinaryTree(9)), BinaryTree(15))
        self.assertEqual(False, BinarySearchTree.isBst(tree))

    def test_ParentIsLessThanRightChildButNotGrandChildren(self):
        tree = BinaryTree(10, BinaryTree(6), BinaryTree(16, BinaryTree(8), BinaryTree(21)))
        self.assertEqual(False, BinarySearchTree.isBst(tree))