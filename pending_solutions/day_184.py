""" Traverse tree using preorder traversal. """

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is not None:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# preorder_traversal(root)
# Output: 1 2 4 5 3