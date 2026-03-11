def inorder_traversal(root):
    """
    Traverse tree using inorder traversal.
    """
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)