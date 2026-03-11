def tree_height(tree):
    if tree is None:
        return 0
    return 1 + max(tree_height(tree.left), tree_height(tree.right))