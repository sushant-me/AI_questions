"""
31–40: Lists
"""

# Example 31: Creating a List
my_list = [1, 2, 3, 4, 5]

# Example 32: Accessing List Elements
first_element = my_list[0]

# Example 33: Adding Elements to a List
my_list.append(6)

# Example 34: Removing Elements from a List
my_list.remove(3)

# Example 35: List Slicing
sub_list = my_list[1:4]

# Example 36: List Length
length = len(my_list)

# Example 37: Iterating Through a List
for item in my_list:
    print(item)

# Example 38: List Comprehension
squared_list = [x**2 for x in my_list]

# Example 39: List Sorting
my_list.sort()

# Example 40: List Reversing
my_list.reverse()