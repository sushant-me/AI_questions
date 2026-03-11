"""
Advanced Lists
"""

# Create a list of tuples with student names and their scores
students = [('Alice', 88), ('Bob', 92), ('Charlie', 78), ('David', 95)]

# Sort the list by scores in descending order
students.sort(key=lambda x: x[1], reverse=True)

# Print the sorted list
print(students)