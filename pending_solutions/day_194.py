def count_frequency(lst):
    """
    Count frequency of elements in list.
    """
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency