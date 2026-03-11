def linear_search(arr, x):
    """
    Implement Linear Search.
    
    This function searches for a given element x in a list arr using linear search algorithm.
    It returns the index of the element if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1