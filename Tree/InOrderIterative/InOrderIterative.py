# Problem: Implement in-order traversal iterative
# e.g. Tree
#       1
#   2       3
# 4  6    7   9
# In-Order: 4 2 6 1 7 3 9

# Tree definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Function
def inOrder(tree):
    if not tree:
        return

    stack = []
    current = tree

    while stack or current:
        if not current:
            current = stack.pop()
            print("%d " %current.value, end="")
            current = current.right
        else:
            stack.append(current)
            current = current.left

# Main Program
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(7), TreeNode(9)))
inOrder(tree)
