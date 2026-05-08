"""
 Lists & Arrays
"""

# Define a list of integers
my_list = [1, 2, 3, 4, 5]

# Define an array of integers using NumPy
import numpy as np
my_array = np.array([1, 2, 3, 4, 5])

# Accessing elements
first_element_list = my_list[0]
first_element_array = my_array[0]

# Modifying elements
my_list[0] = 10
my_array[0] = 10

# Adding elements
my_list.append(6)
my_array = np.append(my_array, 6)

# Removing elements
my_list.remove(6)
my_array = my_array[:-1]

# Iterating over lists
for element in my_list:
    print(element)

# Iterating over arrays
for element in my_array:
    print(element)

# Slicing lists
sublist = my_list[1:3]

# Slicing arrays
subarray = my_array[1:3]

# Sorting lists
my_list.sort()

# Sorting arrays
my_array = np.sort(my_array)

# Reversing lists
my_list.reverse()

# Reversing arrays
my_array = np.flip(my_array)

# Finding the length of lists
length_list = len(my_list)

# Finding the length of arrays
length_array = my_array.shape[0]

# Checking if an element exists in a list
exists_list = 3 in my_list

# Checking if an element exists in an array
exists_array = np.isin(3, my_array)

# Converting list to array
array_from_list = np.array(my_list)

# Converting array to list
list_from_array = my_array.tolist()