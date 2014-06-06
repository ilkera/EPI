# Problem: PreOrder Iterative
# e.g. Tree
#       1
#   2       3
# 4  6    7   9
# PreOrder: 1 2 4 6 3 7 9

# Tree definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Functions
def preOrder_Iterative(tree):
    if not tree:
        return

    stack = []
    stack.append(tree)

    while stack:
        current = stack.pop()
        print("%d " %current.value, end="")

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
# Main program
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(7), TreeNode(9)))
preOrder_Iterative(tree)