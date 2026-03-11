def find_common_elements(*lists):
    """
    Find common elements in multiple lists.
    """
    return set(lists[0]).intersection(*lists[1:])