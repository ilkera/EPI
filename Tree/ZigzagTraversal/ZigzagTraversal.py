# Problem: Zigzag Tree Traversal

# Tree Definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def zigzagTraverse(tree):
    if not tree:
        return

    current_level, next_level = [], []
    current_level.append(tree)
    left_to_right = True

    while current_level:
        current = current_level.pop()
        if current:
            print("%d "%current.value, end="")
            if left_to_right:
                next_level.append(current.left)
                next_level.append(current.right)
            else:
                next_level.append(current.right)
                next_level.append(current.left)

        if not current_level:
            left_to_right = not left_to_right
            temp = current_level
            current_level = next_level
            next_level = temp
            print("")

# Main program
tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
zigzagTraverse(tree)

