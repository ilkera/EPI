# Problem: Write a function to detect if two trees are isomorphic.
#  Two trees are called isomorphic if one of them can be obtained from other by a series of flips,
# i.e. by swapping left and right children of a number of nodes.
# Any number of nodes at any level can have their children swapped.
# Two empty trees are isomorphic.

# Tree definition
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Functions

def isomorphic(first, second):
    if not first and not second:
        return True

    if not first or not second:
        return False

    if first.value != second.value:
        return False

    return (isomorphic(first.left,second.left) and isomorphic(first.right, second.right)) or\
     (isomorphic(first.left, second.right) and isomorphic(first.right, second.left))

# Main program

first = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6)))
second = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7))))
same = TreeNode(1, TreeNode(2), TreeNode(3))
invalid_first = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3, TreeNode(7), TreeNode(8)))
invalid_second = TreeNode(1, TreeNode(2, TreeNode(6), TreeNode(11)), TreeNode(3, TreeNode(8), TreeNode(7)))

# Valid
print(isomorphic(None, None))
print(isomorphic(None, TreeNode(1)))
print(isomorphic(TreeNode(1), None))
print(isomorphic(first, second))
print(isomorphic(same, same))

# Invalid
print(isomorphic(invalid_first, invalid_second))