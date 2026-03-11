def postorder_traversal(root):
    """
    Traverse tree using postorder traversal.
    """
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]