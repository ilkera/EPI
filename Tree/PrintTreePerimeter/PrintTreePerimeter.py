# Problem: Print tree perimeter
#Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root.
#For example, boundary traversal of the following tree is “20 8 4 10 14 25 22″
#       20
#    8           22
# 4       12          25
#        10  14

# Tree definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def printTreeLeaves(tree):
    if not tree:
        return

    printTreeLeaves(tree.left)

    if not tree.left and not tree.right:
        print("%d " %tree.value, end="")

    printTreeLeaves(tree.right)

def printTreeBoundaryLeft(tree):
    if not tree:
        return

    if tree.left:
        print("%d " %tree.value, end="")
        printTreeBoundaryLeft(tree.left)
    elif tree.right:
        print("%d " %tree.value, end="")
        printTreeBoundaryLeft(tree.right)

def printTreeBoundaryRight(tree):
    if not tree:
        return

    if tree.right:
        printTreeBoundaryRight(tree.right)
        print("%d " %tree.value, end="")
    elif tree.left:
        printTreeBoundaryRight(tree.left)
        print("%d " %tree.value, end="")

def printTreeBoundary(tree):
    if not tree:
        return

    print("%d " %tree.value, end="")

    printTreeBoundaryLeft(tree.left)

    printTreeLeaves(tree.left)
    printTreeLeaves(tree.right)

    printTreeBoundaryRight(tree.right)


# Main program
tree = TreeNode(20, TreeNode(8, TreeNode(4), TreeNode(12, TreeNode(10), TreeNode(14))), TreeNode(22, None, TreeNode(25)))
printTreeBoundary(tree)