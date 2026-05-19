"""
Tuples
"""

# Define a tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)

# Access the second element of the tuple
second_element = mixed_tuple[1]

# Create a new tuple with elements from an existing tuple and additional elements
new_tuple = mixed_tuple + (42, "world")

# Check if an element exists in the tuple
element_exists = 3.14 in mixed_tuple

# Iterate over the elements in the tuple
for element in mixed_tuple:
    print(element)

# Get the number of elements in the tuple
tuple_length = len(mixed_tuple)

# Convert a list to a tuple
list_to_tuple = tuple([1, 2, 3])

# Unpack a tuple into multiple variables
a, b, c, d = mixed_tuple

# Print the results
print("Second element:", second_element)
print("New tuple:", new_tuple)
print("Element exists:", element_exists)
print("Tuple length:", tuple_length)
print("List to tuple:", list_to_tuple)
print("Unpacked elements:", a, b, c, d)