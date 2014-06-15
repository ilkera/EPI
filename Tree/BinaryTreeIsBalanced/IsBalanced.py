# Problem: Binary Tree Is Balanced

# Tree definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Tree Utils
def isBalanced(tree):
    if not tree:
        return True

    left_height = height(tree.left)
    right_height = height(tree.right)

    if abs(left_height - right_height) > 1:
        return False
    else:
        return isBalanced(tree.left) and isBalanced(tree.right)

def get_height(tree):
    if not tree:
        return 0

    left_height = get_height(tree.left)
    if left_height == -1:
        return -1  # not balanced

    right_height = get_height(tree.right)
    if right_height == -1:
        return -1  # not balanced

    height_diff = abs(left_height - right_height)

    if height_diff > 1:
        return -1
    return max(left_height, right_height) + 1

def isBalanced_optimized(tree):
    return get_height(tree) != -1

def height(tree):
    if not tree:
        return 0

    return 1 + max(height(tree.left), height(tree.right))

# Main program
balanced_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
unbalanced_tree = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))))
print(isBalanced(balanced_tree))
print(isBalanced(unbalanced_tree))

print(isBalanced_optimized(balanced_tree))
print(isBalanced_optimized(unbalanced_tree))
