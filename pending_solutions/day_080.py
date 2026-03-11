"""
Sets
"""

# Define a function to demonstrate set operations
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    # Union of sets
    union_set = set1.union(set2)
    print("Union of set1 and set2:", union_set)

    # Intersection of sets
    intersection_set = set1.intersection(set2)
    print("Intersection of set1 and set2:", intersection_set)

    # Difference of sets
    difference_set = set1.difference(set2)
    print("Difference of set1 and set2:", difference_set)

    # Symmetric difference of sets
    symmetric_difference_set = set1.symmetric_difference(set2)
    print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# Call the function to display set operations
set_operations()