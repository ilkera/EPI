# Problem : Mirror binary tree
# Suppose i have this tree:

#                   1
#           2             3
#                        4  5
#Then the mirror image will be:

#                   1
#           3               2
#        5     4

# Tree definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


# Tree Utils
class TreeUtils:
    def isSame(self, tree1, tree2):
        if not tree1 and not tree2:
            return True

        if not tree1:
            return False

        if not tree2:
            return False

        if tree1.value != tree2.value:
            return False

        return self.isSame(tree1.left, tree2.left) and self.isSame(tree1.right, tree2.right)


    def mirror(self, tree):
        if not tree:
            return None

        mirror_tree = TreeNode(tree.value)
        mirror_tree.left = self.mirror(tree.right)
        mirror_tree.right = self.mirror(tree.left)

        return mirror_tree

# Main progrma
utils = TreeUtils()
tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
mirror = utils.mirror(tree)

expected = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(4)), TreeNode(2))
print(utils.isSame(mirror, expected))

