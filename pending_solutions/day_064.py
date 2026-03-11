def rotate_list_right(lst, k):
    """
    Write a program to rotate a list to the right.
    """
    k = k % len(lst)
    return lst[-k:] + lst[:-k]