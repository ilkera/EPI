# Problem: Verify Identical Tree

# Tree Definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# TreeUtils
class TreeUtils:
    def isIdentical(self, first, second):
        if not first and not second:
            return True

        if not first or not second:
            return False

        if first.value != second.value:
            return False

        return self.isIdentical(first.left, second.left) and self.isIdentical(first.right, second.right)

import unittest

class IdenticalTreeUnitTests(unittest.TestCase):
    def test_NullTree(self):
        utils = TreeUtils()
        self.assertEqual(True, utils.isIdentical(None, None))

    def test_OneNullTree(self):
        utils = TreeUtils()
        self.assertEqual(False, utils.isIdentical(None, TreeNode(1)))
        self.assertEqual(False, utils.isIdentical(TreeNode(1), None))

    def test_IdenticalTree(self):
        utils = TreeUtils()
        first = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        second = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(True, utils.isIdentical(first, second))

    def test_NotIdenticalTree(self):
        utils = TreeUtils()
        first = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        second = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7, TreeNode(11))))
        self.assertEqual(False, utils.isIdentical(first, second))

