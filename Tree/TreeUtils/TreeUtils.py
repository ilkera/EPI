
# Binary Tree
class BinaryTree:
    def __init__(self, value, left = None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeUtils:
    @staticmethod
    def printPreOrderRecursive(tree):
        if not tree:
            return

        print("%s " %tree.value, end="")
        TreeUtils.printPreOrderRecursive(tree.left)
        TreeUtils.printPreOrderRecursive(tree.right)

    @staticmethod
    def printInOrderRecursive(tree):
        if not tree:
            return

        TreeUtils.printInOrderRecursive(tree.left)
        print("%s " %tree.value, end="")
        TreeUtils.printInOrderRecursive(tree.right)

    @staticmethod
    def printPostOrderRecursive(tree):
        if not tree:
            return

        TreeUtils.printPostOrderRecursive(tree.left)
        TreeUtils.printPostOrderRecursive(tree.right)
        print("%s " %tree.value, end="")