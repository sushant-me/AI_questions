"""
Find mode of list.
"""

def find_mode(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_freq = max(frequency.values())
    mode = [item for item, freq in frequency.items() if freq == max_freq]
    return mode