""" Write a program to find the largest element in a list. """

def find_largest_element(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Example usage:
example_list = [3, 5, 1, 8, 2, 9]
print("The largest element is:", find_largest_element(example_list))