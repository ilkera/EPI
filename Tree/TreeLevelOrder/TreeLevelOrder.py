# Prolem: Level order tree

# Tree definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Tree level order print
def printLevel(tree):
    if not tree:
        return

    current_level_count, next_level_count = 0, 0
    queue = []

    queue.append(tree)
    current_level_count += 1

    while queue:
        current_node = queue.pop(0)
        print("%d " %current_node.value, end="")
        current_level_count -= 1

        if current_node.left:
            queue.append(current_node.left)
            next_level_count += 1

        if current_node.right:
            queue.append(current_node.right)
            next_level_count += 1

        if current_level_count == 0:
            print("")
            current_level_count = next_level_count
            next_level_count = 0

# Find height
def getHeight(tree):
    if not tree:
        return 0
    else:
        return 1 + max(getHeight(tree.left), getHeight(tree.right))

def printLevel_recursive_helper(tree, level):
    if level <= 1:
        print("%d " %tree.value, end="")
    else:
        printLevel_recursive_helper(tree.left, level - 1)
        printLevel_recursive_helper(tree.right, level - 1)

def printLevel_recursive(tree):
    if not tree:
        return

    height = getHeight(tree)

    for level in range(1, height + 1):
        printLevel_recursive_helper(tree, level)
        print("")

# Main program

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(5), TreeNode(7)))
print("Iterative")
printLevel(tree)
print("Recursive")
printLevel_recursive(tree)

