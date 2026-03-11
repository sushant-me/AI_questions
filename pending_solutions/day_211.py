"""
Plot graph using Matplotlib.
"""

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Add title and labels
plt.title('Sample Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()